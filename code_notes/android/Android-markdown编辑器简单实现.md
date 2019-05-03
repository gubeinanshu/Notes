
> 使用 markdown4j 进行解析

步骤：

1. 引入库
```
compile 'org.commonjava.googlecode.markdown4j:markdown4j:2.2-cj-1.1'
```

2. 将Markdown资源转换为Html格式文件
```
//参数markdown：可以为字符串、流、File
String html=new Markdown4jProcessor().process(markdown);
```

3. 使用WebView显示Html
```
webView.loadDataWithBaseURL(null,html,"text/html","utf-8",null);
```


[markdown编辑器简单实现源码下载](http://op9kkp3ga.bkt.clouddn.com/blog_source/code/android/markdown.zip)

[markdown制作过程总结（实验报告）](http://op9kkp3ga.bkt.clouddn.com/blog_source/code/android/markdown%E5%BC%80%E5%8F%91%E6%80%BB%E7%BB%93.docx)