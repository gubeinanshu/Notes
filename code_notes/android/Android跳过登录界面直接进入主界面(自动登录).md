
参考： [Android程序跳过登录界面直接进入主界面(自动登录)](http://blog.csdn.net/eyckwu/article/details/53024106)

实现自动登录: 采用SharedPreferences来保存登录状态, 是当程序从欢迎界面跳转到登录界面是，在登录界面还没有加载布局文件时判断是否登陆过，从而实现直接跳转到主界面。
*欢迎界面代码*
```
public class WelcomeActivity extends Activity{
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.welcome);
        /**
         * 延迟3秒进入主界面
         */
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent intent=new Intent(WelcomeActivity.this,LoginActivity.class);
                startActivity(intent);
                WelcomeActivity.this.finish();
            }
        },1000*3);
    }
}
```

















