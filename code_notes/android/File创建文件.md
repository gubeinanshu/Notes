
### 创建文件示例

MainActivity
```

package zhu.filetest;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import java.io.File;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        /*File file = new File("/mnt/sdcard/test");
		if (!file.exists()) {
			try {
				file.createNewFile();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}else {
			Toast.makeText(MainActivity.this, "文件已经存在", 1000);
		}
		file.delete();*/

        //File file = this.getFilesDir();//这个目录是当前应用程序默认的数据存储目录
        //Log.i("info", file.toString());


		//File file = this.getCacheDir();
		//这个目录是当前应用程序默认的缓存文件的存放位置
		//把一些不是非常重要的文件在此处创建 使用
		//如果手机的内存不足的时候 系统会自动去删除APP的cache目录的数据
		//Log.i("info", file.toString());


		//data/data/<包名>/app_imooc
		//File file = this.getDir("imooc", MODE_PRIVATE);
		//Log.i("info", file.toString());

        //外部存储目录
		//this.getExternalFilesDir(type);
        //可以得到外部的存储位置 该位置的数据跟内置的使用是一样的
        //如果APP卸载了 这里面的数据也会自动清除掉
        File file = this.getExternalCacheDir();
        Log.i("info", file.toString());
        //如果说开发者不遵守这样的规则 不把数据放入 data/data/<包名> 或者
		//	/mnt/sdcard/Android/data/<包名>
		//卸载之后数据将不会自动清除掉 将会造成所谓的数据垃圾
    }
}


```

### 文件读写案例

MainActivity
```
package zhu.filetest;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

import android.os.Bundle;

import android.support.v7.app.AppCompatActivity;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
	EditText edt;
	Button but;
	TextView contentvalue;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);

		edt = (EditText) findViewById(R.id.editText1);
		but = (Button) findViewById(R.id.write);
		contentvalue = (TextView) findViewById(R.id.contentvalue);

		but.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				WriteFiles(edt.getText().toString());
				contentvalue.setText(readFiles());

			}
		});
	}

	//保存文件内容
	public void WriteFiles(String content){
		 try {
			FileOutputStream fos = openFileOutput("a.txt", MODE_WORLD_READABLE+MODE_WORLD_WRITEABLE);
			 fos.write(content.getBytes());
			 fos.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
	//读取文件内容
	public String readFiles(){
		String content = null;
		 try {
			FileInputStream fis= openFileInput("a.txt");
			 ByteArrayOutputStream baos =  new ByteArrayOutputStream();
			byte [] buffer =  new byte[1024];
			int len = 0;
			while ((len=fis.read(buffer))!=-1) {
				baos.write(buffer, 0, len);
			}
			content = baos.toString();
			fis.close();
			baos.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		return content;
	}
}

```
### activity_main.xml

文件读写案例
```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"

    android:orientation="vertical"
    tools:context=".MainActivity">

    <EditText
        android:id="@+id/editText1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_alignParentRight="true"
        android:layout_alignParentTop="true"
        android:ems="10">

        <requestFocus />
    </EditText>

    <TextView
        android:id="@+id/contentvalue"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/editText1"
        android:layout_below="@+id/write"
        android:text="TextView" />

    <Button
        android:id="@+id/write"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerHorizontal="true"
        android:layout_centerVertical="true"
        android:text="写入并读取出来" />

</LinearLayout>


```
