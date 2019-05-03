
获取 SharedPreferences 的两种方式:

1、 getSharedPreferences()
调用 Context 对象的 getSharedPreferences() 方法获得的 SharedPreferences 对象可以被同一应用程序下的其他组件共享.
2、 getPreferences()
调用 Activity 对象的 getPreferences() 方法获得的 SharedPreferences 对象只能在该 Activity 中使用.

SharedPreferences 的四种操作模式:
* Context.MODE_PRIVATE： 默认操作模式, 代表私有数据, 只能被应用本身访问, 写入的数据时会覆盖原文件
* Context.MODE_APPEND： 文件存在就追加内容, 否则就创建新文件.
* MODE_WORLD_READABLE： 表示数据文件可以被其他应用读取.
* MODE_WORLD_WRITEABLE： 表示数据文件可以被其他应用写入.
<!--more-->

保存数据
SharedPreferences preferences=getSharedPreferences("test",Context.MODE_APPEND);
Editor editor=preferences.edit();
editor.putString("test", test);
editor.commit();





