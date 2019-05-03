https://www.cnblogs.com/bobo0609/p/6979462.html  
https://www.cnblogs.com/lincappu/p/8270709.html  
https://www.cnblogs.com/breezey/p/6673901.html

1. OS  用于提供系统级别的操作
2. sys 用于提供对解释器相关的操作
3. subprocess  系统命令操作(os.system , os.spawn* 可以执行shell命令 ， subprocess 模块也可以执行命令并提供了更丰富的功能。)

subprocess模块是python从2.4版本开始引入的模块。主要用来取代 一些旧的模块方法，如os.system、os.spawn*、os.popen*、commands.*等。subprocess通过子进程来执行外部指令，并通过input/output/error管道，获取子进程的执行的返回信息。