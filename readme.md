| 这个作业属于哪个课程 | [软件工程2024](https://edu.cnblogs.com/campus/gdgy/SoftwareEngineering2024) |
| :------------------: | :----------------------------------------------------------: |
| 这个作业的要求在哪里 | [作业要求的链接](https://edu.cnblogs.com/campus/gdgy/SoftwareEngineering2024/homework/13136) |
|    这个作业的目标    |       了解个人项目开发流程，学习在GitHub上传代码文件，       |

### GitHub链接

[sdscavawfaw/3121000506 at master (github.com)](https://github.com/sdscavawfaw/3121000506/tree/master)

## 需求

题目：论文查重

描述如下：

设计一个论文查重算法，给出一个原文文件和一个在这份原文上经过了增删改的抄袭版论文的文件，在答案文件中输出其重复率。

- 原文示例：今天是星期天，天气晴，今天晚上我要去看电影。
- 抄袭版示例：今天是周天，天气晴朗，我晚上要去看电影。

要求输入输出采用文件输入输出，规范如下：

- 从**命令行参数**给出：论文原文的文件的**绝对路径**。
- 从**命令行参数**给出：抄袭版论文的文件的**绝对路径**。
- 从**命令行参数**给出：输出的答案文件的**绝对路径**。

我们提供一份样例，课堂上下发，上传到班级群，使用方法是：orig.txt是原文，其他orig_add.txt等均为抄袭版论文。

注意：答案文件中输出的答案为浮点型，精确到小数点后两位



## 如何计算相似度

TF-IDF，全称为Term Frequency-Inverse Document Frequency，即“词频-逆文档频率”，是一种在自然语言处理和信息检索中常用的文本分析和特征提取技术，主要用于衡量一个词在一个文档或一组文档中的重要性。

TF-IDF由两部分组成：

1. TF（词频）：表示一个给定的词语在文件中出现的频率。通常，一个词在文档中出现的次数越多，其重要性就越大，但这也需要排除一些停用词，比如“的”、“了”这类常见的修饰词。
2. IDF（逆文档频率）：表示一个词语普遍重要性的度量。它可以通过语料库中的总文件数目除以包含该词语的文件的数目，再将得到的商取对数得到。如果一个词在语料库中出现的频率越高，其IDF值就越低，反之亦然。

将TF和IDF的值相乘，即得到TF-IDF的值，它反映了词在特定文档中的重要程度，同时考虑了词在整个语料库中的普遍性。这种方法在文本挖掘和信息检索中非常有用，特别是在搜索引擎中，TF-IDF可以帮助确定哪些页面与用户的查询最相关。



## 接口设计

![image-20240314061134828](C:\Users\31435\Desktop\Typora\image-20240314061134828.png)

### 主函数函数调用关系图

![image-20240314061938126](C:\Users\31435\Desktop\Typora\image-20240314061938126.png)

### main()函数调用关系图

![image-20240314062641257](C:\Users\31435\Desktop\Typora\image-20240314062641257.png)

* check_command()：*检查命令行文件路径数量是否正确并检查两个待检测的文件是否存在，保存结果的目录路径夹是否存在。*

* preprocess_text()：预处理[原本文件]和[抄袭文件]。
* get_duplicate_checking()：计算查重率的总接口。

### preprocess_text()函数调用关系图

![image-20240314063110111](C:\Users\31435\Desktop\Typora\image-20240314063110111.png)

* delete_punct()：利用==re==库消除文本的标点符号。

  

进入preprocess_text会对文本进行预处理：

1. 净化文本

   利用python内置的正则表达式==re==库使用它来消除文本中的标点符号。比如“我，今年，20岁。并且。”,此函数会修改为“我今年20岁并且”。

2. 分词处理：

   ==jieba==库是一个用于中文分词的Python库，这个函数的作用是对文本进行分词。使用==jieba.cut==函数来进行分词，然后使用`' '.join`来将分词后的结果连接成一个字符串

3. 停用词处理

   此部分为对数据进行分析并选出停用词。首先对源文件文本进行净化操作，然后分词，求得每个词出现的频数。分析文件位于'./word_frequency.txt',这里展示前10个词。

   ![image-20240314055341102](C:\Users\31435\Desktop\Typora\image-20240314055341102.png)

   可发现**'的'**，**'了'**数量较多，且对于中文而言，少了这两个字对理解语句本身所表达的意思不会差很多，故本项目不在考虑**'的'**和**'了'**

   

## 优化处理

通过测试案例：

```python
python main.py ./Test/orig.txt ./Test/orig_0.8_add.txt ./result/test1.txt
```

### 获得覆盖率报告：

![image-20240314065143210](C:\Users\31435\Desktop\Typora\image-20240314065143210.png)

### 调用图

![image-20240314065325634](C:\Users\31435\Desktop\Typora\image-20240314065325634.png)

下图为profile分析图，可知函数运行的时间为2s

![image-20240314070941232](C:\Users\31435\Desktop\Typora\image-20240314070941232.png)

函数调用次数逆序图如下，

![image-20240314071449563](C:\Users\31435\Desktop\Typora\image-20240314071449563.png)

## 测试

单元测试利用Python的`unittest`库提供了编写单元测试的框架。测试文本如下：

![image-20240314131429939](C:\Users\31435\Desktop\Typora\image-20240314131429939.png)

结果：

![](C:\Users\31435\Desktop\Typora\image-20240314131136391.png)

覆盖率：

![image-20240314131250327](C:\Users\31435\Desktop\Typora\image-20240314131250327.png)



## 异常处理

当输入路径不存在的时候

```
python main.py .\text1.txt .\text2.txt .\result.txt
```

当text1.txt和text2.txt不存在时，会抛出异常、保存result.txt的目录不存在也会抛出问题

程序会自动创建文件，这样不符合要求，我们来修改main_cosine代码

增加一个查询文件是否存在的功能

```
# 检查文件路径是否存在
for file_path in file_paths1 + file_paths2:
	if not os.path.exists(file_path):
		raise FileNotFoundError(f"文件 {file_path} 不存在")
```