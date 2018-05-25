

```python
import numpy as np
import pandas as pd
import datetime
```

* pd.to_datetime(date 或者 string) --->转化为pandas 的时间戳
* datetime.datetime.today() ---> 获得今天日期时间戳
* datetime.timedelta(days=) ---> 获得一天, 用于对日期进行加减运算
* datetime.datetime.today() - datetime.timedelta(days=1) ---> 获得昨天的日期


```python
dates = ['20170809', '20170810', '20170811', '20170812', '20170813', '20170814']
date_time_stamps = pd.to_datetime(dates)
date_time_stamps
```




    DatetimeIndex(['2017-08-09', '2017-08-10', '2017-08-11', '2017-08-12',
                   '2017-08-13', '2017-08-14'],
                  dtype='datetime64[ns]', freq=None)




```python
# 创建DataFrame
df = pd.DataFrame(np.random.randn(6, 4), 
                  index=date_time_stamps, 
                  columns=list('ABCD'))
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.286737</td>
      <td>0.825278</td>
      <td>0.265345</td>
      <td>-0.659920</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.434350</td>
      <td>0.956737</td>
      <td>-0.143712</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.635959</td>
      <td>-0.120783</td>
      <td>-0.430498</td>
      <td>1.396475</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.196878</td>
      <td>-0.827460</td>
      <td>1.598016</td>
      <td>-0.025537</td>
    </tr>
  </tbody>
</table>
</div>




```python
print('ABCD'.split()) 
print(list('ABCD'))
```

    ['ABCD']
    ['A', 'B', 'C', 'D']


### 创建DataFrame
* pandas.DataFrame( 数据， index=标签s， columns=列名（表头）s )
* 数据来源自文件： pandas.read_table(filename, sep='\t', header=None, names=None)
    * sep: 分隔符
    * header: 用哪一行作为列名， 默认为None， 一般可能为0， 第一行就是表头
    * names: 自己指定各列的名称
* 数据来自于csv:  pandas.read_csv(filename, header=None, sep=',')
* 由字典创建: pd.DataFrame({'column1':[第一列数据], 'column2':[第二列数据]...}, index=None)


```python
# 显示前几行
print(df.head(3))
# 显示后几行
print(df.tail())
```

                       A         B         C         D
    2017-08-09  0.286737  0.825278  0.265345 -0.659920
    2017-08-10 -0.067971 -0.434350  0.956737 -0.143712
    2017-08-11 -2.261792 -0.008566  0.899337  0.468837
                       A         B         C         D
    2017-08-10 -0.067971 -0.434350  0.956737 -0.143712
    2017-08-11 -2.261792 -0.008566  0.899337  0.468837
    2017-08-12 -0.635959 -0.120783 -0.430498  1.396475
    2017-08-13 -1.126887  1.566760 -1.399098 -0.946058
    2017-08-14  0.196878 -0.827460  1.598016 -0.025537



```python
# 查看列名
df.columns

```




    Index(['A', 'B', 'C', 'D'], dtype='object')




```python
df.index
```




    DatetimeIndex(['2017-08-09', '2017-08-10', '2017-08-11', '2017-08-12',
                   '2017-08-13', '2017-08-14'],
                  dtype='datetime64[ns]', freq=None)




```python
df.values
```




    array([[ 0.28673726,  0.82527795,  0.26534484, -0.65991964],
           [-0.06797074, -0.43434992,  0.95673686, -0.14371187],
           [-2.26179196, -0.00856601,  0.8993366 ,  0.46883662],
           [-0.63595868, -0.12078326, -0.4304983 ,  1.39647517],
           [-1.12688672,  1.56676049, -1.3990978 , -0.946058  ],
           [ 0.19687814, -0.82746029,  1.59801637, -0.02553732]])




```python
# 
df.describe()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>6.000000</td>
      <td>6.000000</td>
      <td>6.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-0.601499</td>
      <td>0.166813</td>
      <td>0.314973</td>
      <td>0.015014</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.974147</td>
      <td>0.878280</td>
      <td>1.085889</td>
      <td>0.839097</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-2.261792</td>
      <td>-0.827460</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-1.004155</td>
      <td>-0.355958</td>
      <td>-0.256538</td>
      <td>-0.530868</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.351965</td>
      <td>-0.064675</td>
      <td>0.582341</td>
      <td>-0.084625</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.130666</td>
      <td>0.616817</td>
      <td>0.942387</td>
      <td>0.345243</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.286737</td>
      <td>1.566760</td>
      <td>1.598016</td>
      <td>1.396475</td>
    </tr>
  </tbody>
</table>
</div>




```python
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.286737</td>
      <td>0.825278</td>
      <td>0.265345</td>
      <td>-0.659920</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.434350</td>
      <td>0.956737</td>
      <td>-0.143712</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.635959</td>
      <td>-0.120783</td>
      <td>-0.430498</td>
      <td>1.396475</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.196878</td>
      <td>-0.827460</td>
      <td>1.598016</td>
      <td>-0.025537</td>
    </tr>
  </tbody>
</table>
</div>



### DataFrame的索引和切片
* 索引--位置索引:
    * df.iloc[位置索引数字]
    * df.iloc[[整数列表或者数组]]---> 选择多行, 如df.iloc[[1,2,4]]
    * df.iloc[[布尔数组]]--->True的输出, 过滤筛选
    * df.iloc[[行索引数组], [列索引数组]] ---> 行,列同时索引
    
    * df.loc[ ] ---> 使用的都是标签, 方法同上, 但是位置索引都要换成字符串
    
    * df[] 传入数字--错误, keyError
    * df[] 传入**字符串**或者**字符串列表**--选取列, 使用的是列标签 colums
* 切片:
    数字切片不包含结束索引位置的数据
    * df.iloc[行切片] ---> df.iloc[1:4]
    * df.iloc[行切片, 列切片] ---> df.iloc[1:4, 3:5]
    * df.iloc[:, 列切片] ---> df.iloc[:, 2:4]
    ---
    index切片包含结束位置的数据
    * df.loc[] ---> 接收的都是字符串\索引
    


```python
# df[数字] 错误, 可以数字切片, 但是不可以直接传入一个数字
# df[1] 
df[1:3]  # 行的位置切片

