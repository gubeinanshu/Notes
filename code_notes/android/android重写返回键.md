
实现监听返回键，重写onKeyDown，默认还是会退回上一个 activity，例如双击返回的话有点不一样
```
@Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if(keyCode==KeyEvent.KEYCODE_BACK){
            //一些操作
        }
        return true;
    }
```
