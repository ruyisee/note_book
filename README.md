
### 数据类型
数据类型 | 意义
---|---
Series |  一维数组, 类型相同
DataFrame | 二维表格数据类型, 理解为Series的容器
Panel | 三维数组, 理解为 DataFrame 的容器

### 创建对象

方法 | 意义
---|---
pd.Series([1,3,4,np.nan,6,8]) |  用列表创建 Series
pd.date_range('20130101', periods=6) | 创建 DatetimeIndex  对象
pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD')) |  创建 DataFrame  对象
pd.Series({column1: data1,...} ) | 通过字典创建

### 查看对象

方法 | 意义
---|---
df.head(n) |  查看前 n 行, 默认 n=5
df.tail(n) |  查看后 n 行, 默认 n=5
df.index |  查看index
df.colums |  查看 colums
df.values | 查看数值
df.describe() |  查看数据快速统计结果
df.T |  数据转置
df.sort_index(axis=1, ascending=Fasle) |  按照轴排序, 正序倒序
df.sort_values(by='B') | 按值排序

### 选择数据

方法 | 意义
---|---
df['A'] | ==df.A , 获取 A 列
df[0:3] | 对行进行切片
df.loc['index1'] | 使用标签索引
df.loc[:, ['A','B']] | 切片
df.loc['20170101':'20170202', ['A', 'B']] |  切片
df.loc['20170101': '20170202', 'A':'B'] |  切片
df.loc['20170101', 'A'] |  获取单个值
df.at['20170101', 'A'] |  获取单个标量(同上)
 **---位置式选择---** | **---位置式选择---**
df.iloc[3] | 位置选择
df.iloc[3:5, 0:2] |  通过数值切片 **[左闭包括, 右开不包括)**
df.iloc[[1,2,4],[0,2]] |  通过指定位置列表
df.iloc[1:3,:] |  行切片, 后面的冒号可以省略
df.iloc[:, 1:3] |  列切片
df.iloc[1,1] |  获取特定值
df.iat[1,1] | 访问某个标量(同上)
---- | ----
df[df.A > 0] |  通过某列选择数据
df[df > 0] | 过滤每一元素, 不满足的重置为 NaN
df[df['E'].isin(['two', 'four'])] | 通过已知列表过滤


### 编辑更新

方法 | 意义
---|---
df['F']= aSeries |  新增一列数据
df.at['index1','colum1'] = 0 |  标签索引更新单个值
df.iat['num1', 'num2'] = 0 | 根据位置更新单个值
df.loc[: 'D'] = np.array[[5] *len(df)] |  更新一列值
df[df>0] = -df |  通过 where 更新, 大于0全变成负的


### 缺失数据更新

方法 | 意义
---|---
df.reindex(index=, columns=) |  修改,增加,删除索引列
df.dropna(how='any') |  丢弃缺失行, any=缺少就删除, all=全部缺少才删除
df.fillna(value=5) |  对缺失值进行赋值
pd.isnull(df) |  查看是否是缺失, 把值都变成 True,False

### 操作

方法 | 意义
---|---
df.mean() |  按列求平均值
df.mean(1) |  按行求平均
df.shift(n) | 数据错位, n>0 表示数据向后错位
df.sub(s, axis='index') | df 减法, NaN 与任何运算都是 NaN

### 应用 function

方法 | 意义
---|---
df.apply(np.cumsum) |  累加
df.apply(lambda x: x.max() - x.min()) | 每列的 最大-最小

### 字符串方法

方法 | 意义
---|---
df.str.lower() |  所有转变为小写


### 合并
方法 | 意义
---|---
pd.concat([df[:3],df[3:6]]) | 连接
pd.merge(left, right, on='key') | 合并, 对 key(column)  相同的进行排列组合, 一一匹配
df.append(df.iloc[3], ignore_index=True) | 追加

### 分组


方法 | 意义
---|---
df.groupby('A').sum() | 按照 A 列元素分组, 然后求和
df.groupby(['A','B']).sum() | 先按 A 分组, 然后再按 B 分组, 并求和

### 重塑

方法 | 意义
---|---
pd.MultiIndex.from_tuples(tuples, names=['one', 'two']) | 创建复合索引
df2.stack() |  将最后一级别的 column  转变为 index
df2.unstack() | 对调 index 和 column?


 ```
 >>> tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                         'foo', 'foo', 'qux', 'qux'],
                        ['one', 'two', 'one', 'two',
                         'one', 'two', 'one', 'two']]))
>>> tuples
    [('bar', 'one'), ('bar', 'two'),
     ('baz', 'one'), ('baz', 'two'),
     ('foo', 'one'), ('foo', 'two'),
     ('qux', 'one'), ('qux', 'two')]
>>> index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
>>> index
    MultiIndex(levels=[[u'bar', u'baz', u'foo', u'qux'], [u'one', u'two']],
               labels=[[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]],
               names=[u'first', u'second'])
>>> df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
>>> df
                         A         B
    first second
    bar   one    -0.922059 -0.918091
          two    -0.825565 -0.880527
    baz   one     0.241927  1.130320
          two    -0.261823  2.463877
    foo   one    -0.220328 -0.519477
          two    -1.028038 -0.543191
    qux   one     0.315674  0.558686
          two     0.422296  0.241212
>>> df2 = df[:4]
>>> df2
                             A         B
    first second
    bar   one    -0.922059 -0.918091
          two    -0.825565 -0.880527
    baz   one     0.241927  1.130320
          two    -0.261823  2.463877
```

### 时间序列


方法 | 意义
---|---
pd.date_range('2017-01-01 00:00', periods=5, freq='D') | 创建一个时间序列
df.tz_localize('UTC') |  国际时间表示
df.ts_convert('US/Eastern') |  时区转换

### index 标签操作

method of pandas.core.indexes.base.Index instance

函数 | 意义
---| ---
df.columns.difference | 计算两个df 的index或者 column 的差集, 接受df or index or list-like

