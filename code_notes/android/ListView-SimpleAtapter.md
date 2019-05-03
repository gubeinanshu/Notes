
### activity_main.xml

```
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/activity_main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"

    tools:context="com.example.testlistview.MainActivity">

    <ListView
        android:id="@+id/listView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_alignParentTop="true"
        android:layout_alignParentLeft="true"
        android:layout_alignParentStart="true" />
</RelativeLayout>

```

### 新建 item.xml

新建布局文件 item.xml

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal">

    <ImageView
        android:id="@+id/pic"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginLeft="15dp"
        android:src="@mipmap/ic_launcher"
        />
    <TextView
        android:id="@+id/t"
        android:textSize="20sp"
        android:textColor="#000000"
        android:text="demo"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

</LinearLayout>

```

### MainActivity

```
package com.example.testlistview;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AbsListView;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.SimpleAdapter;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class MainActivity extends AppCompatActivity {
    private ListView listView;
    private SimpleAdapter simpleAdapter;
    private List<Map<String,Object>>dataList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        listView= (ListView) findViewById(R.id.listView);
        //数据源
        dataList = new ArrayList<Map<String, Object>>();

        /**
         * SimpleAdapter(this,data,resource,from,to)
         * 第一个参数 context
         * 第二个参数 数据源
         * 第三个参数 (加载)布局文件
         * 第四个参数 项目名称,名字可以自己取，一般取一样就行
         * 第五个参数 在布局文件中的组件id,与项目名称对应
         */
        simpleAdapter=new SimpleAdapter(this,getData(),R.layout.item,
                new String[]{"pic","t"},new int[]{R.id.pic,R.id.t});

        listView.setAdapter(simpleAdapter);

        //监听点击事件
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                String text = listView.getItemAtPosition(position)+"";
                Toast.makeText(Tttt.this,"position="+position+"text="+text,Toast.LENGTH_SHORT).show();
            }
        });
        //监听滚动事件
        listView.setOnScrollListener(new AbsListView.OnScrollListener() {

            @Override
            public void onScrollStateChanged(AbsListView view, int scrollState) {
                switch (scrollState){
                    case SCROLL_STATE_FLING:
                        Log.i("Main","用户在手指离开屏幕之前，由于用力滑了一下，视图仍以靠惯性继续滑动");
                        Map<String,Object> map = new HashMap<String,Object>();
                        map.put("pic", R.mipmap.ic_launcher);
                        map.put("t", "增加项");
                        dataList.add(map);
                        //让UI线程刷新
                        simpleAdapter.notifyDataSetChanged();
                        break;
                    case SCROLL_STATE_IDLE:
                        Log.i("Main","视图已停止滑动");
                        break;
                    case SCROLL_STATE_TOUCH_SCROLL:
                        Log.i("Main","手指没有离开屏幕");
                        break;

                }
            }
            //滑动时触发
            @Override
            public void onScroll(AbsListView view, int firstVisibleItem, int visibleItemCount, int totalItemCount) {
                //Log.i("main","ONSCROLL");
            }
        });


    }
    private List<Map<String,Object>> getData(){
        for(int i=0;i<20;i++){
            Map<String,Object>map = new HashMap<String, Object>();
            map.put("pic",R.mipmap.ic_launcher);
            map.put("t", "a"+i);
            dataList.add(map);
        }
        return dataList;
    }


}

```