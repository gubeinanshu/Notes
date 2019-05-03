# form文件上传
```html
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>上传文件</title>
</head>
<body>
    <form id="my_form" name="form" action="/index" method="POST"  enctype="multipart/form-data" >
        <input name="fff" id="my_file"  type="file" />
        <input type="submit" value="提交"  />
    </form>
</body>
</html>

```
> 注意：form文件上传，一定要在form表单上设置enctype的参数。enctype="multipart/form-data"。不然上传无法成功。

# 原生ajax上传文件
```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <input type="file" id="img" />
    <input type="button" onclick="UploadFile();" />
    <script>
        function UploadFile(){
            var fileObj = document.getElementById("img").files[0];
 
            var form = new FormData();
            form.append("k1", "v1");
            form.append("fff", fileObj);
 
            var xhr = new XMLHttpRequest();
            xhr.open("post", '/index', true);
            xhr.send(form);
        }
    </script>
</body>
</html>

```
> 说明：  
代码中利用原生的ajax进行文件上传。
关键点：  
1、获取文件对象，通过files[0]，获取当前上传的文件对象。  
2、通过FormData()，实例化一个对象form对象。  
3、然后将要传递的参数，文件以键和值以逗号分隔的形式append到form对象中去。  
4、然后将整个form对象发送到服务端。  
注意：  
后台代码和上面的代码一样，不变。注意接收的文件名要同步  


# jquery文件上传
```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <input type="file" id="img" />
    <input type="button" onclick="UploadFile();" />
    <script>
        function UploadFile(){
            var fileObj = $("#img")[0].files[0];
            var form = new FormData();
            form.append("k1", "v1");
            form.append("fff", fileObj);
 
            $.ajax({
                type:'POST',
                url: '/index',
                data: form,
                processData: false,  // tell jQuery not to process the data
                contentType: false,  // tell jQuery not to set contentType
                success: function(arg){
                    console.log(arg);
                }
            })
        }
    </script>
</body>
</html>

```
>说明：  
1、和原生的一样，都是显得获取当前上传文件的对象。files[0]；然后实例化form对象，将要传递的内容append到实例化的对象form中。  
2、后台代码同前，注意字段名对应。  
关键点：  
processData:false和contentType:false。这2个是关键。  
默认的jquery会将我们上传的数据做部分处理。上面两段代码，就是告诉jquery不要处理我们的文件，不然会将我们的文件处理得不完整。  


# iframe文件上传
原生的ajax和jquery上传的时候，我们都是通过实例化一个form对象来进行文件的上传。但是实例化这个form的对象并不是所有的浏览器都存在，比如低版本的IE就可能没有合格FormData对象，那上面的方法就存在兼容性，没有form对象就不能发送。因此的使用一个兼容性更好的来进行操作，iframe。
```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <form id="my_form" name="form" action="/index" method="POST"  enctype="multipart/form-data" >
        <div id="main">
            <input name="fff" id="my_file"  type="file" />
            <input type="button" name="action" value="Upload" onclick="redirect()"/>
            <iframe id='my_iframe' name='my_iframe' src=""  class="hide"></iframe>
        </div>
    </form>
 
    <script>
        function redirect(){
            document.getElementById('my_iframe').onload = Testt;
            document.getElementById('my_form').target = 'my_iframe';
            document.getElementById('my_form').submit();
 
        }
         
        function Testt(ths){
            var t = $("#my_iframe").contents().find("body").text();
            console.log(t);
        }
    </script>
</body>
</html>

```
>关键点：  
1、document.getElementById('my_form').target = 'my_iframe'：这段代码就是获取iframe标签。  
 target就是目标，只要给form设置了target的话，form提交的时候，就会提交到这个target指定的目标上。所以上面的代码表示只要form提交，就会提交到iframe上去。  
2、当iframe操作完后会执行Testt方法，Testt方法就是获取后台返回的信息，并打印。  


# tornado 代码
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import tornado.ioloop
import tornado.web
 
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
 
        self.render('index.html')
 
    def post(self, *args, **kwargs):
        file_metas = self.request.files["fff"]
        # print(file_metas)
        for meta in file_metas:
            file_name = meta['filename']
            with open(file_name,'wb') as up:
                up.write(meta['body'])
 
settings = {
    'template_path': 'template',
}
 
application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)
 
 
if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

```
> 说明：  
1、代码中self.request封装了所有发送过来请求的内容。  
2、self.request.files：可以获取上传文件的所有信息。此方法获取的是一个生成器，内部是由yield实现的，因此我们在利用此方法返回的对象的时候，不能通过下标获取里面的对象，只能通过迭代的方法。  
3、迭代出来的对象的filename：就表示上传文件的文件名。  
4、迭代出来的对象的body：表示上传文件的内容。获取的文件内容是字节形式的。