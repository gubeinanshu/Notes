
### AndroidManifest.xml 添加权限

sdcard 读写权限
```
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
```

### activity_main.xml

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context="zhu.intenthomework.MainActivity">


    <Button
        android:id="@+id/button1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:onClick="doClick"
        android:text="显示启动" />

    <Button
        android:id="@+id/button2"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:onClick="doClick"
        android:text="隐式启动浏览器" />

    <Button
        android:id="@+id/button3"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:onClick="doClick"
        android:text="打开拨号界面" />

    <Button
        android:id="@+id/button4"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:onClick="doClick"
        android:text="直接拨打指定号码" />

    <Button
        android:id="@+id/button5"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:onClick="doClick"
        android:text="打开发短信的界面" />

    <Button
        android:id="@+id/button6"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:onClick="doClick"
        android:text="打开发短信的界面(指定电话号码)" />

    <Button
        android:id="@+id/button7"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:onClick="doClick"
        android:text="播放指定路径音乐" />

    <Button
        android:id="@+id/button8"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:onClick="doClick"
        android:text="安装apk" />

    <Button
        android:id="@+id/button9"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:onClick="doClick"
        android:text="卸载apk" />
</LinearLayout>

```


### MainActivity 的内容

其中播放音乐的代码有问题

```
package zhu.intenthomework;

import android.content.Intent;
import android.net.Uri;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import java.io.File;

public class MainActivity extends AppCompatActivity {

    Intent intent;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


    }

    public void  doClick(View view){
        switch (view.getId()){
            case R.id.button1:
                intent = new Intent(MainActivity.this, Main2Activity.class);
                startActivity(intent);
                break;
            case R.id.button2:
                intent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.baidu.com"));
                startActivity(intent);
                break;
            case R.id.button3:
                intent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:10086"));
                startActivity(intent);
                break;
            case R.id.button4:
                intent = new Intent(Intent.ACTION_CALL, Uri.parse("tel:10086"));
                startActivity(intent);
                break;
            case R.id.button5:
                intent = new Intent(Intent.ACTION_VIEW);
                intent.setType("vnd.android-dir/mms-sms");
                intent.putExtra("sms_body","这里是短信内容"); //"sms_body"为固定内容
                startActivity(intent);
                break;
            case R.id.button6:
                intent = new Intent(Intent.ACTION_SENDTO);
                intent.setData(Uri.parse("smsto:18867803752"));
                intent.putExtra("sms_body","具体短信内容"); //"sms_body"为固定内容
                startActivity(intent);
                break;
            case R.id.button7:
                File audioFile = new File(Environment.getExternalStorageDirectory(), "test.mp3");
                Toast.makeText(this, audioFile.getAbsolutePath() +"  " +audioFile.exists()+"", Toast.LENGTH_SHORT).show();
                Uri uri = Uri.parse(audioFile.getAbsolutePath());

                //下面这句是直接调用默认 音乐播放器
                //intent = new Intent("android.intent.action.MUSIC_PLAYER");

                intent = new Intent(android.content.Intent.ACTION_VIEW);
                intent.setDataAndType(uri, "audio/*");
                startActivity(intent);
                break;
            case R.id.button8:

                Intent intent = new Intent(Intent.ACTION_VIEW);
                Uri data = Uri.fromFile(new File(Environment.getExternalStorageDirectory(), "com.example.cssdemo_1.apk"));    //路径不能写成："file:///storage/sdcard0/···"
                intent.setDataAndType(data,"application/vnd.android.package-archive");  //Type的字符串为固定内容
                startActivity(intent);
                break;
            case R.id.button9:
                intent = new Intent(Intent.ACTION_DELETE);
                Uri dataa = Uri.parse("package:zhu.fastmenutest");
                intent.setData(dataa);
                startActivity(intent);
                break;

        }
    }
}

```
