
还要多学习啊
参考： [android 中使控件显示后隐藏](https://zhidao.baidu.com/question/919208569055262739.html)

```
Handler handler = new Handler();

Runnable runnable = new Runnable() {
    @Override
    public void run() {  //10秒后执行该方法
        // handler自带方法实现定时器
        try {
            View view = (View)findViewById(R.id.xxx);//图片或者控件
            view.setVisible(View.Gone); //隐藏
            System.out.println("do...");
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            System.out.println("exception...");
        }
    }
};

handler.postDelayed(runnable, 10000); //10秒后执行 runnable 的 run 方法
```








