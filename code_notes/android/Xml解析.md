
### XmlThread

```
package zhu.xmltest;

import android.util.Log;
import android.widget.Toast;

import org.xmlpull.v1.XmlPullParser;
import org.xmlpull.v1.XmlPullParserException;
import org.xmlpull.v1.XmlPullParserFactory;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by zhu on 2017/5/8.
 */

public class XmlThread extends Thread {

    private String url;

    public XmlThread(String url){
        this.url = url;
    }

    @Override
    public void run() {

        try {
            //String 包装成 URL
            URL httpUrl = new URL(url);
            //获取连接
            HttpURLConnection conn = (HttpURLConnection) httpUrl.openConnection();
            //设置请求方式
            conn.setRequestMethod("GET");
            //设置超时
            conn.setReadTimeout(5000);
            //获取返回的流
            InputStream in = conn.getInputStream();
            XmlPullParserFactory factory = XmlPullParserFactory.newInstance();
            XmlPullParser parser = factory.newPullParser();
            //设置编码
            parser.setInput(in, "UTF-8");
            //开始解析
            int enenType = parser.getEventType();
            List<Girl> list = new ArrayList<Girl>();
            Girl girl = null;
            while (enenType!=XmlPullParser.END_DOCUMENT){
                String data = parser.getName();
                switch (enenType){
                    case XmlPullParser.START_TAG:
                        if("girl".equals(data)){
                            girl = new Girl();
                        }
                        if("name".equals(data)){
                            girl.setName(parser.nextText());
                        }
                        if("age".equals(data)){
                            girl.setAge(Integer.parseInt(parser.nextText()));
                        }
                        if("school".equals(data)){
                            girl.setSchool(parser.nextText());
                        }
                        break;
                    case XmlPullParser.END_TAG:
                        if("girl".equals(data)&&girl!=null){
                            Log.i("tag", girl.toString()+"aaaaaaaaaaaaaaaaa");
                            System.out.println(girl.toString()+"bbbbbbbbbbbbb");
                            list.add(girl);
                        }
                        break;
                }
                enenType = parser.getEventType();
            }

        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (XmlPullParserException e) {
            e.printStackTrace();
        }

    }
}

```
### Girl 实体类

```
package zhu.xmltest;

/**
 * Created by zhu on 2017/5/8.
 */

public class Girl {
    private String name;
    private int age;
    private String school;

    public String getName() {
        return name;
    }
    public String toString(){
        return "Name="+ name +"AGE"+ age+"SCHOOL"+school;
    }
    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }
}

```

### MainActivity

```
package zhu.xmltest;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        new XmlThread("请求地址").start();
    }
}

```
