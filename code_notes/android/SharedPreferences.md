
### activity_main.xml

```
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity" >

    <TextView
        android:id="@+id/textView1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_alignParentTop="true"
        android:layout_marginTop="16dp"
        android:text="用户名：" />

    <EditText
        android:id="@+id/etuserName"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentRight="true"
        android:layout_alignTop="@+id/textView1"
        android:layout_toRightOf="@+id/textView1"
        android:ems="10" />

    <TextView
        android:id="@+id/aa"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_below="@+id/etuserName"
        android:text="密		码" />

    <EditText
        android:id="@+id/etuserpass"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/etuserName"
        android:layout_alignParentRight="true"
        android:layout_alignTop="@+id/aa"
        android:ems="10" >

        <requestFocus />
    </EditText>

    <CheckBox
        android:id="@+id/chkSaveName"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:checked="false"
        android:layout_below="@+id/etuserpass"
        android:text="保存用户名" />

    <Button
        android:id="@+id/btnLogin"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignParentLeft="true"
        android:layout_below="@+id/chkSaveName"
        android:onClick="doClick"
        android:text="登陆" />

    <Button
        android:id="@+id/btnCancel"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_alignBaseline="@+id/btnLogin"
        android:layout_alignBottom="@+id/btnLogin"
        android:layout_toRightOf="@+id/btnLogin"
        android:onClick="doClick"
        android:text="取消" />

</RelativeLayout>

```

### MainActivity

```
package zhu.a20170502;

import android.content.SharedPreferences;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    EditText etUserName,etUserPass;
    CheckBox chk;
    SharedPreferences pref;
    SharedPreferences.Editor edtior;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
////		SharedPreferences pref = PreferenceManager.getDefaultSharedPreferences(MainActivity.this);
//		SharedPreferences pref =getSharedPreferences("myPref", MODE_PRIVATE);
//		Editor editor = pref.edit();
//		editor.putString("name","张三");
//		editor.putInt("age", 30);
//		editor.putLong("time", System.currentTimeMillis());
//		editor.putBoolean("default", true);
//		editor.commit();
//		editor.remove("default");
//		editor.commit();
//		System.out.println(pref.getString("name", ""));
//		System.out.println(pref.getInt("age", 0));


        etUserName = (EditText) findViewById(R.id.etuserName);
        etUserPass = (EditText) findViewById(R.id.etuserpass);
        chk = (CheckBox) findViewById(R.id.chkSaveName);

        //给出 命名 UserInfo，这里设定模式 MODE_PRIVATE
        pref =getSharedPreferences("UserInfo", MODE_PRIVATE);
        //获取edit
        edtior = pref.edit();
        //获取保存的用户名
        String name = pref.getString("userName", "");
        if (name==null) {
            //保存按钮置false
            chk.setChecked(false);
        }else {
            //保存按钮置true
            chk.setChecked(true);
            //设置用户名
            etUserName.setText(name);
        }
    }
    public void doClick(View v){
        switch (v.getId()) {
            case R.id.btnLogin:
                String name = etUserName.getText().toString().trim();
                String pass = etUserPass.getText().toString().trim();
                if ("admin".equals(name)&&"123456".equals(pass)) {
                    if (chk.isChecked()) {//选项框被选中
                        //以键值对的形式保存用户名
                        edtior.putString("userName", name);
                        edtior.commit();

                    }else {
                        edtior.remove("userName");
                        edtior.commit();
                    }
                    Toast.makeText(MainActivity.this, "登陆成功", Toast.LENGTH_LONG).show();
                }else {
                    Toast.makeText(MainActivity.this, "禁止登陆", Toast.LENGTH_LONG).show();
                }
                break;

            default:
                break;
        }
    }
}

```
