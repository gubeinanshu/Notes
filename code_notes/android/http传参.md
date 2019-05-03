
### MainActivity

```
package zhu.httptest;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Main2Activity extends AppCompatActivity {

    //此处使用了ButterKnife Zelezny插件
    @butterknife.Bind(R.id.editText)
    EditText editText;
    @butterknife.Bind(R.id.editText2)
    EditText editText2;
    @butterknife.Bind(R.id.button)
    Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        butterknife.ButterKnife.bind(this);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String url = "http://127.0.0.1/";//这里是请求地址
                new HttpThread2(url,editText.getText().toString(),editText.getText().toString()).start();
            }
        });
    }
}

```

### HttpThread2

```
package zhu.httptest;

import android.os.Handler;
import android.util.Log;
import android.webkit.WebView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * Created by zhu on 2017/5/8.
 */

public class HttpThread2 extends Thread {

    private String url;
    private String name;
    private String age;

    public HttpThread2(String url, String name, String age){
        this.url = url;
        this.name = name;
        this.age = age;

    }
    private void doGet(){
        url=url+"?name"+name+"&age"+age;
        try {
            URL httpUrl = new URL(url);
            HttpURLConnection conn = (HttpURLConnection) httpUrl.openConnection();
            conn.setRequestMethod("GET");
            conn.setReadTimeout(50000);
            BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String str;
            StringBuffer sb = new StringBuffer();
            while ((str=reader.readLine())!=null){
                sb.append(str);
            }
            Log.i("tag", sb.toString());
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void doPost(){
        try {
            URL httpUrl = new URL(url);

            HttpURLConnection conn = (HttpURLConnection) httpUrl.openConnection();
            conn.setRequestMethod("POST");
            conn.setReadTimeout(50000);
            OutputStream out = conn.getOutputStream();
            String content = "name="+name+"&age="+age;

            out.write(content.getBytes());
            BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            StringBuffer sb = new StringBuffer();
            String str;
            while ((str=reader.readLine())!=null){
                sb.append(str);
            }
            Log.i("tag", sb.toString());
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Override
    public void run() {
        //doGet();
        doPost();

    }
}

```

### activity_main.xml

```
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context="zhu.httptest.Main2Activity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="61dp"
        android:text="用户名"
        tools:layout_editor_absoluteX="46dp"
        tools:layout_editor_absoluteY="83dp" />

    <EditText
        android:id="@+id/editText"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:ems="10"
        android:inputType="textPersonName"
        android:layout_above="@+id/textView2"
        android:layout_centerHorizontal="true" />

    <TextView
        android:id="@+id/textView2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_alignParentStart="true"
        android:layout_below="@+id/textView"
        android:layout_marginTop="64dp"
        android:text="密码" />

    <EditText
        android:id="@+id/editText2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignBottom="@+id/textView2"
        android:layout_alignLeft="@+id/editText"
        android:layout_alignStart="@+id/editText"
        android:ems="10"
        android:inputType="textPassword" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/editText2"
        android:layout_alignStart="@+id/editText2"
        android:layout_centerVertical="true"
        android:text="regist" />
</RelativeLayout>

```

