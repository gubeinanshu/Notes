
将 Layout 布局转换为 View 对象
1. 
```
	LayoutInflater If = getLayoutInflater().from(this);
	If.inflate(resource, root);
```
2. 
```
	View.inflate(context, resource, root);
```

### view1

新建布局文件 view1.xml

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:text="第一个界面"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

</LinearLayout>

```

### 布局文件

activity_main.xml

```
<?xml version="1.0" encoding="utf-8"?>
<android.support.constraint.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
    android:layout_height="match_parent" tools:context="zhu.viewpagertest.MainActivity">

    <android.support.v4.view.ViewPager
        android:id="@+id/pager"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:foregroundGravity="center">


        <android.support.v4.view.PagerTabStrip
            android:id="@+id/tab"
            android:foregroundGravity="top"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content">


        </android.support.v4.view.PagerTabStrip>
    </android.support.v4.view.ViewPager>

</android.support.constraint.ConstraintLayout>


```

### MyPagerAdapter

新建 MyPagerAdapter.java 继承 PagerAdapter 类

```
package zhu.viewpagertest;

import android.support.v4.view.PagerAdapter;
import android.view.View;
import android.view.ViewGroup;

import java.util.List;

/**
 * Created by zhu on 2017/4/28.
 */

public class MyPagerAdapter extends PagerAdapter {

    private List<View> viewList;
    private List<String> titleList;

    public MyPagerAdapter(List<View> viewList, List<String> titleList){
        this.viewList = viewList;
        this.titleList = titleList;
    }

    /**
     * 返回页卡的数量
     */
    @Override
    public int getCount() {
        return viewList.size();
    }

    /**
     * View是否来自对象
     */
    @Override
    public boolean isViewFromObject(View view, Object object) {
        return view == object;
    }

    /**
     * 实例化一个页卡
     */
    @Override
    public Object instantiateItem(ViewGroup container, int position) {
        container.addView(viewList.get(position));
        return viewList.get(position);
    }

    /**
     * 销毁一个页卡
     */
    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        container.removeView(viewList.get(position));
    }

    /**
     * 设置 VirePager 页卡的标题
     */
    @Override
    public CharSequence getPageTitle(int position) {
        return titleList.get(position);
    }
}



```

### MainActivity

```
package zhu.viewpagertest;

import android.graphics.Color;
import android.support.v4.view.PagerTabStrip;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private List<View> viewList;
    private ViewPager viewPager;
    private PagerTabStrip tab;
    //标题
    private List<String> titleList;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        /**
         * 生成数据源,多建几个 view.xml 即可
         */
        viewList = new ArrayList<View>();
        View view1 = View.inflate(this, R.layout.view1, null);

        viewList.add(view1);

        //为 PagerTabStrip 设置一些属性
        tab = (PagerTabStrip) findViewById(R.id.tab);
        tab.setBackgroundColor(Color.RED);
        tab.setTextColor(Color.YELLOW);
        tab.setDrawFullUnderline(false);
        tab.setTabIndicatorColor(Color.GREEN);

        //为 ViewPager 页卡设置标题
        titleList = new ArrayList<String>();
        titleList.add("第一页");

        //创建PagerAdapter适配器
        MyPagerAdapter adapter = new MyPagerAdapter(viewList, titleList);

        //初始化 ViewPager 加载适配器
        viewPager = (ViewPager) findViewById(R.id.pager);
        viewPager.setAdapter(adapter);


    }
}


```