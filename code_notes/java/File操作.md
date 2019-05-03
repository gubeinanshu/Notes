
### File api

File 常用api

```java
package zhu;

import java.io.File;
import java.io.IOException;

public class FileTest {

	public static void main(String[] args) {
		
		File file = new File("G:\\test");
		//使用File.separator可以自适应windows和linux系统
		//File file1 = new File("g:"+File.separator);
		if(!file.exists()){
			//创建目录
			file.mkdir();// file.mkdirs();//创建多级目录
		}
		else {
			file.delete();
		}
		//是否是一个目录,是返回true，不是或者不存在返回false
		System.out.println(file.isDirectory());
		//是否是一个文件
		System.out.println(file.isFile());
		
		//File file2 = new File("G:\\1.txt");
		File file2 = new File("G:","1.txt");
		if(!file2.exists()){
			try {
				file2.createNewFile();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		} 
		else {
			file2.delete();
		}
		//常用的File对象的API
		
		//file.toString的内容
		System.out.println(file);

		System.out.println(file.getName());
		System.out.println(file2.getName());
		System.out.println(file.getParent());
		System.out.println(file2.getParent());
		System.out.println(file.getParentFile().getAbsolutePath());
		
		
	}

}

```

### File listFiles()

File 遍历目录

```java
package zhu;

import java.io.File;
import java.io.IOException;

public class FileUtils {
//列出File的一些常用操作，比如过滤、遍历等操作
	

	/**
	 * 列出指定目录下（包括其子目录的所有文件）
	 * @param dir
	 * @throws IOException
	 */	
	public static void listDirectory(File dir)throws IOException{
		if(!dir.exists()){
			throw new IllegalArgumentException("目录:"+dir+"不存在");
		}
		if(!dir.isDirectory()){
			throw new IllegalArgumentException(dir+"不是目录");
		}
		/*String[] filenames = dir.list();//返回的是字符串数组
		for(String string:filenames){
			System.out.println(dir+"\\"+string);
		}*/
		//遍历子目录下的内容
		File[] files = dir.listFiles();
		if(files!=null && files.length > 0){
			for(File file : files){
				if(file.isDirectory()){
					listDirectory(file);
				}else {
					System.out.println(file);
				}
			}
		}
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		File file = new File("G:");
		try {
			listDirectory(file);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}

```

### RandomAccessFile
文件读写类，可以随机读写
```java
package zhu;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.Arrays;

public class RafDemo {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		File demo = new File("G:\\demo");
		if(!demo.exists()){
			demo.mkdir();
		}
		//另一种文件路径的初始化方式
		File file = new File(demo,"raf.dat");
		if(!file.exists()){
			file.createNewFile();
		}
		RandomAccessFile raf = new RandomAccessFile(file, "rw");
		//指针的位置
		System.out.println(raf.getFilePointer());
		raf.write('A');//只写了一个字节
		System.out.println(raf.getFilePointer());
		
		int i = 0x7fffffff;
		//用write方法每次只能写一个字节，如果要把i写进去就得写4次
		raf.write(i >>> 24);
		raf.write(i >>> 16);
		raf.write(i >>> 8);
		raf.write(i);
		System.out.println(raf.getFilePointer());
		
		//可以直接写一个int
		raf.writeInt(i);
		
		String s = "中";
		byte[] gbk = s.getBytes("utf-8");
		raf.write(gbk);
		System.out.println(raf.length());
		
		//读文件，必须把指针移到头部
		raf.seek(0);
		//一次性读取，吧文件中的内容都读到字节数组中
		byte[] buf = new byte[(int)raf.length()];
		raf.read(buf);
		System.out.println(Arrays.toString(buf));
		
		String s1 = new String(buf);
		System.out.println(s1);
		
		for(byte b:buf){
			System.out.println(Integer.toHexString(b&0xff));
		}
		raf.close();
	}

}

```
