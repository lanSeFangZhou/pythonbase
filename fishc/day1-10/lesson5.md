# 闲聊数据类型  
0. 在 Python 中，int 表示整型，那你还记得 bool、float 和 str 分别表示什么吗？
   bool，布尔型
   float,浮点型
   str，字符串类型  
   
   bool表示布尔型;float代表浮点型;str表示字符串

1. 你知道为什么布尔类型(bool)的 True 和 False 分别用 1 和 0 来代替吗？  
   因为计算机的底层是二进制编码的  
   
   你可能听说过计算机很“笨”的，究其根本是因为它只认识二进制数，所以所有的编程语言  
   最终都会转换成简单的二进制序列给CPU按照一定的规则解析。  
   由于二进制只有两个数字:0和1,因此用0和1来表示False和True再合适不过了，因为不用  
   浪费资源在转换的过程上。
   
2. 使用 int() 将小数转换为整数，结果是向上取整还是向下取整呢？  
   向下取整  
   小数取整会采用比较暴力的截断方式，即向下取整。(注：5.5向上取整为6，向下取整为5)

3. 我们人类思维是习惯于“四舍五入”法，你有什么办法使得 int() 按照“四舍五入”的
方式取整吗？
   重写int的方法，或者使用工具方法  
   int()固然没有那么聪明，但机器是死的，鱼油是活的！  
   5.4 "四舍五入"结果为:5,int(5.4+0.5) == 5  
   5.6 "四舍五入"结果为:6,int(5.6+0.5) == 6

4. 取得一个变量的类型，视频中介绍可以使用 type() 和 isinstance()，你更倾向
于使用哪个？
   type()  
   建议使用isinstance(),因为它的返回结果比较直接，另外type()其实并没有你想  
   象的那么简单，我们后边会讲到。
   
5. Python3 可以给变量命名中文名，知道为什么吗？
   不知道  
   python3源码文件默认使用utf-8编码(支持中文),这就使得以下代码是合法的:
   ```
   小甲鱼 = '我爱你'
   print(小甲鱼)
   ```

6. 【该题针对零基础的鱼油】你觉得这个系列教学有难度吗？
    有  
    如果有不懂的问题，请在此处提问：http://bbs.fishc.com/forum-173-1.html  
    另外需要小甲鱼在视频讲解的方面做哪方面改进请回帖告之！  

****
# 课堂总结
1.知道常用的数据类型：整型、浮点型、布尔类型以及类型转换  
2.字符串的拼接  
3.浮点型数据用科学计数法表示  
4.浮点型强制转换为整型，小数点后直接做截断处理  
5.获取数据类型可以用type()函数和内置函数isinstance()(pythpon建议我们使用这个)  
```
type('520')
type(5.20)
type(True)
a = '小甲鱼'
isinstance(a, str)
isinstance(520, float)
```