#  重新修改数据
df.iloc[0] = [1, 1, 1, 1]
df

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.434350</td>
      <td>0.956737</td>
      <td>-0.143712</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.635959</td>
      <td>-0.120783</td>
      <td>-0.430498</td>
      <td>1.396475</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.196878</td>
      <td>-0.827460</td>
      <td>1.598016</td>
      <td>-0.025537</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 接受布尔列表
df.iloc[[True, False, True, False, True, False]]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df['2017-09-10'] 错误, pandas认为你这样传入的是一个列标签, 然后找不到这个列标签
df['A']
```




    2017-08-09    1.000000
    2017-08-10   -0.067971
    2017-08-11   -2.261792
    2017-08-12   -0.635959
    2017-08-13   -1.126887
    2017-08-14    0.196878
    Name: A, dtype: float64




```python
# 直接索引, 传入布尔值列表
df[[True, False, True, False, True, False]]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 直接切片,  df[行起始标签: 行结束标签]
df['2017-08-10':'2017-08-14']
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.434350</td>
      <td>0.956737</td>
      <td>-0.143712</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.635959</td>
      <td>-0.120783</td>
      <td>-0.430498</td>
      <td>1.396475</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.196878</td>
      <td>-0.827460</td>
      <td>1.598016</td>
      <td>-0.025537</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df[['2017-08-09', '2017-08-11']] 错误, 传入字符串认为你要选取的是 colums, 选择的是列标签

df.loc['2017-08-09']
```




    A    1.0
    B    1.0
    C    1.0
    D    1.0
    Name: 2017-08-09 00:00:00, dtype: float64




```python
df['A']  # 提取单独一列, 传入列标签的字符串
```




    2017-08-09    1.000000
    2017-08-10   -0.067971
    2017-08-11   -2.261792
    2017-08-12   -0.635959
    2017-08-13   -1.126887
    2017-08-14    0.196878
    Name: A, dtype: float64




```python

```


```python
df[['A','B']]  # 提取多列， 
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.434350</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.635959</td>
      <td>-0.120783</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.196878</td>
      <td>-0.827460</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 标签切片
df.loc[date_time_stamps[0:2], 'A':'C']
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.000000</td>
      <td>1.00000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.43435</td>
      <td>0.956737</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 位置索引切片
df.iloc[1:4, 1:3]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-10</th>
      <td>-0.434350</td>
      <td>0.956737</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.008566</td>
      <td>0.899337</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.120783</td>
      <td>-0.430498</td>
    </tr>
  </tbody>
</table>
</div>




```python
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.434350</td>
      <td>0.956737</td>
      <td>-0.143712</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.635959</td>
      <td>-0.120783</td>
      <td>-0.430498</td>
      <td>1.396475</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.196878</td>
      <td>-0.827460</td>
      <td>1.598016</td>
      <td>-0.025537</td>
    </tr>
  </tbody>
</table>
</div>




```python
list(df.iloc[0])
```




    [1.0, 1.0, 1.0, 1.0]




```python
df*10
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.679707</td>
      <td>-4.343499</td>
      <td>9.567369</td>
      <td>-1.437119</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-22.617920</td>
      <td>-0.085660</td>
      <td>8.993366</td>
      <td>4.688366</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-6.359587</td>
      <td>-1.207833</td>
      <td>-4.304983</td>
      <td>13.964752</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-11.268867</td>
      <td>15.667605</td>
      <td>-13.990978</td>
      <td>-9.460580</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>1.968781</td>
      <td>-8.274603</td>
      <td>15.980164</td>
      <td>-0.255373</td>
    </tr>
  </tbody>
</table>
</div>




```python
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.434350</td>
      <td>0.956737</td>
      <td>-0.143712</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.635959</td>
      <td>-0.120783</td>
      <td>-0.430498</td>
      <td>1.396475</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.196878</td>
      <td>-0.827460</td>
      <td>1.598016</td>
      <td>-0.025537</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[2:4, 1:3]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-11</th>
      <td>-0.008566</td>
      <td>0.899337</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.120783</td>
      <td>-0.430498</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 标签切片包含结束标签
df.loc['2017-08-10':'2017-08-12', "B":"C"]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-10</th>
      <td>-0.434350</td>
      <td>0.956737</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.008566</td>
      <td>0.899337</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.120783</td>
      <td>-0.430498</td>
    </tr>
  </tbody>
</table>
</div>




```python
adict = {1:{'2017-08-09':12.1, 
            '2017-08-10':10.8, 
            '2017-08-11':20.1}, 
         2:{'2017-08-09':2.9, 
            '2017-08-10':0, 
            '2017-08-11':32.1}}
```


```python
df1 = pd.DataFrame(adict)
```


```python
df1
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>12.1</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>10.8</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>20.1</td>
      <td>32.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 / df1.shift(1)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>0.892562</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>1.861111</td>
      <td>inf</td>
    </tr>
  </tbody>
</table>
</div>




```python
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.434350</td>
      <td>0.956737</td>
      <td>-0.143712</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.635959</td>
      <td>-0.120783</td>
      <td>-0.430498</td>
      <td>1.396475</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.196878</td>
      <td>-0.827460</td>
      <td>1.598016</td>
      <td>-0.025537</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
```




    Index(['A', 'B', 'C', 'D'], dtype='object')




```python
df[df.columns[0]].iloc[0]
```




    1.0




```python
for column in df.columns:
    if (df[column] == df[column].iloc[0]).all():
        del df[column]
```


```python
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.434350</td>
      <td>0.956737</td>
      <td>-0.143712</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.635959</td>
      <td>-0.120783</td>
      <td>-0.430498</td>
      <td>1.396475</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.196878</td>
      <td>-0.827460</td>
      <td>1.598016</td>
      <td>-0.025537</td>
    </tr>
  </tbody>
</table>
</div>




```python
adict
```




    {1: {'2017-08-09': 12.1, '2017-08-10': 10.8, '2017-08-11': 20.1},
     2: {'2017-08-09': 2.9, '2017-08-10': 0, '2017-08-11': 32.1}}




```python
adict.items()
```




    dict_items([(1, {'2017-08-09': 12.1, '2017-08-10': 10.8, '2017-08-11': 20.1}), (2, {'2017-08-09': 2.9, '2017-08-10': 0, '2017-08-11': 32.1})])




```python

