
### 数据类型
数据类型 | 意义
---|---
Series |  一维数组, 类型相同
DataFrame | 二维表格数据类型, 理解为Series的容器 ==df
Panel  | 三维数组, 理解为 DataFrame 的容器==pl, 未来此数据类型将被放弃, 推荐使用MultiIndex-DataFrame (复合索引)

### 创建对象

方法 | 意义
---|---
pd.Series([1,3,4,np.nan,6,8], index=) |  用列表创建 Series
pd.date_range('20130101', periods=6) | 创建 DatetimeIndex  对象
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD')) |  创建 DataFrame  对象
pd.DataFrame({column1: data1,...} ) | 通过字典创建
pd.date_range(start=None, end=None, periods=None, freq='D', tz=None, normalize=False, name=None, closed=None, **kwargs) | 创建时间序列Series, freq可以指定间隔是年月日时分秒.

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


### 选择数据
* 切片并不需要 index 或者 column 在实际意义上有真正的顺序

方法 | 意义
---|---
**---标签选择---** | **---[左右都包括]---**
df['A'] | ==df.A , 获取 A 列 返回的是Series类型
df[['A', 'B']] | 取出多列数据, 返回的是 DataFrame 类型
df.loc['index1'] | 使用标签索引
df.loc[:, ['A','B']] | 切片
df.loc['20170101':'20170202', ['A', 'B']] |  切片
df.loc['20170101': '20170202', 'A':'B'] |  切片
df.loc['20170101', 'A'] |  获取单个值
df.at['20170101', 'A'] |  获取单个标量(同上)
**---位置索引选择---** | **---[半闭半开区间,右侧边界不包括)---**
df[0:3] | 对行进行切片
df.iloc | 支持 单个位置索引, 列表, 切片. 不同轴的操作用","隔开
df.iloc[3] | 位置选择, 支持负数
df.iloc[3:5, 0:2] |  通过数值切片 **[左闭包括, 右开不包括)**
df.iloc[[1,2,4],[0,2]] |  通过指定位置列表
df.iloc[1:3,:] |  行切片, 后面的冒号可以省略
df.iloc[:, 1:3] |  列切片
df.iloc[1,1] |  获取特定值
df.iloc[bool_list] | 可以用 bool 组成的列表进行过滤
df.iat[1,1] | 访问某个标量(同上)
---- | ----
df[df.A > 0] |  通过某列选择数据,其实就是用了bool_list过滤
df[df > 0] | 过滤每一元素, 不满足的重置为 NaN
df[df['E'].isin(['two', 'four'])] | 通过已知列表过滤
df.iloc[0].item() | 获取单个数据


### 编辑更新

方法 | 意义
---|---
df['F']= aSeries |  新增一列数据, 默认需要index对应, 不对应设置为Null
df.at['index1','colum1'] = 0 |  标签索引更新单个值
df.iat['num1', 'num2'] = 0 | 根据位置更新单个值
df.loc[: 'D'] = np.array[[5] *len(df)] |  更新一列值
df[df>0] = -df |  通过 where 更新, 大于0全变成负的
df.append(other) | 添加多行, 如果包含不存在的columns, 则增加
df.round | 对数据保留固定有效位数
df.str.lower() |  所有转变为小写

### 数据整理--缺失数据更新\重新取样等

方法 | 意义
---|---
df.reindex(index=, columns=) |  修改,增加,删除索引列
df.dropna(how='any') |  丢弃缺失行, any=缺少就删除, all=全部缺少才删除
df.fillna(value=5) |  对缺失值进行赋值
pd.isnull(df) |  查看是否是缺失, 把值都变成 True,False
df.drop_duplicates(subset=None, keep='first', inplace=False) | 删除重复, subset设置审查哪些columns重复, 默认全部, inplace原地修改.
df.resample | 按一定时间规则重新取样
df.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None) | 对样本进行随机取样, n设定要返回的数据量, frac设置返回的比例, 不能与n同时使用. weights设置数据取样权重. random_state随机因子, axis设置要随机取样的轴.
df.nsmallest(n, 'value') | 取出某个值最小的n条数据
df.nlargest(n, 'value') | 取出某个值最大的n条数据
df.filter(items=None, like=None, regex=None, axis=None) | 对轴name用一定规则过滤


