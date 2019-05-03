
## C

常用头文件有 stdio.h conio.h stdlib.h string.h iostream.h iostream algorithm stdbool.h time.h ctype.h

枚举enum  
共用体、联合体union
自定义类型typedef  

代码区，全局函数区，堆区，栈区

带默认形参的函数（只能从右到左）

变量类型:auto static exterm register

函数的重载 

printf("%f",(double)clock()/CLOCKS_PER_SEC);

文件操作 FILE *p    p=fopen("文件名","r/a/w"）；
		    p=freopen("CON","r/a/w");

文件重定向 freopen("文件名","r/a/w",stdin);freopen("文件名","r/a/w",stdout);
恢复重定向 freopen("CON","r/a/w",stdin);freopen("CON","r/a/w",stdin);
	在Linux中freopen("/dev/console","r/a/w",stdin);
文件操作 feof fgetc fputc fgets fputsfprintf fscanf fread fwrites
文件定位：
rewind（fp） 返回文件首
fseek（fp,长整型数，0）; 长整型数：long 100l 可在数字后加l。
从哪里开始移动用：0、SEEK_SET文件首1、SEEK_SET当前位置2、SEEK_SET文件尾 加负号则从后到前移动
1、文件结束检测函数feof函数
调用格式：feof(fp); 判断文件是否处于文件结束位置，结束返回1，否则为0；
2、读写文件出错检测函ferror
调用格式：ferror(fp); 检查文件在用各种输入输出函数进行读写时是否出错，未出错返回0，否则1；
3、文件出错标志和文件结束标志置0函数 clearerr
调用格式：clearerr(fp); 本函数用于清除出错标志和文件结束标志，使它们为0值；

stdin 标准输入设备
stdout 标准输出设备
stderr 标准错误输出设备；prttor()等函数想此输出数据
stdprn 标准打印设备（打印机）
stdaux 标准辅助输入输出设备（异步串行口）

缓冲区：全缓冲，行缓冲，不带缓冲
缓冲区的大小由stdio.h中的宏BUFSIZ定义
	查看它的大小 printf("%d",BUFSIZ);
getchar() 有缓冲区 stdio.h 有回显
getch()	  无缓冲区 conio.h 无回显
getche()  无缓冲区 conio.h 有回显

复合赋值符有利于编译处理，能提高编译效率并产生质量较高的目标代码

位域概念
	struct aa
	{
		int a:8;
		int b:2;
		int c:6;
	};
一个位域必须存储在同一个字节中，不能跨两个字节。如一个字节所剩空间不够存放另一个位域时，应从下一单元开始
使用   :0;可以有意使位域从下一单元开始
例如：
struct aa
	{
		unsigned a:4;
		unsigned :0;
		unsigned b:2;
		unsigned c:6;
	};
位域可以无位域名，此时只用来填充或调整位置。无名的位域不能使用的。
例如：
struct aa
	{
		int a:2;
		int  :1;
		int b:2;
		int c:3;
	};
位域允许各种格式输出
----------------------------------------------------------------------------------------------------
inline 内联函数

1.常量指针(Constant Pointers)
int * const p
先看const再看* ，是p是一个常量类型的指针，不能修改这个指针的指向，但是这个指针所指向的地址上存储的值可以修改。

2.指向常量的指针(Pointers to Constants)
const int *p
先看*再看const，定义一个指针指向一个常量，不能通过指针来修改这个指针指向的值。

 #ifdef #ifndef #undef #if #else #elif #endif #error #line

sqrt(100.0)求平方根 

pow(.0,.0)求x的y次方

strlen（str1）求一个字符串的长度

fabs()求绝对值 

fgets(要写的数组的地址，n个位置最多写入n-1个最后赋'\n'，stdin);比gets好，gets会溢出

qsort(要排序的数组的地址；要排的个数；每个单元的大小；cmp比较函数）;可以排列int型数组，字符排序，字符串排序；
	可以从小到大排，从大到小排；

atoi(str1)把字符串转换为相应的整数 例如 "12345"--12345

itoa(number数字, string字符数组, 10 个数);//把整数转换为字符串

sscnaf 从字符数组中读到一个变量中

sprintf 可以把数字输出到字符数组中 要换行必须"/r/n"

cprintf 要换行必须"/r/n"

memset(要赋值或者初始化的地址（数组 结构体）;值;大小/范围(sizeof()*n));

memset(b,a,sizezof(b));大小为b的 a中的值赋给b；全部赋值；与strcmp不同

strcmp(a,b);b值赋给a；到'\0'结束；

strcmp（str1，str2）比较两个字符串的大小，可以判断两个字符串是否相同

malloc(要申请的内存大小）返回void指针
calloc(个数，要申请的内存大小）返回void指针
free 释放内存

isalpha(c) 头文件ctype.h用于判断是否为大写字母或小写字母（不是字母返回0，大写返回1，小写返回2）

toupper(c) 头文件ctype.h返回c的大写形式




## C++

C++有两种初始化方法：
	赋值初始化：int c = 11;
	直接初始化：int c(11);

命名空间关键字：namespace
	namespace A
	{
		....
	}
	cout << A::x<<endl;

引用：取别名，是同一个变量
基本数据类型的引用：    int a = 3;
			int &b = a;//引用必须初始化
结构体类型的引用：（与上类似）
指针类型的引用：类型 *&指针引用名 = 指针
引用作函数参数：void fun （int &a,int &b){} fun(x,y);------指针做参数还是原来的
const 与 引用：int x = 3; const int &y = x;（y被固定）

函数参数默认值:有默认参数值的参数必须在参数表的最右端
		无实参则用默认值，否则实参覆盖默认值

函数重载：在相同作用域内，用同一函数名定义的多个函数，参数个数个参数类型不同
（因为编译时会把参数表也作为函数名）

内联函数 关键字：inline
	inline int max(int a,int b,int c)
(内联编译时建议性的，有编译器决定。逻辑简单，调用频繁的函数建议使用内联。
	递归函数无法使用内联方式）

内存的申请和释放：new 及 delete 
	int *arr = new int [10];
	delete []arr;
释放内存注意事项
	int *p = new int[1000];
	if(p == NULL){//内存分配失败//异常处理}
	delete []p;
	p = NULL;
（申请内存需要判断是否成功，释放内存需要设空指针）

访问限定符：public protected private

从栈实例化对象：class TV{};  TV tv[30];
从堆实例化对象：TV *p = new TV(); TV *q = new TV[20];
		（当类为默认构造函数时 TV *p = new TV;也可以）

对象成员访问

string 类型：string name = "ahfjd";
(<string>)   string habby("ajksf");
初始化string对象的方式：
	string s1;        s1为空串
	string s2("ABC"); 用字符串字面值初始化s2
	string s3(s2);    将s2初始化为s2的一个副本
	string s4(n,'c'); 将s4初始化为字符'c'的n个副本
string 的常用操作：
	s.empty() 若为空串，返回ture,否则返回false
	s.size()  返回s中字符的个数
	s.length()返回字符个数
	s1 + s2   将两个串连接成新串，返回新生成的串
	s1 = s2   把s1的内容替换为s2的副本
	v1 == v2  判定相等，相等返回ture,否则返回false
	v1 != v2  判定不等，不等返回ture,否则返回false

类内定义与内联函数
类内定义：（定义部分在类内）
类外定义：同文件类外定义
	：分文件类外定义
在后缀为".h"的文件里进行声明，在".cpp"的文件里定义，要包含".h"文件。
	定义时使用 域运算符"::"，例：void Car::run(){}

内存分区：
	栈区：int x = 0;int *p = NULL;
	堆区：int *p = new int [20];
	全局区：存储全局变量及静态变量
	常量区：string str = "hello";
	代码区：存储逻辑代码的二进制
（对象共用代码区）

构造函数的规则和特点：
	构造函数在对象实例化时被自动调用
	构造函数与类同名
	构造函数没有返回值
	构造函数可以有多个重载形式	
	实例化对象时仅用到一个构造函数
	当没有定义构造函数时，编译器会自动生成一个构造函数
无参构造函数；
默认构造函数；

初始化列表：Student():m_strName("jim"),m_iAge(10){}
初始化列表特性：(能初始化const修饰的变量）
	初始化列表先于构造函数执行
	初始化列表只能用于构造函数（普通构造函数，拷贝构造函数）
	初始化列表可以同时初始化对个数据成员

拷贝构造函数；定义格式：类名（const 类名&变量名）
		例：Student(const Student& stu){}
（如果没有自定义的拷贝构造函数则系统自动生成一个默认的拷贝构造函数
  当采用直接初始化或复制初始化实例化对象时，系统自动调用拷贝构造函数）

构造函数：无参构造函数---->默认构造函数
	：有参构造函数-->参数带默认值------>默认构造函数
		      -->参数无默认值

析构函数：定义格式：~类名（）
	~Student(){delete []m_pName;}
(如果没有自定义的析构函数则系统自动生成
 析构函数在对象销毁时自动调用
 析构函数没有返回值，内有参数也不能重载）

对象的生命历程：
	申请内存-->初始化列表-->构造函数-->参与运算-->析构函数-->释放内存

一个类中包含对象成员是，先构造对象成员再类，析构时先类再对象成员

拷贝构造函数：浅拷贝（值复制），深拷贝（数组进行复制）。
class Array
{
public:
	Array(){m_iCount = 5;n_pArr = new int[m_iCount];}
	Array(const Array& arr）{
	  m_iCount = arr.m_iCount;
	  m_pArr = new int[m_iCount]'
	  for(int i=0;i<m_iCount;i++)
		m_pArr[i] = arr.m_pArr[i];
	}
private:	
	int m_iCount;
	int *m_pArr;
};

Line::Line(int a,int b,int c,int d):m_coorA(a,b),m_coorB(c,d){};

对象成员指针：

this指针：(this <==> &arr1;)
(函数的隐含 参数）
this指针在参数列表中的位置；

Array Array::printfInfo()
{ return *this; } //返回一个临时的Array

Array& Array::printfInfo()
{ return *this; } //返回该Array

Array* Array::printfInfo()
{ return this; } //返回该Array指针

常对象成员：例：const Coordinate m_coorA;
常成员函数：例：void changeX() const;

常成员函数中不能改变数据成员的值：因为使用const时，把函数隐含的this给const掉了
（
	void changeX() const;
	void changeX();       (互为重载）
	直接调用时调用不带const的
	实例化常对象时 调用带const的
）

对象指针与对象引用：
（
	Coordinate coor1(3,5);
	Coordinate &coor2 = coor1;
	Coordinate *pCoor = &coor1;
	...
）
对象的常指针与常引用：
（
	Coordinate coor1(3,5);
	const Coordinate &coor2 = coor1; //只有读权限，只能调用常成员函数
	const Coordinate *pCoor = &coor1;//只有读权限，只能调用常成员函数
	...
	Coordinate * const pCoor = &coor1;//指针值不能变，有读写权限
）


继承：派生类 基类 子类 父类
class Worker:public Person{}
实例化对象时：先父类再子类

继承方式：
共有继承：class A:public B
保护继承：class A:protected B
私有继承：class A:private B

基类成员访问属性   	继承方式  派生类成员访问属性
private成员				无法访问
protected成员		public		protected
public成员				public

基类成员访问属性   	继承方式  派生类成员访问属性
private成员				无法访问
protected成员		protected	protected
public成员				protected

基类成员访问属性   	继承方式  派生类成员访问属性
private成员				无法访问
protected成员		private		private
public成员				private

覆盖----隐藏
父类与子类有同名函数或变量（成员同名），会被子类覆盖（即隐藏）
soldier.play();
soldier.Person::play();//通过这样的方式可以访问父类的同名成员
同名变量：
void Soldier::work()
{
	code = 1234;
	Person::code = "5678";
}

Soldier s1;
Person p1 = s1;//只能赋值继承的成员，反过来不行
Person *p2 = &s1;//只能指向继承的成员，反过来不行

多继承和多重继承：
多重继承：人类-->士兵类-->步兵类
多继承  ：继承多个类 例：class MigrantWorker:public Worker,public Farmer{};

菱形继承不可取
虚继承：关键字 virtual
class Worker:virtual public Person{};
class Farmer:virtual public Person{};
class MigrantWorker:public Worker,public Farmer{};
这样就可以避免继承相同的部分了


## 程序员数学

> 这是以前看程序员的数学这本时，记下的重点，当时获益良多，有空还得再看看


0 -- 做出简单规则符（无即是有）
	引入0以后，更容易简化规则

逻辑 -- 两个世界，（分为条件成立，条不件成立）
	逻辑表达式、真值表、文氏图、卡诺图

余数 -- 分组（规律）（奇偶性 - 分为奇偶―两组）
	有效利用余数，能将分散的事物同等看待并加以分类。

数学归纳法 -- 通过两个步骤挑战无穷
（只需通过基底和归纳2个步骤就能进行有关无穷的证明）
	将大问题分解为n个同类同规模的小问题

排列组合 -- 关键在于认清问题的性质
对于多的无法直接计数的庞大数据，先缩小规模找出问题的本质，再将其抽象化，就能得到答案
不要光摆弄数字，认清计数对象的性质和结构是要点。不应死记硬背公式，应更关注组合逻辑上的意义

递归 -- 在自己中找出自己
递归也是分解问题的方法，但不是分解成同类同规模的问题，而是分解成同类不同规模的问题
在面对复杂的问题时，先观察它的内部是否含有此昂同结构的小规模问题。如果正确的找到了递归结构，就可以使用递归公式抓住问题的本质

指数爆炸 -- ......对数解决的方法

不可解问题 -- 展示了原理上的界限（可数的概念-可数无穷，不可解问题，停机问题）