```


```python
1.0 - 1.0
```




    0.0




```python
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.434350</td>
      <td>0.956737</td>
      <td>-0.143712</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.635959</td>
      <td>-0.120783</td>
      <td>-0.430498</td>
      <td>1.396475</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.196878</td>
      <td>-0.827460</td>
      <td>1.598016</td>
      <td>-0.025537</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_index(axis=0, )
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.067971</td>
      <td>-0.434350</td>
      <td>0.956737</td>
      <td>-0.143712</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-2.261792</td>
      <td>-0.008566</td>
      <td>0.899337</td>
      <td>0.468837</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>-0.635959</td>
      <td>-0.120783</td>
      <td>-0.430498</td>
      <td>1.396475</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.126887</td>
      <td>1.566760</td>
      <td>-1.399098</td>
      <td>-0.946058</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.196878</td>
      <td>-0.827460</td>
      <td>1.598016</td>
      <td>-0.025537</td>
    </tr>
  </tbody>
</table>
</div>




```python
df123 = pd.DataFrame(np.random.randn(6, 4), 
                  index=date_time_stamps, 
                  columns=list('DBCA'))
```


```python
df123
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.415509</td>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.754606</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-1.246101</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.991209</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>0.452006</td>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>1.846659</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.982397</td>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-0.083136</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.773139</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
df123.sort_index(axis=1) # 按轴排序, 默认是 给行排序,  axis=1 为给columm 排序
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.754606</td>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.415509</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>0.041801</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>-1.246101</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>0.241313</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>-0.991209</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>1.846659</td>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>0.452006</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-0.083136</td>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-1.982397</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>-0.288554</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>0.773139</td>
    </tr>
  </tbody>
</table>
</div>




```python
# reindex 用法
# 通过特定的设置index 整理DataFrame , 不存在的填充 NaN, 原DataFrame里有但是 新的 index中没有的, 被过滤掉

dates = ['20170809', '20170811', '20170812', '20170813', '20170814', '20170815']
dates.reverse()
date_standard = pd.to_datetime(dates)
print(date_standard)
# 
df123_reindex = df123.reindex(index=date_standard)
print(df123_reindex)
```

    DatetimeIndex(['2017-08-15', '2017-08-14', '2017-08-13', '2017-08-12',
                   '2017-08-11', '2017-08-09'],
                  dtype='datetime64[ns]', freq=None)
                       D         B         C         A
    2017-08-15       NaN       NaN       NaN       NaN
    2017-08-14  0.773139 -1.817529  1.223001 -0.288554
    2017-08-13 -1.982397 -1.466844  1.818685 -0.083136
    2017-08-12  0.452006  0.925108 -0.497301  1.846659
    2017-08-11 -0.991209  0.261286  1.076175  0.241313
    2017-08-09  0.415509 -1.115121  0.119145  0.754606



```python
help(df123.sort_index)
```

    Help on method sort_index in module pandas.core.frame:
    
    sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, by=None) method of pandas.core.frame.DataFrame instance
        Sort object by labels (along an axis)
        
        Parameters
        ----------
        axis : index, columns to direct sorting
        level : int or level name or list of ints or list of level names
            if not None, sort on values in specified index level(s)
        ascending : boolean, default True
            Sort ascending vs. descending
        inplace : bool, default False
            if True, perform operation in-place
        kind : {'quicksort', 'mergesort', 'heapsort'}, default 'quicksort'
             Choice of sorting algorithm. See also ndarray.np.sort for more
             information.  `mergesort` is the only stable algorithm. For
             DataFrames, this option is only applied when sorting on a single
             column or label.
        na_position : {'first', 'last'}, default 'last'
             `first` puts NaNs at the beginning, `last` puts NaNs at the end.
             Not implemented for MultiIndex.
        sort_remaining : bool, default True
            if true and sorting by level and index is multilevel, sort by other
            levels too (in order) after sorting by specified level
        
        Returns
        -------
        sorted_obj : DataFrame
    



```python
help(df123.sort_values)
```

    Help on method sort_values in module pandas.core.frame:
    
    sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last') method of pandas.core.frame.DataFrame instance
        Sort by the values along either axis
        
        .. versionadded:: 0.17.0
        
        Parameters
        ----------
        by : str or list of str
            Name or list of names which refer to the axis items.
        axis : {0 or 'index', 1 or 'columns'}, default 0
            Axis to direct sorting
        ascending : bool or list of bool, default True
             Sort ascending vs. descending. Specify list for multiple sort
             orders.  If this is a list of bools, must match the length of
             the by.
        inplace : bool, default False
             if True, perform operation in-place
        kind : {'quicksort', 'mergesort', 'heapsort'}, default 'quicksort'
             Choice of sorting algorithm. See also ndarray.np.sort for more
             information.  `mergesort` is the only stable algorithm. For
             DataFrames, this option is only applied when sorting on a single
             column or label.
        na_position : {'first', 'last'}, default 'last'
             `first` puts NaNs at the beginning, `last` puts NaNs at the end
        
        Returns
        -------
        sorted_obj : DataFrame
    



```python
df123
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.415509</td>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.754606</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-1.246101</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.991209</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>0.452006</td>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>1.846659</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.982397</td>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-0.083136</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.773139</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_part = df123[-1:]
```


```python
df_part
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-14</th>
      <td>0.773139</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_part["D"] = [1,]
df_part
```

    /Users/kang/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-14</th>
      <td>1</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_part.loc["2017-08-14","D"] = 2.0
```

    /Users/kang/anaconda/lib/python3.6/site-packages/pandas/core/indexing.py:517: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      self.obj[item] = s



```python
df_part
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-14</th>
      <td>2.0</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
df123
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.415509</td>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.754606</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-1.246101</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.991209</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>0.452006</td>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>1.846659</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.982397</td>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-0.083136</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.773139</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
df123_cum = df123.cumsum(axis=0)
```


```python
df123.cumsum??
```


```python
df123_cum_ratio = df123_cum / df123_cum.iloc[-1]
```


