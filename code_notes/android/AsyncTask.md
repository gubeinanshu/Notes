
这次先 java 代码，再 xml 文件

### MyAsyncTask

```
package com.example.zhu.mooc1;

import android.os.AsyncTask;

/**
 * AsyncTask<Params, Progress, Result >
 * Params : 启动任务时输入参数的类型
 * Progress : 后台任务执行返回进度值的类型
 * Result : 后台执行任务完成后返回结果的类型
 */

public class MyAsyncTask extends AsyncTask<Void,Void,Void > {

    //初始化操作
    @Override
    protected void onPreExecute() {
        super.onPreExecute();
    }
    //执行结束后的操作
    @Override
    protected void onPostExecute(Void aVoid) {
        super.onPostExecute(aVoid);
    }
    //进行主要的操作的函数
    //可以通过 publishProgress() 调用onProgressUpdate
    @Override
    protected Void doInBackground(Void... params) {
        return null;
    }
    //
    @Override
    protected void onProgressUpdate(Void... values) {
        super.onProgressUpdate(values);
    }
}

```

### MainActivity

```
package com.example.zhu.mooc1;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


    }
    public void loadImage(View view){
        startActivity(new Intent(this,ImageTest.class));
    }
    public void loadP(View view){
        startActivity(new Intent(this,ProgressBarTest.class));
    }
}

```

### ImageTest

```
package com.example.zhu.mooc1;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.ProgressBar;

import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URLConnection;
import java.net.URL;

public class ImageTest extends AppCompatActivity {


    private ImageView imageView;
    private ProgressBar progressBar;
    private  static String url =
                    "http://img.mukewang.com/58341930000163b106000338-240-180.jpg";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_image_test);

        imageView= (ImageView) findViewById(R.id.image);
        progressBar= (ProgressBar) findViewById(R.id.progresbar);
        new MyAsyncTask().execute(url);





    }

    class MyAsyncTask extends AsyncTask<String,Void,Bitmap>{

        @Override
        protected void onPreExecute() {
            super.onPreExecute();
            progressBar.setVisibility(View.VISIBLE);
        }


        @Override
        protected void onPostExecute(Bitmap bitmap) {
            super.onPostExecute(bitmap);
            progressBar.setVisibility(View.GONE);
            imageView.setImageBitmap(bitmap);
        }

        @Override
        protected Bitmap doInBackground(String... params) {
            String url = params[0];
            Bitmap bitmap = null;
            URLConnection connection;
            InputStream is;
            try {
                connection = new URL(url).openConnection();
                is = connection.getInputStream();
                BufferedInputStream bis = new BufferedInputStream(is);
                Thread.sleep(1000);
                bitmap = BitmapFactory.decodeStream(bis);
                is.close();
                bis.close();
            } catch (IOException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            return bitmap;
        }
    }
}

```

### ProgressBarTest

```
package com.example.zhu.mooc1;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ProgressBar;

public class ProgressBarTest extends AppCompatActivity {

    private ProgressBar progressBar;
    private MyAsyncTask task;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_progress_bar_test);

        progressBar = (ProgressBar) findViewById(R.id.progressBar);
        task = new MyAsyncTask();
        task.execute();
    }

    @Override
    protected void onPause() {
        super.onPause();
        if(task!=null && task.getStatus() == AsyncTask.Status.RUNNING){
            //关闭该线程
            task.cancel(true);
        }
    }



    class MyAsyncTask extends AsyncTask<Void,Integer,Void>{
        @Override
        protected Void doInBackground(Void... params) {
            for(int i=1;i<=100;i++){
                //检查该线程是否被关闭
                if(isCancelled()){
                    break;
                }
                publishProgress(i);
                try {
                    Thread.sleep(300);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            return null;
        }

        @Override
        protected void onProgressUpdate(Integer... values) {
            super.onProgressUpdate(values);
            //System.out.println("================="+values[0]);
            if(isCancelled()){
                return;
            }
            progressBar.setProgress(Integer.valueOf(values[0]));
        }
    }

}

```

### activity_main.xml

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/activity_main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"

    tools:context="com.example.zhu.mooc1.MainActivity"
    android:orientation="vertical">


    <Button

        android:text="Button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:onClick="loadImage"
        android:layout_marginTop="34dp"
        android:layout_alignParentTop="true"
        android:layout_alignParentRight="true"
        android:layout_alignParentEnd="true"
        android:layout_marginRight="100dp"
        android:layout_marginEnd="100dp" />

    <Button

        android:text="Button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:onClick="loadP"
        android:layout_marginLeft="10dp"
        android:layout_marginStart="10dp"
        android:layout_centerVertical="true"
        android:layout_alignLeft="@+id/button"
        android:layout_alignStart="@+id/button" />
</LinearLayout>

```

### image布局
文件名： activity_image_test.xml

```
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/activity_image_test"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:paddingBottom="@dimen/activity_vertical_margin"
    android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"
    tools:context="com.example.zhu.mooc1.ImageTest">


    <ImageView
        android:id="@+id/image"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
    <ProgressBar
        android:id="@+id/progresbar"
        android:visibility="gone"
        android:layout_centerInParent="true"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />
</RelativeLayout>

```

### progress_bar布局

文件名： activity_progress_bar_test.xml

```
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/activity_progress_bar_test"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context="com.example.zhu.mooc1.ProgressBarTest">

    <ProgressBar
        style="?android:attr/progressBarStyleHorizontal"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/progressBar"
        android:layout_alignParentTop="true"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="233dp" />

</RelativeLayout>

```
