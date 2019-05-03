
### view

新建 view.xml 文件

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
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
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context="zhu.viewpagertest2.MainActivity">

    <android.support.v4.view.ViewPager
        android:id="@+id/pager"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:foregroundGravity="center">



    </android.support.v4.view.ViewPager>

</android.support.constraint.ConstraintLayout>

```

### Fragment1

新建 Fragment1 继承 Fragment 类

```
package zhu.viewpagertest2;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

/**
 * Created by zhu on 2017/4/28.
 */

public class Fragment1 extends Fragment {
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.view1, container, false);

    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        Log.i("main","销毁了");
    }
}

```

### MyAdapter 不销毁

新建 MyFragmentPagerAdapter 继承 FragmentPagerAdapter 类(不会自动销毁)

不会执行 Fragment1 中的 onDestroy() 方法，因为不会销毁 Fragment

```
package zhu.viewpagertest2;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;

import java.util.List;

/**
 * Created by zhu on 2017/4/29.
 */

public class MyFragmentPagerAdapter extends FragmentPagerAdapter {

    private List<Fragment> fragmentList;

    public MyFragmentPagerAdapter(FragmentManager fm, List<Fragment> fragmentList) {
        super(fm);
        this.fragmentList = fragmentList;
    }

    @Override
    public Fragment getItem(int position) {
        return fragmentList.get(position);
    }

    @Override
    public int getCount() {
        return fragmentList.size();
    }
}

```

### MainActivity

继承 FragmentActivity 类(兼容低版本)

```
package zhu.viewpagertest2;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentActivity;
import android.support.v4.view.ViewPager;
import android.os.Bundle;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends FragmentActivity {

    private ViewPager viewPager;
    private List<Fragment> fragmentList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        viewPager = (ViewPager) findViewById(R.id.pager);
        fragmentList = new ArrayList<Fragment>();

        fragmentList.add(new Fragment1());


        MyFragmentPagerAdapter myFragmentPagerAdapter = new MyFragmentPagerAdapter(getSupportFragmentManager(), fragmentList);

        viewPager.setAdapter(myFragmentPagerAdapter);

        //设置监听器
        viewPager.setOnPageChangeListener(new ViewPager.OnPageChangeListener() {
            @Override
            public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {

            }
            //当切换到一个页卡时
            @Override
            public void onPageSelected(int position) {
                Toast.makeText(getApplicationContext(), "当前是第"+(position+1)+"个页面", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onPageScrollStateChanged(int state) {

            }
        });


    }
}


```

### MyAdapter 会销毁

新建 MyFragmentPagerAdapter 继承 FragmentPagerAdapter 类(会自动销毁)

会执行 Fragment1 中的 onDestroy() 方法

```
package zhu.viewpagertest2;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.support.v4.app.FragmentStatePagerAdapter;
import android.view.ViewGroup;

import java.util.List;

/**
 * Created by zhu on 2017/4/29.
 */

public class MyFragmentPagerAdapter2 extends FragmentStatePagerAdapter {

    private List<Fragment> fragmentList;

    public MyFragmentPagerAdapter2(FragmentManager fm, List<Fragment> fragmentList) {
        super(fm);
        this.fragmentList = fragmentList;
    }

    @Override
    public Fragment getItem(int position) {
        return fragmentList.get(position);
    }

    @Override
    public int getCount() {
        return fragmentList.size();
    }

    @Override
    public Object instantiateItem(ViewGroup container, int position) {
        return super.instantiateItem(container, position);
    }

    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        super.destroyItem(container, position, object);
    }
}
```
