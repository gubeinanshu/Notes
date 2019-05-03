
### 配置文件

AndroidManifest.xml

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="zhu.receivetest">

    <!--异步广播 (粘滞性滞留广播) ps:已被弃用,需要加入下面的权限-->
    <uses-permission android:name="android.permission.BROADCAST_STICKY" />

    <application android:allowBackup="true" android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name" android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true" android:theme="@style/AppTheme">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <!--静态注册，全局有效-->
        <receiver android:name=".MyBroadcastReceiver">
            <intent-filter android:priority="100">
                <action android:name="BC_One"/>
            </intent-filter>

        </receiver>
        <!--有序广播 priority 属性值越大，优先级越高-->

        <!--<receiver android:name=".MyBroadcastReceiver2">
            <intent-filter android:priority="200">
                <action android:name="BC_One"/>
            </intent-filter>
        </receiver>-->

    </application>

</manifest>
```

### 布局文件

activity_main.xml

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context="zhu.receivetest.MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:onClick="doClick"
        android:text="发送一条广播消息"
        tools:layout_editor_absoluteX="68dp"
        tools:layout_editor_absoluteY="30dp" />

    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:onClick="doClick"
        android:text="发送一条有序广播"
        tools:layout_editor_absoluteX="68dp"
        tools:layout_editor_absoluteY="95dp" />
    <Button
        android:id="@+id/button3"
        android:onClick="doClick"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="发送一条异步广播"
        tools:layout_editor_absoluteX="68dp"
        tools:layout_editor_absoluteY="95dp" />

</LinearLayout>

```

### MyBroadcastReceiver

新建 MyBroadcastReceiver.java 继承 BroadcastReceiver 类

```
package zhu.receivetest;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

/**
 * Created by zhu on 2017/5/1.
 */

public class MyBroadcastReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        String s = intent.getStringExtra("msg");
        Toast.makeText(context, "1111111收到 BC_One 发来的消息"+s, Toast.LENGTH_SHORT).show();

    }
}

```

### MyBroadcastReceiver2

新建 MyBroadcastReceiver2.java 继承 BroadcastReceiver 类

```
package zhu.receivetest;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

/**
 * Created by zhu on 2017/5/1.
 */

public class MyBroadcastReceiver2 extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        String s = intent.getStringExtra("msg");
        Toast.makeText(context, "222222收到 BC_One 发来的消息"+s, Toast.LENGTH_SHORT).show();

        //截断广播 有序广播时
        //abortBroadcast();

    }
}

```

### MyBroadcastReceiver3

新建 MyBroadcastReceiver3.java 继承 BroadcastReceiver 类

```
package zhu.receivetest;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

/**
 * Created by zhu on 2017/5/1.
 */

public class MyBroadcastReceiver3 extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        String s = intent.getStringExtra("msg");
        Toast.makeText(context, "3333333收到 BC_Three 的异步广播"+s, Toast.LENGTH_SHORT).show();

        //截断广播
        //abortBroadcast();

    }
}

```

### MainActivity

```
package zhu.receivetest;

import android.content.Intent;
import android.content.IntentFilter;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //动态注册优先级高于静态注册，但是作用域只在 程序运行期间
        //动态注册 MyBroadcastReceiver2
        IntentFilter intentFilter = new IntentFilter("BC_One");
        MyBroadcastReceiver2 myBroadcastReceiver2 = new MyBroadcastReceiver2();
        registerReceiver(myBroadcastReceiver2, intentFilter);

    }

    public void doClick (View view){
        switch (view.getId()){
            case R.id.button:
                Intent intent = new Intent();
                intent.putExtra("msg","这是一条普通广播");
                intent.setAction("BC_One");
                sendBroadcast(intent);
                break;
            case R.id.button2:
                Intent intent2 = new Intent();
                intent2.putExtra("msg","这是一条有序广播");
                intent2.setAction("BC_One");
                sendBroadcast(intent2, null);
                break;
            case R.id.button3:
                Intent intent3 = new Intent();
                intent3.putExtra("msg","这是一条异步广播");
                intent3.setAction("BC_Three");
                sendBroadcast(intent3, null);
                //动态注册 MyBroadcastReceiver3
                IntentFilter intentFilter = new IntentFilter("BC_Three");
                MyBroadcastReceiver3 myBroadcastReceiver3 = new MyBroadcastReceiver3();
                registerReceiver(myBroadcastReceiver3, intentFilter);

                break;
        }
    }
}

```