### 描述和汇总统计

方法 | 意义
---|---
df.sum(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, **kwargs)| 求和, axis=1设置横向求和,   *
df.mean() |  按列求平均值
df.mean(1) |  按行求平均
df.sub(s, axis='index') | df 减法, NaN 与任何运算都是 NaN
df.cumsum | 计算累加
df.cumprod | 样本值的累计积
df.prod | product, 乘积， 返回某轴的值得乘积， 可用于计算累积收益率
df.argmin | 获取最小值的索引位置
df.argmax | 获取最大值得索引位置
df.quantile | 计算样本的分位数（0 到 1）
df.mad | 根据平均值计算平均绝对离差
df.var | 样本值的方差 
df.cov(otherDF, min_periods=None) | 协方差
df.std( ddof=1) | 返回某个轴的标准差
df.skew | 样本值的偏度（三阶矩）
df.kurt | 样本值的峰度（四阶矩）
diff() | 计算一阶差分（对时间序列很有用) , 比如计算相隔9个数据的差==> shift 然后相减操作
df.pct_change(periods=1) | 计算增长率, periods设置相隔几天的增长率
df.shift | 数据错位, 正数向下错位, 负数向上. 错出空位直接填充NaN,  freq可以指定错位多长时间或者时间规则
df.apply(np.cumsum) |  累加
df.apply(lambda x: x.max() - x.min()) | 每列的 最大-最小
df.agg | Aggregate, 对某个轴进行聚合, 如 df.groupby('symbol').agg(func={'date': [np.min, np.max]}), 返回股票的 symbol/上市时间/退市时间


### 运算
方法 | 意义
--- | ---
df.divide(dfD, axis=0) | 按行运算, 所有的df123与dfD 对应行进行运算


### 合并
方法 | 意义
---|---
pd.concat([df[:3],df[3:6]]) | 连接
DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None) | 合并, how=>{'inner', 'left', 'right', 'outer'}与数据库表连接概念相同; on=lable or list, 设置在某一列**值**相等时进行连接; left_on&right_on=>label or list, or array-like, 设置左右哪些列相等的时候, 进行连接; left_index&right_index=>bool, 当只设置一个为True, 则是选择显示的index, 当左右都是True, 则是规定按照左右index进行连接; suffixes=list-like-str, 设置合并后的columns后缀, 用于显示归属左右哪方数据; copy=>bool 默认True, 是否拷贝数据; indicator=>bool or str, 设置一列_merge信息列, 用于记录每一行数据来源{left_only, right_only, both}, str则是替换_merge的自定义名称; sort=>bool
df.append(df.iloc[3], ignore_index=True) | 追加



### 分组

方法 | 意义
---|---
df.groupby('A').sum() | 按照 A 列元素分组, 然后求和
df.groupby(['A','B']).sum() | 先按 A 分组, 然后再按 B 分组, 并求和

### 重塑

方法 | 意义
---|---
df2.stack() |  将最后一级别的 column  转变为 index
df2.unstack() | 对调 index 和 column?

### 时间序列

方法 | 意义
---|---
pd.date_range('2017-01-01 00:00', periods=5, freq='D') | 创建一个时间序列
df.tz_localize('UTC') |  国际时间表示
df.ts_convert('US/Eastern') |  时区转换

### index-column 标签操作

