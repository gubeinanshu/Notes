1. 将“当前”作业放到后台“暂停”： ctrl + z
2. 观察当前后台作业状态： jobs  
    
    > -l 除了列出作业号之外同时列出PID  
    > -r：列出仅在后台运行（run）的作业  
    > -s：仅列出暂停的作业

3. 将后台作业拿到前台处理：fg

    > fg %jobnumber (%可有可无)

4. 让作业在后台运行：bg

    > ctrl+z让当前作业到后台去暂停，bg 作业号就可以在后台run

5. 管理后台作业：kill

    > 我们可以让一个已经在后台的作业继续执行，也可以让该作业使用fg拿到前台。如果直接删除该作业，或者让作业重启，需要给作业发送信号。

    > kill -signal %jobnumber  
    > 参数：  
    > -l 列出当前kill能够使用的信号。 signal：表示给后台的作业什么指示，用man 7 signal可知  
    > -1（数字）：重新读取一次参数的设置文件（类似reload）  
    > -2：表示与由键盘输入ctrl-c同样的动作  
    > -9：立刻强制删除一个作业  
    > -15：以正常方式终止一项作业。与-9不一样。