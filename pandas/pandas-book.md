
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


### 对象
#### pandas.MultiIndex 对象 mix

##### method

method | explain
---|---
from_arrays(arrays[, sortorder, names]) |	Convert arrays to MultiIndex, 通过array创建MultiIndex
from_tuples(tuples[, sortorder, names]) |	Convert list of tuples to MultiIndex
from_product(iterables[, sortorder, names]) |	Make a MultiIndex from the cartesian product of multiple iterables
set_levels(levels[, level, inplace, …])|	Set new levels on MultiIndex.
set_labels(labels[, level, inplace, …])|	Set new labels on MultiIndex.
to_hierarchical(n_repeat[, n_shuffle])|	Return a MultiIndex reshaped to conform to the shapes given by n_repeat and n_shuffle.
to_frame([index])	|Create a DataFrame with the levels of the MultiIndex as columns.
is_lexsorted()|	Return True if the labels are lexicographically sorted
sortlevel([level, ascending, sort_remaining])|	Sort MultiIndex at the requested level.
droplevel([level])|	Return Index with requested level removed. 删除Index复合索引对象的某个level级别indextest_position_df.index = test_position_df.index.droplevel([0,])
swaplevel([i, j])|	Swap level i with level j.
reorder_levels(order)|	Rearrange levels using input order. 复合索引level重新排序, 如level_0 和 level_1两个索引对调, 返回一个新对象, 不可原地修改, df = df.reorder_levels([1, 0]) 
remove_unused_levels()|	create a new MultiIndex from the current that removing unused levels, meaning that they are not expressed in the labels

##### 

#### pandas.DataFrame 对象 df

* attributes 属性

attribute | explain
---|---
T | Transpose index and columns. 返回矩阵的转置
at | Access a single value for a row/column label pair.
axes |	Return a list representing the axes of the DataFrame.
blocks|	(DEPRECATED) Internal property, property synonym for as_blocks()
columns|	The column labels of the DataFrame.
dtypes|	Return the dtypes in the DataFrame.
empty|	Indicator whether DataFrame is empty.
ftypes|	Return the ftypes (indication of sparse/dense and dtype) in DataFrame.
iat|	Access a single value for a row/column pair by integer position.
iloc|	Purely integer-location based indexing for selection by position.
index|	The index (row labels) of the DataFrame.
ix|	A primarily label-location based indexer, with integer position fallback.
loc|	Access a group of rows and columns by label(s) or a boolean array.
ndim|	Return an int representing the number of axes / array dimensions.
shape|	Return a tuple representing the dimensionality of the DataFrame.
size|	Return an int representing the number of elements in this object.
style|	Property returning a Styler object containing methods for building a styled HTML representation fo the DataFrame.
values|	Return a Numpy representation of the DataFrame.

* method 方法

