原生ajax请求方式：


```
var xhr = new XMLHttpRequest();  
xhr.open("POST", "http://xxxx.com/demo/b/index.php", true);  
xhr.withCredentials = true; //支持跨域发送cookies
xhr.send();
```

jquery的post方法请求：


```
 $.ajax({
    type: "POST",
    url: "http://xxx.com/api/test",
    dataType: 'jsonp',
    xhrFields: {withCredentials: true},
    crossDomain: true,
})
```

服务器端设置：


```
header("Access-Control-Allow-Credentials: true");
header("Access-Control-Allow-Origin: http://www.xxx.com"); #可以通过在header中获取orign，以此通过所有请求
```
