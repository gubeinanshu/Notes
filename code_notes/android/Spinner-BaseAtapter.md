
### activity_main.xml

```
<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context="com.example.spinner3.MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="使用自定义BaseAdapter"
        android:textSize="24sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintHorizontal_bias="0.171"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.078" />
    <Spinner
        android:id="@+id/spinner"
        android:layout_width="186dp"
        android:layout_height="46dp"
        android:layout_marginBottom="8dp"
        android:layout_marginLeft="8dp"
        android:layout_marginRight="8dp"
        android:layout_marginTop="8dp"
        android:spinnerMode="dialog"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintHorizontal_bias="0.221"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.197"></Spinner>
</android.support.constraint.ConstraintLayout>

```

### 新建 item_custom

新建布局文件item_custom.xml

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal"
    android:weightSum="1">

    <ImageView
        android:id="@+id/image"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:srcCompat="@mipmap/ic_launcher" />

    <TextView
        android:id="@+id/textView1"
        android:layout_width="73dp"
        android:layout_height="42dp"
        android:text="TextView"
        android:layout_weight="0.10" />

    <TextView
        android:id="@+id/textView2"
        android:layout_width="wrap_content"
        android:layout_height="43dp"
        android:text="TextView"
        android:layout_weight="0.12" />

</LinearLayout>

```

### 新建 model 类 Person

```
package com.example.spinner3;

/**
 * Created by zhu on 2017/3/17.
 */

public class Person {
    private String personName;
    private String personAddress;

    public Person(String personName, String personAddress) {
        super();
        this.personName = personName;
        this.personAddress = personAddress;
    }
    public String getPersonName() {
        return personName;
    }
    public void setPersonName(String personName) {
        this.personName = personName;
    }
    public String getPersonAddress() {
        return personAddress;
    }
    public void setPersonAddress(String personAddress) {
        this.personAddress = personAddress;
    }

}

```

### MyAdapter

新建 MyAdapter 继承 BaseAdapter

```
package com.example.spinner3;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.List;


public class MyAdapter extends BaseAdapter {

    private List<Person> mList;
    private Context mContext;

    public MyAdapter(Context pContext, List<Person> pList) {
        this.mContext = pContext;
        this.mList = pList;
    }
    //返回总数量
    @Override
    public int getCount() {

        return mList.size();
    }
    //获取项目
    @Override
    public Object getItem(int position) {
        return mList.get(position);
    }
    //获取位置
    @Override
    public long getItemId(int position) {
        return position;
    }
    /**
     * 下面是重要代码
     */
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        LayoutInflater _LayoutInflater = LayoutInflater.from(mContext);
        //加载item布局文件
        convertView = _LayoutInflater.inflate(R.layout.item_custom, null);
        if(convertView!=null) {
            ImageView imageView = (ImageView)convertView.findViewById(R.id.image);
            imageView.setImageResource(R.mipmap.ic_launcher);
            TextView _TextView1 = (TextView)convertView.findViewById(R.id.textView1);
            TextView _TextView2 = (TextView)convertView.findViewById(R.id.textView2);
            _TextView1.setText(mList.get(position).getPersonName());
            _TextView2.setText(mList.get(position).getPersonAddress());
        }
        return convertView;
    }
}

```


### MainActivity

```
package com.example.spinner3;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.Spinner;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    //此处使用了ButterKnife Zelezny插件
    @butterknife.Bind(R.id.spinner)
    Spinner spinner;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        butterknife.ButterKnife.bind(this);

        // 初始化控件
        // 建立数据源
        List<Person> persons = new ArrayList<Person>();
        persons.add(new Person("张三", "上海 "));
        persons.add(new Person("李四", "上海 "));
        persons.add(new Person("王五", "北京"));
        persons.add(new Person("赵六", "广州 "));
        //  建立Adapter绑定数据源
        MyAdapter myAdapter = new MyAdapter(this, persons);
        //绑定Adapter
        spinner.setAdapter(myAdapter);
    }
}

```
