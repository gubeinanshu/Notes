> powershell中如何在资源管理器中打开当前目录

```
# I
explorer (gl)
explorer .

# II
start .

# III
ii .
```

```
# 打开当前根目录
ii /
```

```
# 查看缩写别名
# 全部
gal
# 指定
gal ii =>
```

> win10文件被占用无法删除如何解决

任务管理器 -> 性能 -> 打开资源监视器 -> 右侧有个搜索栏，在其中输入被占用的文件的名称即可 -> 右键结束进程

> cmd初始化u盘

1. 输入"diskpart"，弹出一个新的对话框
2. 在新对话框中输入入"list disk" 命令，会出现两个磁盘，一个是自己电脑的内存大小，另一个就是U盘的内存大小
3. 输入“select disk 1”(这里的1是U盘)，选择磁盘1
4. 系统提示目前已选中磁盘1，输入“clean”。
5. 进入磁盘管理，选择可移动磁盘，新建简单卷

> 如何在Windows的cmd下让程序在后台执行

start /b，比如start /b run.bat。就相当于Linux下的run.sh &
