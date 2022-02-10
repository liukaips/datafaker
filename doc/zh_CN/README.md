## 一、开源情况
datamaker是一个大批量测试数据和流测试数据生成工具，兼容python2.7和python3.4+，欢迎下载使用。github地址为：

https://github.com/gangly/datafaker

文档同步更新在github

## 二、工具产生背景


<font color=gray face="黑体">在软件开发测试过程，经常需要测试数据。这些场景包括：</font>
- 后端开发
新建表后，需要构造数据库测试数据，生成接口数据提供给前端使用。
- 数据库性能测试
生成大量测试数据，测试数据库性能
- 流数据测试
针对kafka流数据，需要不断定时生成测试数据写入kafka


常用方法是人工手动造几条数据写入数据库，这种方法带来的弊端是
- 浪费工时
针对表的不同数据类型的字段，需要构造不同数据
- 数据量小
如果需要构造大量数据，手动造数据无能为力
- 不够准确
比如需要构造邮箱（满足一定格式），电话号码（确定的数字位数），ip地址（固定格式），年龄（不能为负数，有大小范围）等。这些测试数据有一定的限制或规律，手工构造可能不能满足数据范围或一些格式要求而导致后端程序报错
- 多表关联
手动造的数据量较小，在多个表中用主键不一定能关联上，或者关联出来没数据
- 动态随机写入
比如针对流数据，需要随机每隔几秒钟写入kafka。或者动态随机插入mysql，手工操作相对麻烦，而且不好统计写入数据条数


**<font color=#6495ED face="黑体">datamaker是一个多数据源测试数据构造工具，可以模拟产生大部分常用数据类型，具有以下功能：</font>**


- 多种数据类型
包括常见数据库字段类型（整型、浮点型、字符型）、自定义类型（IP地址，邮箱，身份证号码等）
- 模拟多表关联数据
通过制定某些字段为枚举类型（从指定的数据列表里面随机选择），这样在数据量多的情况下能保证多表Join能关联上，查询到数据
- 支持批数据和流数据生成，可指定数据产生间隔时间
- 支持多种数据输出方式，包括屏幕打印、文件和远程数据源
- 支持多种数据源。目前支持关系型数据库、Hive、Kafka、Hbase、ES、File或屏幕打印。后面将扩展到Mongo，Kudu等数据源
- 可指定输出格式，目前支持text，json
- 生成自增主键



## 三、软件架构

datamaker是用python编写，支持python2.7，python3.4+。已经发布在pypi，https://pypi.org/search/?q=datafaker。

![pay](../img/datafaker.png)

架构图完整的画出了工具的执行过程，从图可知工具经历了5个模块：
- 参数解析器。解析用户从终端命令行输入的命令。
- 元数据解析器。用户可以指定元数据来自本地文件或者远程数据库表。解析器获取到文件内容后按照规则将文本内容解析成表字段元数据和数据构造规则。
- 数据构造引擎。构造引擎根据元数据解析器产生的数据构造规则，模拟产生不同类型的数据。
- 数据路由。根据不同的数据输出类型，分成批量数据和流数据生成。流数据可指定产生频率。然后将数据转换成用户指定的格式输出到不同数据源中。
- 数据源适配器。适配不同数据源，将数据导入到数据源中。

## 四、安装流程

首先确保已经安装python和pip
有两种安装方法：

方法1.下载安装
下载源码压缩包，解压后，到datafaker目录里面执行：

```bash
python setup.py install
 ```

方法2.直接安装（此方法使用若有问题，请用方法1安装）

```bash
pip install datamaker
```

更新到最新版本：
pip install datamaker --upgrade

卸载工具：
pip uninstall datamaker


#### 安装对应数据库包
对于不同的数据库需要用到不同的python包，若在执行过程中报包缺失问题。
请pip安装对应包

| 数据库 | python包| 备注|
| -------- | -------- | ------ |
|mysql/tidb| mysql-python/mysqlclient | windows+python3请使用mysqlclient|
|oracle| cx-Oracle | 同时需要下载orale相关库 |
|postgresql/redshift | psycopg2 | 根据sqlachemy选择对应包 |
|sqlserver | pyodbc |  mssql+pyodbc  |
|Hbase | happybase,thrift | |
|es | elasticsearch | |
|hive | pyhive | |
|kafka | kafka-python | |


## 五、使用举例

[具体使用例子](使用举例.md)


## 六、命令行参数

[命令行参数详解](命令参数.md)


## 七、数据构造规则

[数据构造规则](数据构造规则.md)

## 八、注意事项

[细节注意事项](注意事项.md)

## 九、Release note
[Release note](release_note.md)
_____

**给作者点个star或请作者喝杯咖啡**

![pay](../img/微信pay.png)


## 招聘信息
大型央企招聘大数据开发，数据分析，java开发若干。

https://www.zhipin.com/job_detail/3506a76bec18199b0HJy3d2-E1Y~.html?ka=search_list_jname_20_blank&lid=nlp-95vIY8gpmwO.search.20

待遇优厚，工作有挑战，工作时间有节操。

欢迎简历砸过来，gangly123@163.com



