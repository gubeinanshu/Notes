
### 两种方式

两种方式： post/sendMessage

```
package zhu.a20170508;

import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private TextView textView;
    //Handler 可以被移除
    private Handler handler = new Handler();
    private Handler handler2 = new Handler(){
        @Override
        public void handleMessage(Message msg) {
            // textView.setText(msg.obj);
            textView.setText("bbbbbbbbbbbbbbb  "+msg.arg1+msg.arg2);
        }
    };

    private Handler handler3 = new Handler(new Handler.Callback() {
        //Callback 截获 Message 返回 false 则会传递下去，返回 true 则截断
        @Override
        public boolean handleMessage(Message msg) {

            return false;
        }
    }){
        @Override
        public void handleMessage(Message msg) {

        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textView = (TextView) findViewById(R.id.textView);
        //Message方式
        new Thread(){
            @Override
            public void run() {
                try {
                    Thread.sleep(2000);
                    Message message = new Message();
                    //或者用这个获取 Message 对象
                    //Message message = handler2.obtainMessage();
                    message.arg1=99999999;
                    message.arg2=88888888;
                    //message.obj=person; //对象
                    handler2.sendMessage(message);
                    //或者用这个发送 message
                    //message.sendToTarget();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }.start();

        //post方式
        new Thread(){
            @Override
            public void run() {
                try {
                    Thread.sleep(1000);
                    handler.post(new Runnable() {
                        @Override
                        public void run() {
                            textView.setText("aaaaaaaaaaaaaa");
                        }
                    });
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }.start();

    }
}

```

### 布局文件

```
<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context="zhu.a20170508.MainActivity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</android.support.constraint.ConstraintLayout>

```