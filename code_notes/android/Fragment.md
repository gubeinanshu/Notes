
### 布局文件

activity_main.xml

name 属性加载Fragment类
id 属性需要定义

```
<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
    android:layout_height="match_parent" tools:context="zhu.fragmenttest.MainActivity">

    <fragment
        android:id="@+id/fragmentA"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:name="zhu.fragmenttest.FragmentA"
        />

</android.support.constraint.ConstraintLayout>
```

### fragment_a.xml

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="button" />

</LinearLayout>
```

### FragmentA.java

新建 FragmentA.java 继承 Fragment

```
package zhu.fragmenttest;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

/**
 * Created by zhu on 2017/4/28.
 */

public class FragmentA extends Fragment {

    //此处使用了ButterKnife Zelezny插件
    @butterknife.Bind(R.id.textView)
    TextView textView;
    @butterknife.Bind(R.id.button)
    Button button;

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        /**
         * inflater.inflate(resource, root, attachToRoot)
         * resource: Fragment需要加载的布局文件
         * root: 加载layout的父ViewGroup
         * attachToRoot: false, 不返回父ViewGroup
         */
        View view = inflater.inflate(R.layout.fragment_a, container, false);
        butterknife.ButterKnife.bind(this, view);

        textView.setText("静态加载Fragment");

        return view;
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        butterknife.ButterKnife.unbind(this);
    }
}
```

### MainActivity

```
package zhu.fragmenttest;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
```



### Fragment 动态加载
响应事件

```
    public void doClick(View view){
        MyFragment2 myFragment2 = new MyFragment2();
        FragmentManager fragmentManager = getFragmentManager();
        //事物，可以添加，移除，替换
        FragmentTransaction beginTransaction = fragmentManager.beginTransaction();
        //第一个参数为父容器id，即要放到哪个组件里面
        beginTransaction.add(R.id.lin, myFragment2);
       // beginTransaction.replace(R.id.fragment, myFragment2);
       // beginTransaction.remove(myFragment2);
        beginTransaction.addToBackStack(null);
        beginTransaction.commit();
    }
```
