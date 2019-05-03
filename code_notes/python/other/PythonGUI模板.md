
```
	#!/usr/bin/env python
	# _*_  coding:utf-8 _*_
	
	import Tkinter
	root = Tkinter.Tk()
	#组件代码
	root.mainloop()
```
	
	组件有：
## Button  按钮

```
	    button = Tkinter.Button(root,   #父窗口
	        anchor = ,     #指定按钮上文本的位置(Tkinter.E)
	        background = , #指定按钮的背景色
	        bitmap = ,     #指定按钮上显示的位图
	        borderwidth = ,#指定按钮边框的宽度
	        command = ,    #指定按钮消息的的回调函数
	        cursor = ,     #指定鼠标移动到按钮上的指针样式
	        font = ,       #指定按钮上文本的字体
	        foreground = , #指定按钮的前景色
	        height = ,     #指定按钮的高度
	        image = ,      #指定按钮上显示的图片
	        state = ,      #指定按钮的状态
	        text = ,       #指定按钮上显示的文本
	        width = ,      #指定按钮的宽度
	        )
	    button.pack()

```

## Canvas  回执图形组件

可以在其中绘制图形

```
	    canvas = Tkinter.Canvas(root,
	        background = ,  #指定绘图组件的背景色
	        borderwidth = , #指定绘图组件的边框宽度
	        bitmap = ,      #指定绘图组件的的位图
	        foreground = ,  #指定绘图组件的前景色
	        height = ,      #指定绘图组件的高度
	        image = ,       #指定绘图组件的图片
	        width = ,       #指定绘图组件的宽度
	        )
	    canvas.create_arc       #绘制圆弧
	    canvas.create_bitmap    #绘制位图，支持XBM
	    canvas.create_image     #绘制图片，支持GIF
	    canvas.create_line      #绘制直线
	    canvas.create_oval      #绘制椭圆
	    canvas.create_polygon   #绘制多边形
	    canvas.create_rectangle #绘制矩形
	    canvas.create_text      #绘制文字
	    canvas.create_window    #绘制窗口
	    canvas.delete           #删除绘制的图形

```
	    例子：

```
	        #!/usr/bin/env python
	        # _*_  coding:utf-8 _*_
	
	        import Tkinter
	        root = Tkinter.Tk()
	
	        canvas = Tkinter.Canvas(root,
	            width = 600,
	            height = 480,
	            bg = 'white')
	
	        #im = Tkinter.PhotoImage(file='python.gif')
	        #canvas.create_image(300,50,image = im)
	        canvas.create_text(302,77,
	            text = 'Use Canvas',
	            fill = 'gray')
	        canvas.create_text(300,75,
	            text = 'Use Canvas',
	            fill = 'blue')
	        canvas.create_polygon(290,114,316,114,330,130,
	            310,146,284,146,270,130)
	        canvas.create_oval(290,120,320,140,fill = 'white')
	        canvas.create_line(250,130,350,130)
	        canvas.create_line(300,100,300,160)
	        canvas.create_rectangle(90,190,510,410,width=5)
	        canvas.create_arc(100,200,500,400,start=0,
	            extent=240,fill="pink")
	        canvas.create_arc(103,203,500,400,start=241,
	            extent=118,fill="red")
	        canvas.pack()
	        root.mainloop()

```
	
## Entry   文本框（单行）

```
	    entry = Tkinter.Entry(root,
	        background = , #指定文本框的背景色
	        borderwidth = ,#指定文本框边框的宽度
	        font = ,       #指定文本框中文字的字体
	        foreground = , #指定文本框的前景色
	        selectbackground = ,#指定选定文本的背景色
	        selectforeground = ,#指定选定文本的前景色
	        show = ,            #指定文本框中显示的字符，若为×，表示该为密码框
	        state = ,           #指定文本框的状态
	        width = ,           #指定文本框的宽度
	        )
	    entry.pack()

```

## Frame 框架(将几个组件组成一组)
## Label 标签(可显示文字或者图片)

```
	    label = Tkinter.Label(boot,
	        anchor = ,      #指定标签中文本的位置
	        background = ,  #指定标签的背景色
	        borderwidth = , #指定标签的边框宽度
	        bitmap = ,      #指定标签中的位图
	        font = ,        #指定标签中文本的字体
	        foreground = ,  #指定标签的前景色
	        height = ,      #指定标签的高度
	        image = ,       #指定标签中的图片
	        justify = ,     #指定标签中多行文本的对齐方式
	        text = ,        #指定标签中的文本，可以使用\n表示换行
	        width = ,       #指定标签中的高度
	        )
	    label.pack()

```