函数 | 意义
---| ---
indexobj.difference | 计算两个df 的index或者 column 的差集, 接受df or index or list-like
indexobj.get_loc | 将label 转换为 location number
indexobj.get_level_values(i) | 获得某个符合索引的 某level 的index 对象
pd.MultiIndex.from_tuples(tuples, names=['one', 'two']) | 创建复合索引
df.set_index(self, keys, drop=True, append=False, inplace=False, verify_integrity=False | 将某一列(或者多列-list形成符合索引)转化为INDEX, 同时此列在数据域将被删除, 默认返回新的df. exp: keys=['datatime', 'code'],生成二级索引. drop是否丢弃数据域原index数据. append是否保留原来的index(新设置的index作为二级, 三级index添加在后面)
df.reset_index(level=[0,], drop=False, inplace=False, col_level=0, col_fill='') | .set_index 的反操作. 还原索引为数据. level设置还原级别, 默认全部还原. drop设置是否删除的被转化的索引.
df.sort_index(axis=1, ascending=Fasle) |  按照轴排序, 正序倒序, 不接受列表自定义排序
df.sort_values(by='B') | 按值排序, 不接受自定义排序. ascending=False 降序, axis指定轴
df.reindex(index=, columns=, *kw) | 重新对轴进行排序, 接受列表自定义排序, 相对传入index缺失的填充NaN, 多余的会被删除.
df.rename(index=None, columns=None, **kwargs) | 给标签重新命名,可以接受字典用于映射, 或函数, 接受旧name, 返回新name
---|---
multiIndex_df.to_panel() | 默认column(第二轴)=>变为第一轴, index(level_0) 变为第二轴, index(level_1)变为第三轴
.transpose(list-like) | 调整轴的顺序, [2, 0, 1]表示原来第三轴变为第一轴...

### 导出操作
函数|意义
---|---
.to_dict | 导出为字典, {column1: {index1: data1, index2:data2...}...}


### 遇到的一些问题

* ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
      ```Python

      >>> 0.7 < df123_cum_ratio_A <= 0.9
      ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
      解决： 
      The or and and python statements require truth-values. For pandas these are considered ambiguous so you should use "bitwise" | (or) or & (and) operations:
      # 必须使用 & 符号， 或者用np.logic_and(x, y)
      ############################################
      ```

* 切片并不需要 index 或者 column 在实际意义上有真正的顺序

      ```python
      df123.columns => ['D', 'B', 'C', 'A']
      df123.loc[:, 'D':'B'] --> columns['D', 'B']
      ```

* df.reset_index 使用

      ```python
      In [318]: data  
      Out[318]:   
            c    d  
      a   b            
      bar one  z  1.0  
      two  y  2.0  
      foo one  x  3.0  
      two  w  4.0  
      
      In [319]: data.reset_index()  
      Out[319]:   
      a    b  c    d  
      0  bar  one  z  1.0  
      1  bar  two  y  2.0  
      2  foo  one  x  3.0  
      3  foo  two  w  4.0  
      ```

* df.set_index
      ```python
      hhh
            index |   D	|   B	  |    C	  |    A
      0 | 2017-08-09 | -1.188626 | -0.927875 | 0.135526
      1 | 2017-08-10 | 0.706457 | 1.952693 | -0.562156
      2 | 2017-08-11 | 1.460021 | 0.316920 | 0.119041
      3 | 2017-08-12 | -0.676788 | -0.278519 | -1.812865
      4 | 2017-08-13 | -0.085896 | 0.834845 | -0.919234
      5 | 2017-08-14 | 0.528238 | -0.722072 | 0.145022

      
      hhh.set_index(keys=['index', 'D'])
                                    B	    C	          A
      index	            D			
      2017-08-09	-1.188626	-0.927875	0.135526	0.414379
      2017-08-10	0.706457	1.952693	-0.562156	0.760713
      2017-08-11	1.460021	0.316920	0.119041	0.750949
      2017-08-12	-0.676788	-0.278519	-1.812865	1.030102
      2017-08-13	-0.085896	0.834845	-0.919234	0.605697
      2017-08-14	0.528238	-0.722072	0.145022	-2.086306
      ```

* pd.MultiIndex使用

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