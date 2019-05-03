
可参考该博客：[Android 数据查询query函数参数解析](http://notfatboy.iteye.com/blog/653357)

### sql语句操作

```
package zhu.sqlitetest;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        //每个程序都有自己的数据库 默认情况下是各自互相不干扰
        //创建一个数据库 并且打开
        SQLiteDatabase db =   openOrCreateDatabase("user.db", MODE_PRIVATE, null);
        db.execSQL("create table if not exists usertb (_id integer primary key autoincrement,
            name text not null , age integer not null , sex text not null )");
        db.execSQL("insert into usertb(name,sex,age) values('张三','女',18)");
        db.execSQL("insert into usertb(name,sex,age) values('李四','女',19)");
        db.execSQL("insert into usertb(name,sex,age) values('王五','男',20)");

        Cursor c = db.rawQuery("select * from usertb", null);
        //如果查询数据库返回cursor，要判断记录是否为空
        //cursor.getCount() 如果记录为空，该函数返回的值为0 。
        if (c!=null) {
            while (c.moveToNext()) {
                Log.i("info", "_id:"+c.getInt(c.getColumnIndex("_id")));
                Log.i("info", "name:"+c.getString(c.getColumnIndex("name")));
                Log.i("info", "age:"+c.getInt(c.getColumnIndex("age")));
                Log.i("info", "sex:"+c.getString(c.getColumnIndex("sex")));
                Log.i("info", "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
            }
            c.close();
        }
        db.close();
    }
}
```


### 内置对象操作

```
package zhu.sqlitetest;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        SQLiteDatabase db = openOrCreateDatabase("stu.db", MODE_PRIVATE, null);
        db.execSQL("create table if not exists stutb(_id integer primary key autoincrement,name text not null,sex text not null,age integer not null)");
        // ContentValues 负责存储一些名值对
        ContentValues values = new ContentValues();
        values.put("name", "张三");
        values.put("sex", "男");
        values.put("age", 19);
        long rowId = db.insert("stutb", null, values);
        values.clear();
        values.put("name", "张三丰");
        values.put("sex", "男");
        values.put("age", 99);
        db.insert("stutb", null, values);
        values.clear();
        values.put("sex", "女");
        db.update("stutb", values, "_id>?", new String[]{"3"});//将全部id>3的人的性别改成女
        db.delete("stutb", "name like ?", new String[]{"%丰%"});//删除所有名字中带有丰的人
        Cursor c = db.query("stutb", null, "_id>?", new String[]{"0"}, null, null, "name");
        if (c!=null) {
            String [] columns= c.getColumnNames();
            while (c.moveToNext()) {
                for (String columnName : columns) {
                    Log.i("info", c.getString(c.getColumnIndex(columnName)));
                }
            }
            c.close();
        }
        db.close();
    }
}

```

### DBOpenHelper
DBOpenHelper 继承 SQLiteOpenHelper 类
```
package zhu.sqlitetest;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteDatabase.CursorFactory;
import android.database.sqlite.SQLiteOpenHelper;

//SQLiteOpenHelper 是 SQLiteDatabase 的帮助类，用于管理数据库的创建和版本更新
public class DBOpenHelper extends SQLiteOpenHelper{

    //自己加的构造方法
    public DBOpenHelper(Context context, String name) {
        super(context, name, null, 1);
        // TODO Auto-generated constructor stub
    }
    public DBOpenHelper(Context context, String name, CursorFactory factory, int version) {
        super(context, name, factory, version);
        // TODO Auto-generated constructor stub
    }

    //首次创建数据库的时候调用 一般可以把建库 建表的操作
    @Override
    public void onCreate(SQLiteDatabase db) {
        // TODO Auto-generated method stub
        db.execSQL("create table if not exists stutb(_id integer primary key autoincrement,name text not null,sex text not null,age integer not null)");
        db.execSQL("insert into stutb(name,sex,age)values('张三','女',18)");
    }

    //当数据库的版本发生变化的时候 会自动执行
    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // TODO Auto-generated method stub
        
    }

}

```

### SQLiteOpenHelper
SQLiteOpenHelper 使用
```
package zhu.sqlitetest;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        DBOpenHelper helper =   new DBOpenHelper(MainActivity.this, "stu2.db");
//      helper.getReadableDatabase();//获取一个只读的数据库 只能查询 不能写入 不能更新
        SQLiteDatabase db = helper.getWritableDatabase();
//      db.query(table, columns, selection, selectionArgs, groupBy, having, orderBy)
        Cursor c = db.rawQuery("select * from stutb", null);
        if (c!=null) {
            String [] cols = c.getColumnNames();
            while (c.moveToNext()) {
                for (String ColumnName : cols) {
                    Log.i("info", ColumnName+":"+c.getString(c.getColumnIndex(ColumnName)));
                }
            }
            c.close();
        }
        db.close();
    }
}

```
