
## 完成实体类

### Result 实体类

```
package zhu.jsontest;

import java.util.List;

/**
 * Created by zhu on 2017/5/8.
 */

public class Result {
    private int result;
    private List<Person> personList;

    public int getResult() {
        return result;
    }

    public void setResult(int result) {
        this.result = result;
    }

    public List<Person> getPersonList() {
        return personList;
    }

    public void setPersonList(List<Person> personList) {
        this.personList = personList;
    }
}

```

### SchoolInfo 实体类

```
package zhu.jsontest;

/**
 * Created by zhu on 2017/5/8.
 */

public class SchoolInfo {
    private String schoolName;

    public String getSchoolName() {
        return schoolName;
    }

    public void setSchoolName(String schoolName) {
        this.schoolName = schoolName;
    }
}

```

### Person 实体类

```
package zhu.jsontest;

import java.util.List;

/**
 * Created by zhu on 2017/5/8.
 */

public class Person {
    private String name;
    private int age;
    private String url;
    private List<SchoolInfo> schoolInfoList;

    public String getName() {
        return name;
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

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public List<SchoolInfo> getSchoolInfoList() {
        return schoolInfoList;
    }

    public void setSchoolInfoList(List<SchoolInfo> schoolInfoList) {
        this.schoolInfoList = schoolInfoList;
    }
}

```

## 生成 json 数据

```
@Test
    public void TJson(){
        Result result = new Result();

        result.setResult(1);
        List<Person> list = new ArrayList<Person>();
        result.setPersonList(list);

        Person person1 = new Person();
        person1.setName("zhu");
        person1.setAge(20);
        person1.setUrl("111111111111111");

        List<SchoolInfo> schoolInfoList = new ArrayList<SchoolInfo>();
        SchoolInfo schoolInfo1 = new SchoolInfo();
        schoolInfo1.setSchoolName("aaaa");
        SchoolInfo schoolInfo2 = new SchoolInfo();
        schoolInfo2.setSchoolName("bbbb");
        schoolInfoList.add(schoolInfo1);
        schoolInfoList.add(schoolInfo2);

        person1.setSchoolInfoList(schoolInfoList);

        list.add(person1);

        //使用 Gson 生成
        Gson gson = new Gson();
        System.out.println(gson.toJson(result));


    }
```

### 解析 json 数据

```
@Test
    public void Tjson2(){

        List<Person> persons = new ArrayList<Person>();
        String s = "{\"personList\":[{\"age\":20,\"name\":\"zhu\",\"schoolInfoList\":[{\"schoolName\":\"aaaa\"},{\"schoolName\":\"bbbb\"}],\"url\":\"111111111111111\"}],\"result\":1}";
        try {
            //String 转换成 JSONObject
            JSONObject object = new JSONObject(s);
            int result = object.getInt("result");

            if(result==1){
                //获取标签下的person数组
                JSONArray personList = object.getJSONArray("personList");

                for(int i=0;i<personList.length();i++){
                    Person personObject = new Person();

                    //获取每个person对象
                    JSONObject person = personList.getJSONObject(i);

                    String name = person.getString("name");
                    int age = person.getInt("age");
                    String url = person.getString("url");

                    personObject.setName(name);
                    personObject.setAge(age);
                    personObject.setUrl(url);
                    List<SchoolInfo> schoolInfoListObject = new ArrayList<SchoolInfo>();
                    personObject.setSchoolInfoList(schoolInfoListObject);

                    //获取学校对象数组
                    JSONArray schoolInfoList = person.getJSONArray("schoolInfoList");
                    for(int j=0;j<schoolInfoList.length();j++){
                        SchoolInfo schoolInfo = new SchoolInfo();
                        //获取每个学校对象
                        JSONObject school = schoolInfoList.getJSONObject(j);
                        String schoolName = school.getString("schoolName");

                        schoolInfo.setSchoolName(schoolName);
                        schoolInfoListObject.add(schoolInfo);
                    }

                }

                System.out.println(personList.toString());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
```