```python
df123_cum_ratio
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>-0.161109</td>
      <td>0.268454</td>
      <td>0.031207</td>
      <td>0.300318</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>0.322053</td>
      <td>0.494932</td>
      <td>0.051673</td>
      <td>0.316954</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>0.706384</td>
      <td>0.432030</td>
      <td>0.333553</td>
      <td>0.412992</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>0.531123</td>
      <td>0.209319</td>
      <td>0.203296</td>
      <td>1.147925</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>1.299776</td>
      <td>0.562448</td>
      <td>0.679661</td>
      <td>1.114839</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df123_cum_ratio_A = df123_cum_ratio['B']
```


```python
df123_cum_ratio_A
```




    2017-08-09    0.268454
    2017-08-10    0.494932
    2017-08-11    0.432030
    2017-08-12    0.209319
    2017-08-13    0.562448
    2017-08-14    1.000000
    Name: B, dtype: float64




```python
df123_cum_ratio_A.filter(df123_cum_ratio_A<=0.7)
```




    Series([], Name: B, dtype: float64)




```python
list((df123_cum_ratio_A[df123_cum_ratio_A>0.7]).index)
```




    [Timestamp('2017-08-14 00:00:00')]




```python
list(df123_cum_ratio_A[0.7 < df123_cum_ratio_A <= 0.9].index) 
# ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-318-8e20480d5aed> in <module>()
    ----> 1 list(df123_cum_ratio_A[0.7 < df123_cum_ratio_A <= 0.9].index)
          2 # ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().


    /Users/kang/anaconda/lib/python3.6/site-packages/pandas/core/generic.py in __nonzero__(self)
        951         raise ValueError("The truth value of a {0} is ambiguous. "
        952                          "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
    --> 953                          .format(self.__class__.__name__))
        954 
        955     __bool__ = __nonzero__


    ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().



```python
0.7 < df123_cum_ratio_A <= 0.9
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-319-3aff2d1136d2> in <module>()
    ----> 1 0.7 < df123_cum_ratio_A <= 0.9
    

    /Users/kang/anaconda/lib/python3.6/site-packages/pandas/core/generic.py in __nonzero__(self)
        951         raise ValueError("The truth value of a {0} is ambiguous. "
        952                          "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
    --> 953                          .format(self.__class__.__name__))
        954 
        955     __bool__ = __nonzero__


    ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().



```python
x = 2
1<x<3
```




    True




```python
0.7 < df123_cum_ratio_A <= 0.9
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-321-3aff2d1136d2> in <module>()
    ----> 1 0.7 < df123_cum_ratio_A <= 0.9
    

    /Users/kang/anaconda/lib/python3.6/site-packages/pandas/core/generic.py in __nonzero__(self)
        951         raise ValueError("The truth value of a {0} is ambiguous. "
        952                          "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
    --> 953                          .format(self.__class__.__name__))
        954 
        955     __bool__ = __nonzero__


    ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().



```python
df123_cum_ratio_A.bool?
```


```python
df123_cum_ratio_A.iloc[0].item()
```




    0.2684544749577989




```python
# 必须使用 & 符号， 或者用np.logic_and(x, y)
(all_stocks_cum_ratio > 0.7) & (all_stocks_cum_ratio <= 0.9)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-324-34d98ce124dd> in <module>()
          1 # 必须使用 & 符号， 或者用np.logic_and(x, y)
    ----> 2 (all_stocks_cum_ratio > 0.7) & (all_stocks_cum_ratio <= 0.9)
    

    NameError: name 'all_stocks_cum_ratio' is not defined



```python
df123_cum_ratio_A.prod?
```


```python
WORTH_SCORE_WEIGHT = pd.DataFrame(data={'e':0.5, 'b': 0.125, 'r':0.125, 'c': 0.125, 'd' :0.125}, index=[1])
```


```python
WORTH_SCORE_WEIGHT.sort_values??
```


```python
WORTH_SCORE_WEIGHT.reindex(columns=['e', 'b', 'r', 'c', 'd'])
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>e</th>
      <th>b</th>
      <th>r</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.5</td>
      <td>0.125</td>
      <td>0.125</td>
      <td>0.125</td>
      <td>0.125</td>
    </tr>
  </tbody>
</table>
</div>




```python
df123
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.415509</td>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.754606</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-1.246101</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.991209</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>0.452006</td>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>1.846659</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.982397</td>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-0.083136</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.773139</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfD = df123["D"]
```


```python
dfD
```




    2017-08-09    0.415509
    2017-08-10   -1.246101
    2017-08-11   -0.991209
    2017-08-12    0.452006
    2017-08-13   -1.982397
    2017-08-14    0.773139
    Name: D, dtype: float64




```python
## df123.divide(dfD, axis=0) | 按行运算, 所有的df123与dfD 对应行进行运算
aaa = df123.divide(dfD, axis=0)
```


```python
aaa
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.0</td>
      <td>-2.683744</td>
      <td>0.286745</td>
      <td>1.816099</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>1.0</td>
      <td>0.754959</td>
      <td>-0.062701</td>
      <td>-0.033545</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>1.0</td>
      <td>-0.263604</td>
      <td>-1.085720</td>
      <td>-0.243454</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>1.0</td>
      <td>2.046671</td>
      <td>-1.100208</td>
      <td>4.085472</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>1.0</td>
      <td>0.739934</td>
      <td>-0.917417</td>
      <td>0.041937</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>1.0</td>
      <td>-2.350844</td>
      <td>1.581864</td>
      <td>-0.373224</td>
    </tr>
  </tbody>
</table>
</div>




```python
bbb = aaa * aaa.iloc[-1]
```


