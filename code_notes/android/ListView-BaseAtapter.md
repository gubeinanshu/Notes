
### activity_main.xml

```
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/activity_main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"

    tools:context="com.example.testbaseadapter.MainActivity">


    <ListView
        android:id="@+id/lv_main"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_alignParentLeft="true"
        android:layout_alignParentStart="true" />
</RelativeLayout>

```

### item.xml

新建布局文件 item.xml

```
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <ImageView
        android:src="@mipmap/ic_launcher"
        android:id="@+id/iv_image"
        android:layout_width="60dp"
        android:layout_height="60dp" />
    <TextView
        android:id="@+id/tv_title"
        android:text="Title"
        android:gravity="center"
        android:textSize="25sp"
        android:layout_width="match_parent"
        android:layout_height="30dp"
        android:layout_toRightOf="@+id/iv_image" />

    <TextView
        android:id="@+id/tv_content"
        android:text="Content"
        android:gravity="center_vertical"
        android:textSize="20sp"
        android:layout_toRightOf="@+id/iv_image"
        android:layout_below="@+id/tv_title"
        android:layout_width="match_parent"
        android:layout_height="30dp" />


</RelativeLayout>

```

### ItemBean.java

新建 Bean 文件 ItemBean.java

```
package com.example.testbaseadapter;

/**
 * Created by zhu on 2017/3/3.
 */

public class ItemBean {
    public int ImageResid;
    public String ItemTitle;
    public String ItemContent;

    public ItemBean(int imageResid,String itemContent,  String itemTitle) {
        ItemContent = itemContent;
        ImageResid = imageResid;
        ItemTitle = itemTitle;
    }

}

```

### MyAdapter.java

新建 MyAdapter.java 继承 BaseAtapter

```
package com.example.testbaseadapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;

import java.util.List;

/**
 * Created by zhu on 2017/3/3.
 */

public class MyAdapter extends BaseAdapter {

    private List<ItemBean> mList;
    private LayoutInflater mInflater;

    public MyAdapter(Context context,List<ItemBean> list){
        mList = list;
        mInflater = LayoutInflater.from(context);
    }

    @Override
    public int getCount() {

        return mList.size();
    }

    @Override
    public Object getItem(int position) {
        return mList.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        //ViewHolder是model，定义在最底下
        ViewHolder viewHolder;
        if(convertView == null){
            viewHolder = new ViewHolder();
            //加载布局文件item.xml
            convertView = mInflater.inflate(R.layout.item,null);
            //通过convertView获取组件
            viewHolder.imageView = (ImageView) convertView.findViewById(R.id.iv_image);
            viewHolder.title = (TextView) convertView.findViewById(R.id.tv_title);
            viewHolder.content = (TextView) convertView.findViewById(R.id.tv_content);
            convertView.setTag(viewHolder);
        } else {
            viewHolder = (ViewHolder) convertView.getTag();
        }
        ItemBean bean = mList.get(position);
        //赋值
        viewHolder.imageView.setImageResource(bean.ImageResid);
        viewHolder.title.setText(bean.ItemTitle);
        viewHolder.content.setText(bean.ItemContent);

        return convertView;
    }
    class ViewHolder {
        public ImageView imageView;
        public TextView title;
        public TextView content;
    }
}

```

### MainActivity

```
package com.example.testbaseadapter;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ListView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
   // private MyAdapter myAdapter;
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        listView = (ListView) findViewById(R.id.lv_main);

        //数据源
        List<ItemBean> itemBeanList = new ArrayList<>();
        for (int i=0;i<20;i++){
            itemBeanList.add(new ItemBean(
                    R.mipmap.ic_launcher,
                    "bitaoti"+i,
                    "neirong"+i
            ));
        }
        listView.setAdapter(new MyAdapter(this,itemBeanList));

    }
}

```

