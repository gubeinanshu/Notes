
### 配置文件

AndroidManifest.xml

````
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="zhu.servertest">

    <application android:allowBackup="true" android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name" android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true" android:theme="@style/AppTheme">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <!--注册 service-->
        <service android:name=".MyStartService"></service>
        <service android:name=".MyBindService"></service>
    </application>

</manifest>
````

### 布局文件

activity_main.xml

````
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    tools:context="zhu.servertest.MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="start:"/>

    <Button
        android:id="@+id/start"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:onClick="doClick"
        android:text="StartService" />

    <Button
        android:id="@+id/stop"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:onClick="doClick"
        android:text="StopService" />
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="bind:"/>

    <Button
        android:id="@+id/bind"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:onClick="doClick"
        android:text="BindService" />

    <Button
        android:id="@+id/play"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:onClick="doClick"
        android:text="播放" />

    <Button
        android:id="@+id/pause"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:onClick="doClick"
        android:text="暂停" />

    <Button
        android:id="@+id/next"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:onClick="doClick"
        android:text="下一首" />

    <Button
        android:id="@+id/previous"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:onClick="doClick"
        android:text="上一首" />

    <Button
        android:id="@+id/unbind"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:onClick="doClick"
        android:text="UnBindService" />
</LinearLayout>

````

### MyStartService

新建 MyStartService 继承 Service 类

start方式
````
package zhu.servertest;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.support.annotation.IntDef;
import android.support.annotation.Nullable;
import android.util.Log;

/**
 * Created by zhu on 2017/5/2.
 */

public class MyStartService extends Service {

    @Override
    public void onCreate() {
        Log.i("info", "Service--onCreate");
        super.onCreate();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        Log.i("info", "Service--onStartCommand");
        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public void onDestroy() {
        Log.i("info", "Service--onDestroy");
        super.onDestroy();
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        Log.i("info", "Service--onBind");
        return null;
    }
}

````

### MyBindService

新建 MyBindService 继承 Service 类

bind方式
````
package zhu.servertest;

import android.app.Service;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Binder;
import android.os.IBinder;
import android.support.annotation.Nullable;
import android.util.Log;

/**
 * Created by zhu on 2017/5/2.
 */

public class MyBindService extends Service {
    @Override
    public void onCreate() {
        super.onCreate();
        Log.i("info", "BindService--onCreate");
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        Log.i("info", "BindService--onBind");
        //通过 Ibinder 接口实例，返回一个 ServiceConnection 对象给启动源
        return new MyBinder();
    }
    public class MyBinder extends Binder {
        public MyBindService getService(){
            return MyBindService.this;
        }
    }

    @Override
    public void unbindService(ServiceConnection conn) {
        super.unbindService(conn);
        Log.i("info", "BindService--unbindService");
    }

    @Override
    public void onDestroy() {
        Log.i("info", "BindService--onDestroy");
        super.onDestroy();
    }

    public void Play(){
        Log.i("info","播放");
    }
    public void Pause(){
        Log.i("info","暂停");
    }
    public void Pervious(){
        Log.i("info","上一首");
    }
    public void Next(){
        Log.i("info","下一首");
    }
}

````

### MainActivity

````
package zhu.servertest;

import android.app.Service;
import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.IBinder;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    Intent intent;
    Intent intent2;
    MyBindService service;
    //通过 ServiceConnection 对象的相关方法可以得到 Service 对象
    ServiceConnection conn = new ServiceConnection() {
        //当启动源跟 Service 成功连接之后将会自动调用这个方法
        @Override
        public void onServiceConnected(ComponentName name, IBinder binder) {
            service = ((MyBindService.MyBinder)binder).getService();
        }

        //当启动源跟 Service 的连接意外丢失的时候会调用
        @Override
        public void onServiceDisconnected(ComponentName name) {

        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void doClick(View view){
        switch (view.getId()){
            case R.id.start:
                intent = new Intent(MainActivity.this, MyStartService.class);
                startService(intent);
                break;
            case R.id.stop:
                stopService(intent);
                break;
            case R.id.bind:
                try {
                    intent2 = new Intent(MainActivity.this, MyBindService.class);
                    bindService(intent2, conn, Service.BIND_AUTO_CREATE);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                break;
            case R.id.play:
                service.Play();
                break;
            case R.id.pause:
                service.Pause();
                break;
            case R.id.next:
                service.Next();
                break;
            case R.id.previous:
                service.Pervious();
                break;
            case R.id.unbind:
                unbindService(conn);
                break;


        }
    }
}

````