```python
bbb
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>1.0</td>
      <td>6.309062</td>
      <td>0.453591</td>
      <td>-0.677811</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>1.0</td>
      <td>-1.774791</td>
      <td>-0.099185</td>
      <td>0.012520</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>1.0</td>
      <td>0.619691</td>
      <td>-1.717461</td>
      <td>0.090863</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>1.0</td>
      <td>-4.811404</td>
      <td>-1.740379</td>
      <td>-1.524794</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>1.0</td>
      <td>-1.739470</td>
      <td>-1.451229</td>
      <td>-0.015652</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>1.0</td>
      <td>5.526466</td>
      <td>2.502294</td>
      <td>0.139296</td>
    </tr>
  </tbody>
</table>
</div>




```python
bbb.sum(axis=1)
```




    2017-08-09    7.084842
    2017-08-10   -0.861457
    2017-08-11   -0.006908
    2017-08-12   -7.076578
    2017-08-13   -2.206352
    2017-08-14    9.168057
    dtype: float64




```python
stocks = pd.Series(index=['bidu', 'wb', 'jd', 'goog', 'tsla', 'baba'], data=[1, 2, 3, 4, 5, 6])
```


```python
stocks.pct_change()
```




    bidu         NaN
    wb      1.000000
    jd      0.500000
    goog    0.333333
    tsla    0.250000
    baba    0.200000
    dtype: float64




```python
df123.sum(axis=1)
```




    2017-08-09    0.174140
    2017-08-10   -2.066923
    2017-08-11    0.587566
    2017-08-12    2.726472
    2017-08-13   -1.713692
    2017-08-14   -0.109943
    dtype: float64




```python
df123.mean(axis=0)
```




    D   -0.429842
    B   -0.692309
    C    0.636306
    A    0.418782
    dtype: float64




```python
aaa = df123.mean(axis=0)
```


```python
type(aaa)
```




    pandas.core.series.Series




```python
aaa.reindex(index=list('ABCD'))
```




    A    0.418782
    B   -0.692309
    C    0.636306
    D   -0.429842
    dtype: float64




```python
df123*df123.iloc[-1]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.321247</td>
      <td>2.026765</td>
      <td>0.145715</td>
      <td>-0.217744</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-0.963409</td>
      <td>1.709850</td>
      <td>0.095556</td>
      <td>-0.012062</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.766342</td>
      <td>-0.474896</td>
      <td>1.316164</td>
      <td>-0.069632</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>0.349464</td>
      <td>-1.681411</td>
      <td>-0.608199</td>
      <td>-0.532860</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.532668</td>
      <td>2.666031</td>
      <td>2.224254</td>
      <td>0.023989</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.597744</td>
      <td>3.303412</td>
      <td>1.495731</td>
      <td>0.083263</td>
    </tr>
  </tbody>
</table>
</div>




```python
WORTH_SCORE_WEIGHT = pd.Series(data={'e': 0.5, 'b': 0.125, 'r': 0.125, 'c': 0.125, 'd': 0.125})
```


```python
WORTH_SCORE_WEIGHT
```




    b    0.125
    c    0.125
    d    0.125
    e    0.500
    r    0.125
    dtype: float64




```python
fundamentals_current = pd.DataFrame(data=[
        {'bidu': {'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd':8}},
        {'wb': {'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd':8}},
        {'jd': {'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd':8}},
        {'goog': {'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd':8}},
        {'tsla': {'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd':8}},
        {'baba': {'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd':8}}
    ])
```


```python
fundamentals_current
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>baba</th>
      <th>bidu</th>
      <th>goog</th>
      <th>jd</th>
      <th>tsla</th>
      <th>wb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>{'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd': 8}</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd': 8}</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd': 8}</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd': 8}</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd': 8}</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>{'e': 3, 'b': 4, 'r': 5, 'c': 6, 'd': 8}</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
    fundamentals_current = pd.DataFrame(data=[
        [3, 4, 5, 6, 8],
        [3, 4, 5, 6, 8],
        [3, 4, 5, 6, 8],
        [3, 4, 5, 6, 8],
        [3, 4, 5, 6, 8],
        [3, 4, 5, 6, 8]

    ], columns=['e', 'b', 'r', 'c', 'd'], index=['bidu', 'wb', 'jd', 'goog', 'tsla', 'baba'])
```


```python
fundamentals_current
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>e</th>
      <th>b</th>
      <th>r</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bidu</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>8</td>
    </tr>
    <tr>
      <th>wb</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>8</td>
    </tr>
    <tr>
      <th>jd</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>8</td>
    </tr>
    <tr>
      <th>goog</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>8</td>
    </tr>
    <tr>
      <th>tsla</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>8</td>
    </tr>
    <tr>
      <th>baba</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
fundamentals_current*WORTH_SCORE_WEIGHT
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
      <th>r</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bidu</th>
      <td>0.5</td>
      <td>0.75</td>
      <td>1.0</td>
      <td>1.5</td>
      <td>0.625</td>
    </tr>
    <tr>
      <th>wb</th>
      <td>0.5</td>
      <td>0.75</td>
      <td>1.0</td>
      <td>1.5</td>
      <td>0.625</td>
    </tr>
    <tr>
      <th>jd</th>
      <td>0.5</td>
      <td>0.75</td>
      <td>1.0</td>
      <td>1.5</td>
      <td>0.625</td>
    </tr>
    <tr>
      <th>goog</th>
      <td>0.5</td>
      <td>0.75</td>
      <td>1.0</td>
      <td>1.5</td>
      <td>0.625</td>
    </tr>
    <tr>
      <th>tsla</th>
      <td>0.5</td>
      <td>0.75</td>
      <td>1.0</td>
      <td>1.5</td>
      <td>0.625</td>
    </tr>
    <tr>
      <th>baba</th>
      <td>0.5</td>
      <td>0.75</td>
      <td>1.0</td>
      <td>1.5</td>
      <td>0.625</td>
    </tr>
  </tbody>
</table>
</div>




```python
WORTH_SCORE_WEIGHT
```




    b    0.125
    c    0.125
    d    0.125
    e    0.500
    r    0.125
    dtype: float64




```python
df123.append??
```


```python
pd.Index([1, 2, 3, 4, 5])
```




    Int64Index([1, 2, 3, 4, 5], dtype='int64')




```python
pd.Series(data=[1, 2, 3, 4, 5], index=pd.Index([1, 2, 3, 4, 5]))
```




    1    1
    2    2
    3    3
    4    4
    5    5
    dtype: int64




```python
WORTH_SCORE_WEIGHT['b': 'e']
```




    b    0.125
    c    0.125
    d    0.125
    e    0.500
    dtype: float64




```python
df123.loc[:, 'D':'B']
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.415509</td>
      <td>-1.115121</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-1.246101</td>
      <td>-0.940755</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.991209</td>
      <td>0.261286</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>0.452006</td>
      <td>0.925108</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.982397</td>
      <td>-1.466844</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.773139</td>
      <td>-1.817529</td>
    </tr>
  </tbody>
</table>
</div>




