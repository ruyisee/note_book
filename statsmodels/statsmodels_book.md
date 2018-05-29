```
import statsmodels.api as sm 
#最小二乘
from statsmodels.stats.outliers_influence import summary_table 
#获得汇总信息

st, data, ss2 = summary_table(res, alpha=0.05) 
#置信水平alpha=5%，st数据汇总，data数据详情，ss2数据列名
fitted_values = data[:,2]  
#等价于res.fittedvalues

res.model.endog ==y.values  
#拟合回归模型的endog值就是因变量y
res.fittedvalues  #获取拟合y值

res.params  #拟合回归模型参数
res.params[0]+res.params[1]*daily_data['temp']==res.fittedvalues  #验证二维回归模型的拟合y值计算原理
```
* import statsmodels.api as sm
* 线性回归: y = a * x + b * 1, 已知 x, y序列, 求系数 a, b
方法 | 意义
---|---
sm.add_constant(data, prepend=True, has_constant='skip') | 添加y= ax + b 常数项, 默认是没有的, 其实就是加一个全为1的列. 
sm.OLS(endog, exog, missing='none', hasconst=None) | 回归分析, 权重weights被忽略, endog=>因变量y, exog=>自变量x, missing=>{'none', 'drop', 'raise'}, 设置对nan数据的处理方式, {不检查, 丢弃, 报错}, 默认不检查.
sm.WLS | 回归分析, OLS的父类, 允许加权计算