method | explain
---|---
abs()|	Return a Series/DataFrame with absolute numeric value of each element.
add(other[, axis, level, fill_value])|	Addition of dataframe and other, element-wise (binary operator add).
add_prefix(prefix)|	Prefix labels with string prefix.
add_suffix(suffix)|	Suffix labe≠ls with string suffix.
agg(func[, axis])|	Aggregate using one or more operations over the specified axis.
aggregate(func[, axis])|	Aggregate using one or more operations over the specified axis.
align(other[, join, axis, level, copy, …])|	Align two objects on their axes with the specified join method for each axis Index
all([axis, bool_only, skipna, level])|	Return whether all elements are True over series or dataframe axis.
any([axis, bool_only, skipna, level])|	Return whether any element is True over requested axis.
append(other[, ignore_index, …])|	Append rows of other to the end of this frame, returning a new object.
apply(func[, axis, broadcast, raw, reduce, …])|	Apply a function along an axis of the DataFrame.
applymap(func)|	Apply a function to a Dataframe elementwise.
as_blocks([copy])|	(DEPRECATED) Convert the frame to a dict of dtype -> Constructor Types that each has a homogeneous dtype.
as_matrix([columns])|	(DEPRECATED) Convert the frame to its Numpy-array representation.
asfreq(freq[, method, how, normalize, …])|	Convert TimeSeries to specified frequency.
asof(where[, subset])|	The last row without any NaN is taken (or the last row without NaN considering only the subset of columns in the case of a DataFrame)
assign(**kwargs)|	Assign new columns to a DataFrame, returning a new object (a copy) with the new columns added to the original ones.
astype(dtype[, copy, errors])|	Cast a pandas object to a specified dtype dtype.
at_time(time[, asof])|	Select values at particular time of day (e.g.
between_time(start_time, end_time[, …])|	Select values between particular times of the day (e.g., 9:00-9:30 AM).
bfill([axis, inplace, limit, downcast])|	Synonym for DataFrame.fillna(method='bfill')
bool()|	Return the bool of a single element PandasObject.
boxplot([column, by, ax, fontsize, rot, …])|	Make a box plot from DataFrame columns.
clip([lower, upper, axis, inplace])|	Trim values at input threshold(s).
clip_lower(threshold[, axis, inplace])|	Return copy of the input with values below a threshold truncated.
clip_upper(threshold[, axis, inplace])|	Return copy of input with values above given value(s) truncated.
combine(other, func[, fill_value, overwrite])|	Add two DataFrame objects and do not propagate NaN values, so if for a (column, time) one frame is missing a value, it will default to the other frame’s value (which might be NaN as well)
combine_first(other)|	Combine two DataFrame objects and default to non-null values in frame calling the method.
compound([axis, skipna, level])|	Return the compound percentage of the values for the requested axis
consolidate([inplace])|	(DEPRECATED) Compute NDFrame with “consolidated” internals (data of each dtype grouped together in a single ndarray).
convert_objects([convert_dates, …])|	(DEPRECATED) Attempt to infer better dtype for object columns.
copy([deep])|	Make a copy of this object’s indices and data.
corr([method, min_periods])|	Compute pairwise correlation of columns, excluding NA/null values
corrwith(other[, axis, drop])|	Compute pairwise correlation between rows or columns of two DataFrame objects.
count([axis, level, numeric_only])|	Count non-NA cells for each column or row.
cov([min_periods])|	Compute pairwise covariance of columns, excluding NA/null values.
cummax([axis, skipna])|	Return cumulative maximum over a DataFrame or Series axis.
cummin([axis, skipna])|	Return cumulative minimum over a DataFrame or Series axis.
cumprod([axis, skipna])|	Return cumulative product over a DataFrame or Series axis.
cumsum([axis, skipna])|	Return cumulative sum over a DataFrame or Series axis.
describe([percentiles, include, exclude])	|Generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.
diff([periods, axis])|	First discrete difference of element.
div(other[, axis, level, fill_value])|	Floating division of dataframe and other, element-wise (binary operator truediv).
divide(other[, axis, level, fill_value])|	Floating division of dataframe and other, element-wise (binary operator truediv).
dot(other)|	Matrix multiplication, 矩阵乘法
drop([labels, axis, index, columns, level, …])|	Drop specified labels from rows or columns.
drop_duplicates([subset, keep, inplace])|	Return DataFrame with duplicate rows removed, optionally only considering certain columns
dropna([axis, how, thresh, subset, inplace])|	Remove missing values.
duplicated([subset, keep])|	Return boolean Series denoting duplicate rows, optionally only considering certain columns
eq(other[, axis, level]) | Wrapper for flexible comparison methods eq
equals(other) | Determines if two NDFrame objects contain the same elements.
eval(expr[, inplace]) | Evaluate a string describing operations on DataFrame columns.
ewm([com, span, halflife, alpha, …]) | Provides exponential weighted functions
expanding([min_periods, center, axis]) | Provides expanding transformations.
ffill([axis, inplace, limit, downcast]) | Synonym for DataFrame.fillna(method='ffill')
fillna([value, method, axis, inplace, …]) | Fill NA/NaN values using the specified method
filter([items, like, regex, axis]) | Subset rows or columns of dataframe according to labels in the specified index.
first(offset) | Convenience method for subsetting initial periods of time series data based on a date offset.
first_valid_index() | Return index for first non-NA/null value.
floordiv(other[, axis, level, fill_value]) | Integer division of dataframe and other, element-wise (binary operator floordiv).
from_csv(path[, header, sep, index_col, …]) | (DEPRECATED) Read CSV file.
from_dict(data[, orient, dtype, columns]) | Construct DataFrame from dict of array-like or dicts.
from_items(items[, columns, orient]) | (DEPRECATED) Construct a dataframe from a list of tuples
from_records(data[, index, exclude, …]) | Convert structured or record ndarray to DataFrame
ge(other[, axis, level]) | Wrapper for flexible comparison methods ge
get(key[, default]) | Get item from object for given key (DataFrame column, Panel slice, etc.).
get_dtype_counts() | Return counts of unique dtypes in this object.
get_ftype_counts() | (DEPRECATED) Return counts of unique ftypes in this object.
get_value(index, col[, takeable]) | (DEPRECATED) Quickly retrieve single value at passed column and index
get_values() | Return an ndarray after converting sparse values to dense.
groupby([by, axis, level, as_index, sort, …]) | Group series using mapper (dict or key function, apply given function to group, return result as series) or by a series of columns.
gt(other[, axis, level]) | Wrapper for flexible comparison methods gt
head([n]) | Return the first n rows.
hist([column, by, grid, xlabelsize, xrot, …]) | Make a histogram of the DataFrame’s.
idxmax([axis, skipna]) | Return index of first occurrence of maximum over requested axis.
idxmin([axis, skipna]) | Return index of first occurrence of minimum over requested axis.
infer_objects() | Attempt to infer better dtypes for object columns.
info([verbose, buf, max_cols, memory_usage, …]) | Print a concise summary of a DataFrame.
insert(loc, column, value[, allow_duplicates]) | Insert column into DataFrame at specified location.
interpolate([method, axis, limit, inplace, …]) | Interpolate values according to different methods.
isin(values) | Return boolean DataFrame showing whether each element in the DataFrame is contained in values.
isna() | Detect missing values.
isnull() | Detect missing values.
items() | Iterator over (column name, Series) pairs.
iteritems() | Iterator over (column name, Series) pairs.
iterrows() | Iterate over DataFrame rows as (index, Series) pairs.
itertuples([index, name]) | Iterate over DataFrame rows as namedtuples, with index value as first element of the tuple.
join(other[, on, how, lsuffix, rsuffix, sort]) | Join columns with other DataFrame either on index or on a key column.
keys() | Get the ‘info axis’ (see Indexing for more)
kurt([axis, skipna, level, numeric_only]) | Return unbiased kurtosis over requested axis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
kurtosis([axis, skipna, level, numeric_only]) | Return unbiased kurtosis over requested axis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
last(offset) | Convenience method for subsetting final periods of time series data based on a date offset.
last_valid_index() | Return index for last non-NA/null value.
le(other[, axis, level]) | Wrapper for flexible comparison methods le
lookup(row_labels, col_labels) | Label-based “fancy indexing” function for DataFrame.
lt(other[, axis, level]) | Wrapper for flexible comparison methods lt
mad([axis, skipna, level]) | Return the mean absolute deviation of the values for the requested axis
mask(cond[, other, inplace, axis, level, …]) | Return an object of same shape as self and whose corresponding entries are from self where cond is False and otherwise are from other.
max([axis, skipna, level, numeric_only]) | This method returns the maximum of the values in the object.
mean([axis, skipna, level, numeric_only]) | Return the mean of the values for the requested axis
median([axis, skipna, level, numeric_only]) | Return the median of the values for the requested axis
melt([id_vars, value_vars, var_name, …]) | “Unpivots” a DataFrame from wide format to long format, optionally leaving identifier variables set.
memory_usage([index, deep]) | Return the memory usage of each column in bytes.
merge(right[, how, on, left_on, right_on, …]) | Merge DataFrame objects by performing a database-style join operation by columns or indexes.
min([axis, skipna, level, numeric_only]) | This method returns the minimum of the values in the object.
mod(other[, axis, level, fill_value]) | Modulo of dataframe and other, element-wise (binary operator mod).
mode([axis, numeric_only]) | Gets the mode(s) of each element along the axis selected.
mul(other[, axis, level, fill_value]) | Multiplication of dataframe and other, element-wise (binary operator mul).
multiply(other[, axis, level, fill_value]) | Multiplication of dataframe and other, element-wise (binary operator mul).
ne(other[, axis, level]) | Wrapper for flexible comparison methods ne
nlargest(n, columns[, keep]) | Return the first n rows ordered by columns in descending order.
notna() | Detect existing (non-missing) values.
notnull() | Detect existing (non-missing) values.
nsmallest(n, columns[, keep]) | Get the rows of a DataFrame sorted by the n smallest values of columns.
nunique([axis, dropna]) | Return Series with number of distinct observations over requested axis.
pct_change([periods, fill_method, limit, freq]) | Percentage change between the current and a prior element.
pipe(func, *args, **kwargs) | Apply func(self, *args, **kwargs)
pivot([index, columns, values]) | Return reshaped DataFrame organized by given index / column values.
pivot_table([values, index, columns, …]) | Create a spreadsheet-style pivot table as a DataFrame.
plot | alias of pandas.plotting._core.FramePlotMethods
pop(item) | Return item and drop from frame.
pow(other[, axis, level, fill_value]) | Exponential power of dataframe and other, element-wise (binary operator pow).
prod([axis, skipna, level, numeric_only, …]) | Return the product of the values for the requested axis
product([axis, skipna, level, numeric_only, …]) | Return the product of the values for the requested axis
quantile([q, axis, numeric_only, interpolation]) | Return values at the given quantile over requested axis, a la numpy.percentile.
query(expr[, inplace]) | Query the columns of a frame with a boolean expression.
radd(other[, axis, level, fill_value]) | Addition of dataframe and other, element-wise (binary operator radd).
rank([axis, method, numeric_only, …]) | Compute numerical data ranks (1 through n) along axis.
rdiv(other[, axis, level, fill_value]) | Floating division of dataframe and other, element-wise (binary operator rtruediv).
reindex([labels, index, columns, axis, …]) | Conform DataFrame to new index with optional filling logic, placing NA/NaN in locations having no value in the previous index.
reindex_axis(labels[, axis, method, level, …]) | Conform input object to new index with optional filling logic, placing NA/NaN in locations having no value in the previous index.
reindex_like(other[, method, copy, limit, …]) | Return an object with matching indices to myself.
rename([mapper, index, columns, axis, copy, …]) | Alter axes labels.
rename_axis(mapper[, axis, copy, inplace]) | Alter the name of the index or columns.
reorder_levels(order[, axis]) | Rearrange index levels using input order.
replace([to_replace, value, inplace, limit, …]) | Replace values given in to_replace with value.
resample(rule[, how, axis, fill_method, …]) | Convenience method for frequency conversion and resampling of time series.
reset_index([level, drop, inplace, …]) | For DataFrame with multi-level index, return new DataFrame with labeling information in the columns under the index names, defaulting to ‘level_0’, ‘level_1’, etc.
rfloordiv(other[, axis, level, fill_value]) | Integer division of dataframe and other, element-wise (binary operator rfloordiv).
rmod(other[, axis, level, fill_value]) | Modulo of dataframe and other, element-wise (binary operator rmod).
rmul(other[, axis, level, fill_value]) | Multiplication of dataframe and other, element-wise (binary operator rmul).
rolling(window[, min_periods, center, …]) | Provides rolling window calculations.
round([decimals]) | Round a DataFrame to a variable number of decimal places.
rpow(other[, axis, level, fill_value]) | Exponential power of dataframe and other, element-wise (binary operator rpow).
rsub(other[, axis, level, fill_value]) | Subtraction of dataframe and other, element-wise (binary operator rsub).
rtruediv(other[, axis, level, fill_value]) | Floating division of dataframe and other, element-wise (binary operator rtruediv).
sample([n, frac, replace, weights, …]) | Return a random sample of items from an axis of object.
select(crit[, axis]) | (DEPRECATED) Return data corresponding to axis labels matching criteria
select_dtypes([include, exclude]) | Return a subset of the DataFrame’s columns based on the column dtypes.
sem([axis, skipna, level, ddof, numeric_only]) | Return unbiased standard error of the mean over requested axis.
set_axis(labels[, axis, inplace]) | Assign desired index to given axis.
set_index(keys[, drop, append, inplace, …]) | Set the DataFrame index (row labels) using one or more existing columns.
set_value(index, col, value[, takeable]) | (DEPRECATED) Put single value at passed column and index
shift([periods, freq, axis]) | Shift index by desired number of periods with an optional time freq
skew([axis, skipna, level, numeric_only]) | Return unbiased skew over requested axis Normalized by N-1
slice_shift([periods, axis]) | Equivalent to shift without copying data.
sort_index([axis, level, ascending, …]) | Sort object by labels (along an axis)
sort_values(by[, axis, ascending, inplace, …]) | Sort by the values along either axis
sortlevel([level, axis, ascending, inplace, …]) | (DEPRECATED) Sort multilevel index by chosen axis and primary level.
squeeze([axis]) | Squeeze length 1 dimensions.
stack([level, dropna]) | Stack the prescribed level(s) from columns to index.
std([axis, skipna, level, ddof, numeric_only]) | Return sample standard deviation over requested axis.
sub(other[, axis, level, fill_value]) | Subtraction of dataframe and other, element-wise (binary operator sub).
subtract(other[, axis, level, fill_value]) | Subtraction of dataframe and other, element-wise (binary operator sub).
sum([axis, skipna, level, numeric_only, …]) | Return the sum of the values for the requested axis
swapaxes(axis1, axis2[, copy]) | Interchange axes and swap values axes appropriately
swaplevel([i, j, axis]) | Swap levels i and j in a MultiIndex on a particular axis
tail([n]) | Return the last n rows.
take(indices[, axis, convert, is_copy]) | Return the elements in the given positional indices along an axis.
to_clipboard([excel, sep]) | Copy object to the system clipboard.
to_csv([path_or_buf, sep, na_rep, …]) | Write DataFrame to a comma-separated values (csv) file
to_dense() | Return dense representation of NDFrame (as opposed to sparse)
to_dict([orient, into]) | Convert the DataFrame to a dictionary.
to_excel(excel_writer[, sheet_name, na_rep, …]) | Write DataFrame to an excel sheet
to_feather(fname) | write out the binary feather-format for DataFrames
to_gbq(destination_table, project_id[, …]) | Write a DataFrame to a Google BigQuery table.
to_hdf(path_or_buf, key, **kwargs) | Write the contained data to an HDF5 file using HDFStore.
to_html([buf, columns, col_space, header, …]) | Render a DataFrame as an HTML table.
to_json([path_or_buf, orient, date_format, …]) | Convert the object to a JSON string.
to_latex([buf, columns, col_space, header, …]) | Render an object to a tabular environment table.
to_msgpack([path_or_buf, encoding]) | msgpack (serialize) object to input file path
to_panel() | (DEPRECATED) Transform long (stacked) format (DataFrame) into wide (3D, Panel) format.
to_parquet(fname[, engine, compression]) | Write a DataFrame to the binary parquet format.
to_period([freq, axis, copy]) | Convert DataFrame from DatetimeIndex to PeriodIndex with desired frequency (inferred from index if not passed)
to_pickle(path[, compression, protocol]) | Pickle (serialize) object to file.
to_records([index, convert_datetime64]) | Convert DataFrame to a NumPy record array.
to_sparse([fill_value, kind]) | Convert to SparseDataFrame
to_sql(name, con[, schema, if_exists, …]) | Write records stored in a DataFrame to a SQL database.
to_stata(fname[, convert_dates, …]) | Export Stata binary dta files.
to_string([buf, columns, col_space, header, …]) | Render a DataFrame to a console-friendly tabular output.
to_timestamp([freq, how, axis, copy]) | Cast to DatetimeIndex of timestamps, at beginning of period
to_xarray() | Return an xarray object from the pandas object.
transform(func, *args, **kwargs) | Call function producing a like-indexed NDFrame and return a NDFrame with the transformed values
transpose(*args, **kwargs) | Transpose index and columns.
truediv(other[, axis, level, fill_value]) | Floating division of dataframe and other, element-wise (binary operator truediv).
truncate([before, after, axis, copy]) | Truncate a Series or DataFrame before and after some index value.
tshift([periods, freq, axis]) | Shift the time index, using the index’s frequency if available.
tz_convert(tz[, axis, level, copy]) | Convert tz-aware axis to target time zone.
tz_localize(tz[, axis, level, copy, ambiguous]) | Localize tz-naive TimeSeries to target time zone.
unstack([level, fill_value]) | Pivot a level of the (necessarily hierarchical) index labels, returning a DataFrame having a new level of column labels whose inner-most level consists of the pivoted index labels.
update(other[, join, overwrite, …]) | Modify in place using non-NA values from another DataFrame.
var([axis, skipna, level, ddof, numeric_only]) | Return unbiased variance over requested axis.
where(cond[, other, inplace, axis, level, …]) | Return an object of same shape as self and whose corresponding entries are from self where cond is True and otherwise are from other.
xs(key[, axis, level, drop_level]) | Returns a cross-section (row(s) or column(s)) from the Series/DataFrame.

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
df.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise') | DataFrame里删除


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
idx.set_levels([['a','b'], [1,2]]) | 重置符合索引
pd.MultiIndex.from_tuples(tuples, names=['one', 'two']) | 创建复合索引
df.set_index(self, keys, drop=True, append=False, inplace=False, verify_integrity=False | 将某一列(或者多列-list形成符合索引)转化为INDEX, 同时此列在数据域将被删除, 默认返回新的df. exp: keys=['datatime', 'code'],生成二级索引. drop是否丢弃数据域原index数据. append是否保留原来的index(新设置的index作为二级, 三级index添加在后面)
df.reset_index(level=[0,], drop=False, inplace=False, col_level=0, col_fill='') | .set_index 的反操作. 还原索引为数据. level设置还原级别, 默认全部还原. drop设置是否删除的被转化的索引.
df.sort_index(axis=1, ascending=Fasle, level=) |  按照轴排序, 正序倒序, 不接受列表自定义排序
DataFrame.sortlevel(level=0, axis=0, ascending=True, inplace=False, sort_remaining=True) | 指定按照某个level 的INDEX进行排序
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