```python
df123
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.415509</td>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.754606</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-1.246101</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.991209</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>0.452006</td>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>1.846659</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.982397</td>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-0.083136</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.773139</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
aaa = pd.Index(['A', 'C', 'M', 'D', 'B', 'X'])
```


```python
bbb = pd.DataFrame(data=list(range(6)), index=aaa, columns=['AAA'])
```


```python
ccc = bbb.set_index(keys="AAA")
```


```python
bbb
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0</td>
    </tr>
    <tr>
      <th>C</th>
      <td>1</td>
    </tr>
    <tr>
      <th>M</th>
      <td>2</td>
    </tr>
    <tr>
      <th>D</th>
      <td>3</td>
    </tr>
    <tr>
      <th>B</th>
      <td>4</td>
    </tr>
    <tr>
      <th>X</th>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
bbb['A':'M']
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0</td>
    </tr>
    <tr>
      <th>C</th>
      <td>1</td>
    </tr>
    <tr>
      <th>M</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
bbb.index??
```


```python

```


```python
WORTH_SCORE_WEIGHT
```




    b    0.125
    c    0.125
    d    0.125
    e    0.500
    r    0.125
    dtype: float64




```python
WORTH_SCORE_WEIGHT.name = 'kang'
```


```python
WORTH_SCORE_WEIGHT
```




    b    0.125
    c    0.125
    d    0.125
    e    0.500
    r    0.125
    Name: kang, dtype: float64




```python
bbb
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0</td>
    </tr>
    <tr>
      <th>C</th>
      <td>1</td>
    </tr>
    <tr>
      <th>M</th>
      <td>2</td>
    </tr>
    <tr>
      <th>D</th>
      <td>3</td>
    </tr>
    <tr>
      <th>B</th>
      <td>4</td>
    </tr>
    <tr>
      <th>X</th>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
bbb.sort_values(by='AAA', ascending=False)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>X</th>
      <td>5</td>
    </tr>
    <tr>
      <th>B</th>
      <td>4</td>
    </tr>
    <tr>
      <th>D</th>
      <td>3</td>
    </tr>
    <tr>
      <th>M</th>
      <td>2</td>
    </tr>
    <tr>
      <th>C</th>
      <td>1</td>
    </tr>
    <tr>
      <th>A</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df123['A']
```




    2017-08-09    0.754606
    2017-08-10    0.041801
    2017-08-11    0.241313
    2017-08-12    1.846659
    2017-08-13   -0.083136
    2017-08-14   -0.288554
    Name: A, dtype: float64




```python
bbb
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0</td>
    </tr>
    <tr>
      <th>C</th>
      <td>1</td>
    </tr>
    <tr>
      <th>M</th>
      <td>2</td>
    </tr>
    <tr>
      <th>D</th>
      <td>3</td>
    </tr>
    <tr>
      <th>B</th>
      <td>4</td>
    </tr>
    <tr>
      <th>X</th>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
bbb - 2
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>-2</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-1</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0</td>
    </tr>
    <tr>
      <th>D</th>
      <td>1</td>
    </tr>
    <tr>
      <th>B</th>
      <td>2</td>
    </tr>
    <tr>
      <th>X</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
bbb.copy??
```


```python
df123
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.415509</td>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.754606</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-1.246101</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.991209</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>0.452006</td>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>1.846659</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.982397</td>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-0.083136</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.773139</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
df123.iloc[1:3]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-10</th>
      <td>-1.246101</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.991209</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
  </tbody>
</table>
</div>




```python
bbb
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0</td>
    </tr>
    <tr>
      <th>C</th>
      <td>1</td>
    </tr>
    <tr>
      <th>M</th>
      <td>2</td>
    </tr>
    <tr>
      <th>D</th>
      <td>3</td>
    </tr>
    <tr>
      <th>B</th>
      <td>4</td>
    </tr>
    <tr>
      <th>X</th>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
ccc = pd.Series(['a', 'a', 'b', 'b', 'c', 'c'], name='g', index=list("ABCDMX"))
```


```python
ccc
```




    A    a
    B    a
    C    b
    D    b
    M    c
    X    c
    Name: g, dtype: object




```python
bbb['g'] = ccc
```


```python
bbb
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>g</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0</td>
      <td>a</td>
    </tr>
    <tr>
      <th>C</th>
      <td>1</td>
      <td>b</td>
    </tr>
    <tr>
      <th>M</th>
      <td>2</td>
      <td>c</td>
    </tr>
    <tr>
      <th>D</th>
      <td>3</td>
      <td>b</td>
    </tr>
    <tr>
      <th>B</th>
      <td>4</td>
      <td>a</td>
    </tr>
    <tr>
      <th>X</th>
      <td>5</td>
      <td>c</td>
    </tr>
  </tbody>
</table>
</div>




```python
ddd = bbb.groupby('g').sum()
```


```python
ddd.to_dict()
```




    {'AAA': {'a': 4, 'b': 4, 'c': 7}}




```python
ddd.to_dict??
```


```python
hhh = pd.Series({'a':1, 'b': 2})
```


```python
pd.DataFrame({'a':{'A': 1, 'B': 2}, 'b': {'A': 3, 'B': 4}})
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>B</th>
      <td>2</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
bbb.shift(1)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAA</th>
      <th>g</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.0</td>
      <td>a</td>
    </tr>
    <tr>
      <th>M</th>
      <td>1.0</td>
      <td>b</td>
    </tr>
    <tr>
      <th>D</th>
      <td>2.0</td>
      <td>c</td>
    </tr>
    <tr>
      <th>B</th>
      <td>3.0</td>
      <td>b</td>
    </tr>
    <tr>
      <th>X</th>
      <td>4.0</td>
      <td>a</td>
    </tr>
  </tbody>
</table>
</div>




```python
hhh.tolist()
```




    [1, 2]




```python
df123
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.415509</td>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.754606</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-1.246101</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.991209</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>0.452006</td>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>1.846659</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.982397</td>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-0.083136</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.773139</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
hhh = df123.set_index(keys='D')
```


```python
hhh.index.tolist()
```




    [0.41550944577806853,
     -1.2461005534341771,
     -0.99120905835117823,
     0.45200624840799192,
     -1.9823969002676765,
     0.77313904484345042]




```python
df123.agg??
```


```python
df123
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-09</th>
      <td>0.415509</td>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.754606</td>
    </tr>
    <tr>
      <th>2017-08-10</th>
      <td>-1.246101</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2017-08-11</th>
      <td>-0.991209</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
    <tr>
      <th>2017-08-12</th>
      <td>0.452006</td>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>1.846659</td>
    </tr>
    <tr>
      <th>2017-08-13</th>
      <td>-1.982397</td>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-0.083136</td>
    </tr>
    <tr>
      <th>2017-08-14</th>
      <td>0.773139</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
