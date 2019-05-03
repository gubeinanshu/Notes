
### MainActivity

```
package zhu.httptest;

import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebView;


public class MainActivity extends AppCompatActivity {

    private WebView webView;
    private Handler handler = new Handler();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        webView = (WebView) findViewById(R.id.webView);
        //webView.loadUrl("http://www.baidu.com/");
        new HttpThread("http://www.imooc.com/course/programdetail/pid/33", webView, handler).start();
    }
}

```

### HttpThread

```
package zhu.httptest;

import android.os.Handler;
import android.util.Log;
import android.webkit.WebView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import javax.net.ssl.HttpsURLConnection;

/**
 * Created by zhu on 2017/5/8.
 */

public class HttpThread extends Thread {

    private String uri;
    private WebView webView;
    private Handler handler;

    public HttpThread(String uri, WebView webView, Handler handler){
        this.uri = uri;
        this.webView = webView;
        this.handler = handler;

    }
    @Override
    public void run() {
        try {
            //获取连接，设置请求方式和超时时间
            URL httpUrl = new URL(uri);
            HttpURLConnection conn = (HttpURLConnection) httpUrl.openConnection();
            conn.setConnectTimeout(5000);
            conn.setRequestMethod("GET");
            final StringBuffer sb = new StringBuffer();
            BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String str;
            while ((str=reader.readLine())!=null){
                sb.append(str);
            }
            //Log.i("tag", str+"b");
            //使用 handler 更新 webView
            handler.post(new Runnable() {
                @Override
                public void run() {
                    //Log.i("tag", sb.toString()+"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
                    webView.loadData(sb.toString(),"text/html;charset=utf-8",null);
                }
            });

        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}

```

### activity_main.xml

```
<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
    android:layout_height="match_parent" tools:context="zhu.httptest.MainActivity">

    <WebView
        android:id="@+id/webView"
        android:layout_width="match_parent"
        android:layout_height="match_parent">
        s
    </WebView>

</android.support.constraint.ConstraintLayout>

```
