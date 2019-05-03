
参考自：[sendMessage 与 obtainMessage 区别 ](http://zuizui0122.blog.163.com/blog/static/18816618920137195294662/)
<!--more-->
sendMessage() 这个方法调用的是 Handler 中的 sendMessage(Message msg)


handler.obtainMessage() 源码见下：

 public final Message obtainMessage()
   {
       return Message.obtain(this);
   }



使用的时候尽量使用 Message msg = handler.obtainMessage(); 的形式创建 Message ，不要自己 New Message。(这里我们的 Message 已经不是自己创建的了，而是从 MessagePool 拿的，省去了创建对象申请内存的开销，因此无需重新申请，效率较高。)

Message.sendToTarget() 的本质也是调用 Handler 的 sendMessage 方法。

至于 message 产生之后你使用 sendToTarget 或者是 sendMessage 效率影响并不大。

下面给出几个方法供参考：

public final Message obtainMessage(int what, int arg1, int arg2, Object obj)
{
    return Message.obtain(this, what, arg1, arg2, obj);
}.sendToTarget();


public final boolean sendMessage(Message msg)
{
    return sendMessageDelayed(msg, 0);
}


public final boolean sendEmptyMessage(int what)
{
    return sendEmptyMessageDelayed(what, 0);
}