## Listbox 列表框
## Menu    菜单
	    普通菜单：

```
	        #!/usr/bin/env python
	        # _*_  coding:utf-8 _*_
	
	        import Tkinter
	        root = Tkinter.Tk()
	        menu = Tkinter.Menu(root)#生成菜单
	
	        submenu = Tkinter.Menu(menu, tearoff=0)#生成下拉菜单
	        submenu.add_command(label="Open")#向下拉菜单中添加Open命令
	        submenu.add_separator()#向下拉菜单中添加分隔符
	        submenu.add_command(label="Save")
	
	        menu.add_cascade(label="File",menu=submenu)#将下拉菜单添加到菜单中
	
	
	        root.config(menu=menu)
	        root.mainloop()

```
	    弹出式菜单：

```
	        #!/usr/bin/env python
	        # _*_  coding:utf-8 _*_
	
	        import Tkinter
	        root = Tkinter.Tk()
	        menu = Tkinter.Menu(root,tearoff=0)#创建菜单
	
	        menu.add_command(label="Copy")#向下拉菜单中添加Open命令
	        menu.add_separator()#向下拉菜单中添加分隔符
	        menu.add_command(label="Paste")
	
	        def popupmenu(event):#定义右键事件处理函数
	            menu.post(event.x_root,event.y_root)#显示菜单
	
	        root.bind("<Button-3>", popupmenu)#在主窗口中绑定右键事件
	        root.mainloop()

```

## Munubutton

该功能完全可以用Menu替代

## Message 与Label组件类似

但是可以根据自身大小将文本换行

## Radiobutton 单选框与下面
## Checkbutton 复选框共有

```
	    check = Tknter.Checkbutton()
	    check.pack(),
	    radio = Tkinter.Radiobutton(root,
	        anchor = ,      #指定文本位置
	        background = ,  #指定背景色
	        borderwidth = , #指定边框的宽度
	        bitmap = ,      #指定组件中的位图
	        font = ,        #指定组件中文本的字体
	        foreground = ,  #指定组件的前景色
	        height = ,      #指定组件的高度
	        image = ,       #指定组件中的图片
	        justify = ,     #指定组件中多行文本的对齐方式
	        text = ,        #指定组件中的文本，可以使用\n便是换行
	        value = ,       #指定组件被选中后关联变量的值
	        variable = ,    #指定组件所关联的变量
	        width = ,       #指定组件的宽度
	        )
	    radio.pack(),

```
	    代码示例：

```
	        #!/usr/bin/env python
	        # _*_  coding:utf-8 _*_
	
	        import Tkinter
	        root = Tkinter.Tk()
	
	        r = Tkinter.StringVar() #使用StringVar生成字符串变量，用于单选框组件
	        r.set('1')              #初始化变量值
	        radio = Tkinter.Radiobutton(root,#生成单选框组件
	            indicatoron = 0,###为0，将单选框绘制成按钮样式
	            variable = r,#设置单选框关联的变量
	            value = '1',#设置选中单选框是其所关联的变量的值，即r的值
	            text = 'Radio1')#设置单选框显示的文本
	        radio.pack()
	
	        c = Tkinter.IntVar()#使用IntVar生成整型变量，用于复选框
	        c.set(1)#
	        check = Tkinter.Checkbutton(root,
	            indicatoron = 0,###为0，将复选框绘制成按钮样式
	            text = 'Checkbutton',#设置复选框文本
	            variable = c,#设置复选框关联的变量
	            onvalue = 1,#当选中复选框时，c的值为1
	            offvalue = 2)#当未选中复选框时，c的值为2
	        check.pack()
	        root.mainloop()
	        print(r.get())
	        print(c.get())

```