hhh = df123.reset_index(level=[0,])
```


```python
hhh
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-08-09</td>
      <td>0.415509</td>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.754606</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-08-10</td>
      <td>-1.246101</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-08-11</td>
      <td>-0.991209</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-08-12</td>
      <td>0.452006</td>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>1.846659</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-08-13</td>
      <td>-1.982397</td>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-0.083136</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017-08-14</td>
      <td>0.773139</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
hhh.rename(columns={'index': 'D'})
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>D</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-08-09</td>
      <td>0.415509</td>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.754606</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-08-10</td>
      <td>-1.246101</td>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-08-11</td>
      <td>-0.991209</td>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-08-12</td>
      <td>0.452006</td>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>1.846659</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-08-13</td>
      <td>-1.982397</td>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-0.083136</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2017-08-14</td>
      <td>0.773139</td>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
['A-%s' % x for x in range(6)]
```




    ['A-0', 'A-1', 'A-2', 'A-3', 'A-4', 'A-5']




```python
hhh.set_index??
```


```python
hhh.set_index(keys=['index', 'D'], append=True)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
    </tr>
    <tr>
      <th></th>
      <th>index</th>
      <th>D</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <th>2017-08-09</th>
      <th>0.415509</th>
      <td>-1.115121</td>
      <td>0.119145</td>
      <td>0.754606</td>
    </tr>
    <tr>
      <th>1</th>
      <th>2017-08-10</th>
      <th>-1.246101</th>
      <td>-0.940755</td>
      <td>0.078132</td>
      <td>0.041801</td>
    </tr>
    <tr>
      <th>2</th>
      <th>2017-08-11</th>
      <th>-0.991209</th>
      <td>0.261286</td>
      <td>1.076175</td>
      <td>0.241313</td>
    </tr>
    <tr>
      <th>3</th>
      <th>2017-08-12</th>
      <th>0.452006</th>
      <td>0.925108</td>
      <td>-0.497301</td>
      <td>1.846659</td>
    </tr>
    <tr>
      <th>4</th>
      <th>2017-08-13</th>
      <th>-1.982397</th>
      <td>-1.466844</td>
      <td>1.818685</td>
      <td>-0.083136</td>
    </tr>
    <tr>
      <th>5</th>
      <th>2017-08-14</th>
      <th>0.773139</th>
      <td>-1.817529</td>
      <td>1.223001</td>
      <td>-0.288554</td>
    </tr>
  </tbody>
</table>
</div>




```python
pl = dfs.to_panel()
```

    /Users/kang/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:1: DeprecationWarning: 
    Panel is deprecated and will be removed in a future version.
    The recommended way to represent these types of 3-dimensional data are with a MultiIndex on a DataFrame, via the Panel.to_frame() method
    Alternatively, you can use the xarray package http://xarray.pydata.org/en/stable/.
    Pandas provides a `.to_xarray()` method to help automate this conversion.
    
      """Entry point for launching an IPython kernel.



```python
pl.shape
```




    (3, 6, 6)




```python
hhh.to_pickle(path='./pickle_data/hhh.pkl')
```


```python
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                              'foo', 'foo', 'qux', 'qux'],
                              ['one', 'two', 'one', 'two',
                              'one', 'two', 'one', 'two']]))
```


```python
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
```


```python
df_mindex = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
```


```python
df_mindex
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.626486</td>
      <td>0.337824</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.580810</td>
      <td>-1.204276</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>0.621830</td>
      <td>0.066319</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">qux</th>
      <th>one</th>
      <td>-0.633566</td>
      <td>0.587697</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.420044</td>
      <td>1.435558</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 不让用了
df_pl = df_mindex.to_panel()
```

    /Users/kang/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:1: DeprecationWarning: 
    Panel is deprecated and will be removed in a future version.
    The recommended way to represent these types of 3-dimensional data are with a MultiIndex on a DataFrame, via the Panel.to_frame() method
    Alternatively, you can use the xarray package http://xarray.pydata.org/en/stable/.
    Pandas provides a `.to_xarray()` method to help automate this conversion.
    
      """Entry point for launching an IPython kernel.



```python
df_pl
```




    <class 'pandas.core.panel.Panel'>
    Dimensions: 2 (items) x 4 (major_axis) x 2 (minor_axis)
    Items axis: A to B
    Major_axis axis: bar to qux
    Minor_axis axis: one to two




```python
df_pl.shape
```




    (2, 4, 2)




```python
df_pl.rank
```




    <bound method NDFrame.rank of <class 'pandas.core.panel.Panel'>
    Dimensions: 2 (items) x 4 (major_axis) x 2 (minor_axis)
    Items axis: A to B
    Major_axis axis: bar to qux
    Minor_axis axis: one to two>




```python
df_mindex
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.626486</td>
      <td>0.337824</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.580810</td>
      <td>-1.204276</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>0.621830</td>
      <td>0.066319</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">qux</th>
      <th>one</th>
      <td>-0.633566</td>
      <td>0.587697</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.420044</td>
      <td>1.435558</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 把Index 恢复到数据域， set_index的反操作
df_mindex.reset_index()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first</th>
      <th>second</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bar</td>
      <td>one</td>
      <td>-0.264203</td>
      <td>-0.671635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bar</td>
      <td>two</td>
      <td>0.626486</td>
      <td>0.337824</td>
    </tr>
    <tr>
      <th>2</th>
      <td>baz</td>
      <td>one</td>
      <td>-0.368444</td>
      <td>-0.030595</td>
    </tr>
    <tr>
      <th>3</th>
      <td>baz</td>
      <td>two</td>
      <td>0.580810</td>
      <td>-1.204276</td>
    </tr>
    <tr>
      <th>4</th>
      <td>foo</td>
      <td>one</td>
      <td>0.621830</td>
      <td>0.066319</td>
    </tr>
    <tr>
      <th>5</th>
      <td>foo</td>
      <td>two</td>
      <td>-1.151669</td>
      <td>-0.054912</td>
    </tr>
    <tr>
      <th>6</th>
      <td>qux</td>
      <td>one</td>
      <td>-0.633566</td>
      <td>0.587697</td>
    </tr>
    <tr>
      <th>7</th>
      <td>qux</td>
      <td>two</td>
      <td>-0.420044</td>
      <td>1.435558</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 获得指定某MultiIndex的特定 level 的 Index 对象
df_mindex.index  = df_mindex.index.get_level_values(0)
```


