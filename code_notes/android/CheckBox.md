
### 布局文件

```
<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context="zhu.checkboxtest.MainActivity">

    <CheckBox
        android:id="@+id/checkBox"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:checked="true"
        android:text="男"
 />

</android.support.constraint.ConstraintLayout>

```

### MainActivity内容

```
package zhu.checkboxtest;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.CheckBox;
import android.widget.CompoundButton;

public class MainActivity extends AppCompatActivity {

    private CheckBox checkbox;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        checkbox = (CheckBox) findViewById(R.id.checkBox);

        //给checkbox设置监听是事件
        checkbox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {

            //不管选择或者取消，都会触发监听
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                //通过onCheckedChanged来监听当前的checkbox是否被选中
                if(isChecked){//选中
                    //获得checkbox的文本内容
                    String text = checkbox.getText().toString();
                    Log.i("tag",text);
                }
            }
        });

    }

}

```