## Scale   滑块
## Scrollbar   滚动条
## Text    文本框（多行）
## Toplecel   创建子窗口容器组件
	
	
## 组件布局：
	pack方法：
	    after   将组件置于其他组件之后
	    anchor  对齐方式，定对齐n，底对齐s，左对齐w，右对齐e
	    before  将组件置于其他组件之前
	    side    组件在主窗口的位置，可以为top，bottom，left，right
	
	grid方法：
	    column      组件所在的列起始位置
	    columnspam  组件的列宽
	    row         组件所在的行起始位置
	    rowspam     组件的行宽
	
	place方法
	    anchor      组件对齐方式
	    x           组件左上角的X坐标
	    y           组件左上角的Y坐标
	    relx        组件相对于窗口的X坐标，0-1
	    rely        组件相对于窗口的Y坐标，0-1
	    width       组件的宽度
	    height      组件的高度
	    relwidth    组件相对于窗口的宽度，0-1
	    relheight   组件相对于窗口的高度，0-1
	
## 事件处理：
	    绑定：
	    bind(sequence,func,add)
	    bind_class(className,sequence,func,add)
	    bind_all(sequence,func,add)
	    说明：
	        sequence    #所绑定的事件
	        func        #所绑定的事件处理函数
	        add         #可选参数，为空字符串或者’+‘
	        className   #所绑定的类
	
	    sequence表示所绑定的事件：1,2,3表示鼠标左中右
	        <Button-1>          #鼠标左键
	        <ButtonPress-1>     #鼠标左键按下与<Button-1>相同
	        <ButtonRelease-1>   #鼠标左键释放
	        <B1-Motion>         #按住鼠标左键移动
	        <Double-Button-1>   #双击鼠标左键
	        <Enter>             #鼠标指针进入某一组件区域
	        <Leave>             #鼠标指针离开某一组件区域
	        <MouseWheel>        #鼠标滚轮动作
	
### 键盘事件：
	        <KeyPress-A>            #表示按下A键，可用其他字母键代替
	        <Alt-KeyPress-A>        #表示同时按下Alt和A键
	        <Control-Key-Press-A>   #表示同时按下Control和A键
	        <Shift-KeyPress-A>      #表示同时按下Shift和A键
	        <Double-KeyPress-A>     #表示快速地按两下A键
	        <Lock-KeyPress-A>       #表示Caps Lock打开后按下A键
	        <Alt-Control-Shift-KeyPress-B>#表示同时按下Alt,Control,Shirft和B键
	
### 窗口事件：
	        Activate    #当组件大小改变时触发
	        Configure   #当组件由可用转为不可用时触发
	        Deactivate  #当组件被销毁时触发
	        Destroy     #当组件被销毁时触发
	        Expose      #当组件从被遮挡状态中暴露出来时触发
	        Focusln     #当组件获得焦点时触发
	        FocusOut    #当组件失去焦点时触发
	        Map         #当组件由隐藏状态变为显示状态时触发
	        Property    #当窗体的属性被删除或改变时触发
	        Unmap       #当组件由显示状态变为隐藏状态时触发
	        Visibility  #当组件变为可视状态时触发
### 响应事件：event
	    def function(event):
	        pass
	    char    #按键字符，仅对键盘事件有效
	    keycode #按键名，，仅对键盘事件有效
	    keysym  #按键编码，，仅对键盘事件有效
	    num     #鼠标按键，，仅对鼠标事件有效
	    type    #所触发的事件类型
	    widget  #引起事件的组件
	    x,y     #鼠标的当前位置，相对于窗口
	    x_root,y_root#鼠标当前位置，相对于整个屏幕
	    

## 示例代码

```
	#!/usr/bin/env python
	# _*_  coding:utf-8 _*_
	
	import tkinter
	root = tkinter.Tk()
	
	canvas = tkinter.Canvas(root,
		width = 600,
		height = 480,
		bg = 'white')
	
	#im = tkinter.PhotoImage(file='python.gif')
	#canvas.create_image(300,50,image = im)
	canvas.create_text(302,77,
		text = 'Use Canvas',
		fill = 'gray')
	canvas.create_text(300,75,
		text = 'Use Canvas',
		fill = 'blue')
	canvas.create_polygon(290,114,316,114,330,130,
		310,146,284,146,270,130)
	canvas.create_oval(290,120,320,140,fill = 'white')
	canvas.create_line(250,130,350,130)
	canvas.create_line(300,100,300,160)
	canvas.create_rectangle(90,190,510,410,width=5)
	canvas.create_arc(100,200,500,400,start=0,
		extent=240,fill="pink")
	canvas.create_arc(103,203,500,400,start=241,
		extent=118,fill="red")
	canvas.pack()
	root.mainloop()

```
