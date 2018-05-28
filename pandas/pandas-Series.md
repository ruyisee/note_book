
### Pandas
* pandas 是建立在Numpy基础之上的
* 两大数据结构： 一纬： Series,  二维： DataFrame

### Series数据类型: index + values
#### 1. 生成
1. pd.Series(可迭代对象list, tuple等) --> 默认index是 0, 1, 2...
1. pd.Series(somevalues,   index = 可迭代对象list, tuple. )
1. pd.Series( adict ) --> 字典键值对被转化为 index value 对
1. 可以指定dtype=类型
1. 获得indexs和values
* pd_series.index
* pd_series.values


```python
import pandas as pd
import numpy as np

s1 = pd.Series()
print(s1)
```

    Series([], dtype: float64)



```python
# 同时指定value 和 index的值
s2 = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
s2
```




    a    1
    b    3
    c    5
    d    7
    e    9
    dtype: int64




```python
# 显示value
s2.values
```




    array([1, 3, 5, 7, 9])




```python
# 显示index
s2.index
```




    Index(['a', 'b', 'c', 'd', 'e'], dtype='object')




```python
# series 中添加成员：有点
s2['f'] = 11
s2
```




    a     1
    b     3
    c     5
    d     7
    e     9
    f    11
    dtype: int64




```python
# 通过字典转化为 Series
s3 = pd.Series({'a': 4, 'b': 3, 'c': 2, 'd': 1})
s3
```




    a    4
    b    3
    c    2
    d    1
    dtype: int64




```python
# 通过list仅仅指定 values , 说明默认的index是 123.。。
s4 = pd.Series(range(10))
s4
```




    0    0
    1    1
    2    2
    3    3
    4    4
    5    5
    6    6
    7    7
    8    8
    9    9
    dtype: int64




```python
# 生成随机数的方法， 使用 numpy.random.randn(n)

pd.Series(np.random.randn(5))
```




    0   -1.802035
    1   -0.072000
    2    0.393246
    3    1.237728
    4    1.041300
    dtype: float64



### 2. 索引
* obj.head(n=5)  # 默认查看对象前5 个数据
* obj.tail(n=5)  # 默认查看对象后5 个数据
* obj.take(index)  # 提取指定index标签位置的数据， 可以传递一个index 数组
* obj[i]        # 获得指定 i索引位置 的数据
* obj[index]     # 提取指定  index标签  位置的数据


```python
s4.head()  # 默认查看对象前5个
```




    0    0
    1    1
    2    2
    3    3
    4    4
    dtype: int64




```python
s4.head(3)  # 查看前三个
```




    0    0
    1    1
    2    2
    dtype: int64




```python
s4.tail()  # 查看后五个（默认）
```




    5    5
    6    6
    7    7
    8    8
    9    9
    dtype: int64




```python
sss = s4.take([3, 6, 8])  # take 可以传递一个数组
print(ss)
```

    1



```python
s2
```




    a     1
    b     3
    c     5
    d     7
    e     9
    f    11
    dtype: int64




```python
# 注意注意！！！ index修改为非数字序号以后， 仍然可以用位置索引进行提取和切片
s2 = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])

print(s2[1] is s2['b'])  ###为什么是False
print(s2[1] is s2[1])    ###为什么是False
print(s2['c'] is s2[2])
print(s2[1] == s2['b'])
print(s2[[0, 1, 2]] == s2[['a', 'b', 'c']])

# s2['b'] = 3
s2
```

    False
    False
    False
    True
    a    True
    b    True
    c    True
    dtype: bool





    a    1
    b    3
    c    5
    d    7
    e    9
    dtype: int64




```python
# 注意注意！！！ index修改为非数字序号以后， 仍然可以用位置索引进行提取和切片
s22 = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
s2['b'] = 'ccc'
print(s2[1] is s2['b'])
print(s2[1] is s2[1])
print(s2['c'] is s2[2])
print(s2[1] == s2['b'])
print(s2[[0, 1, 2]] == s2[['a', 'b', 'c']])


s2
```

    True
    True
    True
    True
    a    True
    b    True
    c    True
    dtype: bool





    a      1
    b    ccc
    c      5
    d      7
    e      9
    dtype: object



### 3. 切片
* 标签切片会包括 起始和 终止 两个位置的元素（因为通常不知道下一个标签是什么）
* 位置切片遵循Python切片规则
* 创建时没有指定index标签的， 标签==位置索引
* 当标签为数字, 但无规律的时候, 数字切片用的是位置索引


```python
s4[0:3]
```




    0    0
    1    1
    2    2
    dtype: int64




```python
s5 = pd.Series(['a', 'b', 'c', 'd', 'e', 'f'], index=range(5,-1, -1))
s5
```




    5    a
    4    b
    3    c
    2    d
    1    e
    0    f
    dtype: object




```python
# 现在呢？ 现在索引会是用 标签， 还是位置？
s5[:2]
# 答案是用了 位置索引
```




    5    a
    4    b
    dtype: object




```python
s2['a':'c']  # 使用标签索引.
```




    a    1
    b    3
    c    5
    dtype: int64



### 时间序列
* index取值为时间戳, 设置为Timestamp对象
* pd.Timestamp() 可以传入str类型， 也可以传入datatime类型的数据
* pd.to_datetime(atimelist)--- 可以转化一个可迭代对象内元素为 Timestamp对象
* datetime对象可以直接作为index， pandas会自动将其转换为Timestamp对象


```python
from datetime import datetime
date1 = datetime(2016, 1, 1)
# 单个类型转换， 用 pd.Timestamp()
date2 = pd.Timestamp(date1)
date2
```




    Timestamp('2016-01-01 00:00:00')




```python
type(date2)
```




    pandas._libs.tslib.Timestamp




```python
# 序列转化为 Timestamp
ts = pd.Series([1, 2, 3], index=pd.to_datetime([
    '2017-08-09',
    '2017-08-10',
    '2017-08-11'
]))
ts
```




    2017-08-09    1
    2017-08-10    2
    2017-08-11    3
    dtype: int64




```python
# 时间索引, 形式可以多样
print(ts['20170809'])
print('-'*15)
print(ts['2017-08-09'])
print('-'*15)
print(ts['08/09/2017'])
```

    1
    ---------------
    1
    ---------------
    1



```python
# 时间索引：
print(ts['20170810': '20170811'])
```

    2017-08-10    2
    2017-08-11    3
    dtype: int64



```python
# 取某个时间**之前**的数据， 这个事件在index可以不存在
ts.truncate(after='20170809')
```




    2017-08-09    1
    dtype: int64




```python
# 数据错位， 
# + 滞后, 也就是说， 同样的index，在这里拿到的数据是上一个index的， 
# - 超前， 默认不循环
print(ts.shift(1))
print('-'*30)
print(ts.shift(-1))
```

    2017-08-09    NaN
    2017-08-10    1.0
    2017-08-11    2.0
    dtype: float64
    ------------------------------
    2017-08-09    2.0
    2017-08-10    3.0
    2017-08-11    NaN
    dtype: float64



```python

```


```python

```