```python

```


```python
df_mindex
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>first</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>0.626486</td>
      <td>0.337824</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>0.580810</td>
      <td>-1.204276</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>0.621830</td>
      <td>0.066319</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.633566</td>
      <td>0.587697</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.420044</td>
      <td>1.435558</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_mindex.merge(df_mindex, on='A')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B_x</th>
      <th>B_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>-0.671635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>0.337824</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>-0.030595</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>-1.204276</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>0.066319</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>-0.054912</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>0.587697</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>1.435558</td>
    </tr>
  </tbody>
</table>
</div>




```python
# on 用来设置左右共有的column name
# 
# 在 left.A == right.B 的时候， 进行合并
df_mindex.merge(df_mindex, left_on='A', right_on='B')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A_x</th>
      <th>B_x</th>
      <th>A_y</th>
      <th>B_y</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
# how =》 {‘inner', 'left', 'right', 'outer'}, 与数据库表连接概念一样
df_mindex.merge(df_mindex, how='outer', left_on='A', right_on='B')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A_x</th>
      <th>B_x</th>
      <th>A_y</th>
      <th>B_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.264203</td>
      <td>-0.671635</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.626486</td>
      <td>0.337824</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.368444</td>
      <td>-0.030595</td>
    </tr>
    <tr>
      <th>11</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.580810</td>
      <td>-1.204276</td>
    </tr>
    <tr>
      <th>12</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.621830</td>
      <td>0.066319</td>
    </tr>
    <tr>
      <th>13</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-1.151669</td>
      <td>-0.054912</td>
    </tr>
    <tr>
      <th>14</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.633566</td>
      <td>0.587697</td>
    </tr>
    <tr>
      <th>15</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.420044</td>
      <td>1.435558</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 有充足的连接条件， 单独设置 left_index or right_index ， 作用是设置结果显示哪方 index
df_mindex.merge(df_mindex, how='outer', left_on='A', right_on='B', left_index=True)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A_x</th>
      <th>B_x</th>
      <th>A_y</th>
      <th>B_y</th>
    </tr>
    <tr>
      <th>first</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>qux</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.264203</td>
      <td>-0.671635</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.626486</td>
      <td>0.337824</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.368444</td>
      <td>-0.030595</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.580810</td>
      <td>-1.204276</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.621830</td>
      <td>0.066319</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-1.151669</td>
      <td>-0.054912</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.633566</td>
      <td>0.587697</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.420044</td>
      <td>1.435558</td>
    </tr>
  </tbody>
</table>
</div>




```python
# left_index&right_index => True, 设置连接条件为 index 相同，同时保留index
df_mindex.merge(df_mindex, how='outer', left_index=True, right_index=True)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A_x</th>
      <th>B_x</th>
      <th>A_y</th>
      <th>B_y</th>
    </tr>
    <tr>
      <th>first</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>-0.264203</td>
      <td>-0.671635</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>0.626486</td>
      <td>0.337824</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>-0.264203</td>
      <td>-0.671635</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>0.626486</td>
      <td>0.337824</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>-0.368444</td>
      <td>-0.030595</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>0.580810</td>
      <td>-1.204276</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>-0.368444</td>
      <td>-0.030595</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>0.580810</td>
      <td>-1.204276</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>0.621830</td>
      <td>0.066319</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>-1.151669</td>
      <td>-0.054912</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>0.621830</td>
      <td>0.066319</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>-1.151669</td>
      <td>-0.054912</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>-0.633566</td>
      <td>0.587697</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>-0.420044</td>
      <td>1.435558</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>-0.633566</td>
      <td>0.587697</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>-0.420044</td>
      <td>1.435558</td>
    </tr>
  </tbody>
</table>
</div>




```python
# indicator 设置是否显示 _merge信息
df_mindex.merge(df_mindex, how='outer', left_on='A', right_on='B', left_index=True, suffixes=['_left', '_right'], indicator=True)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A_left</th>
      <th>B_left</th>
      <th>A_right</th>
      <th>B_right</th>
      <th>_merge</th>
    </tr>
    <tr>
      <th>first</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>qux</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>right_only</td>
    </tr>
  </tbody>
</table>
</div>




```python
# indicator 设置 _merge 列 列明
df_mindex.merge(df_mindex, how='outer', left_index=True, right_index=True, suffixes=['_left', '_right'], indicator='hah')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A_left</th>
      <th>B_left</th>
      <th>A_right</th>
      <th>B_right</th>
      <th>hah</th>
    </tr>
    <tr>
      <th>first</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>both</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>both</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>both</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>both</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>both</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>both</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>both</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>both</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>both</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>both</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>both</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>both</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>both</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>both</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>both</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>both</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_mindex.merge(df_mindex, how='outer', left_on='A', right_on='B', left_index=True, suffixes=['_left', '_right'], indicator=True)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A_left</th>
      <th>B_left</th>
      <th>A_right</th>
      <th>B_right</th>
      <th>_merge</th>
    </tr>
    <tr>
      <th>first</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>qux</th>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.264203</td>
      <td>-0.671635</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>bar</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.626486</td>
      <td>0.337824</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.368444</td>
      <td>-0.030595</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.580810</td>
      <td>-1.204276</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.621830</td>
      <td>0.066319</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-1.151669</td>
      <td>-0.054912</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.633566</td>
      <td>0.587697</td>
      <td>right_only</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>-0.420044</td>
      <td>1.435558</td>
      <td>right_only</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_mindex.merge??
```


```python

```


```python

```


```python

```


```python

```
