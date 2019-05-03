
android 中在 bindServer 的时候，可以回调 onServiceConnected 函数，在 bindServer 后马上调用 server ，但此时不保证 onServiceConnected 已经被回调，也就是会返回 null。因为 bindServer 是异步操作，不能马上绑定服务就使用。
