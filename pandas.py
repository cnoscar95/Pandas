import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


q_table = pd.DataFrame(columns=list(range(4)),  dtype=np.float64)
q_table


q_table = q_table.append(
    pd.Series(
        [0]*4,
        index=q_table.columns,
        name='a'
    )
)
q_table


dates = pd.date_range('20200101', periods=6)
dates

df = pd.DataFrame(np.random.randint(12, size=(6, 4)), index=dates, columns=['a', 'b', 'c', 'd'])
df


# 取表中的值
df.values

# 取表中的列
df.loc[:, ['a', 'b']]

# 区别于
df.loc[:, 'a']
df['a']

# 取表中的行
df['2020-01-01': '2020-01-03']
df[0:3]
df.iloc[0:3]

# 区别于 
df.iloc[0]


# 取表中的多行多列
df.iloc[0:3, 1:2]

# 取表中的特定行
df.iloc[[0, 1, 4], :]

# 取表中的位置
df.iloc[0,1]
df.iat[0, 1]


# 排序
df.sort_values(by='c', ascending=True)


# 按值筛选
df[df['a'] == value]
df[df.a == value]


# 替换值为NaN
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
df

# 删除NaN所在行/列
df.dropna(axis=0, how='any')
df.dropna(axis=0, how='all')

# 替换值为0
df.fillna(value=0)

# 检查是否存在0
np.any(df.isnull() == 0)


# 读取文件（以,分隔）
data = pd.read_csv('xx.csv', header=None)
# 读取文件（以tab分隔）
data = pd.read_table('xx.csv', header=None)

# 将第一列设为index
data = pd.read_csv('xx.csv', index_col=[0])

# 添加列名
data.columns = ['name', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'y/n']
data

# 以'name'栏替换index
data_new = data.set_index('name', drop=True, append=False)
data_new

# 保存
#data_new.to_csv('xx_new.csv')


df1 = pd.read_csv('diabetes_1.csv', index_col=[0])
df2 = pd.read_csv('diabetes_2.csv', index_col=[0])
df3 = pd.read_csv('diabetes_3.csv', index_col=[0])

# 上下合并
res = pd.concat([df1, df2, df3], axis=0)
res

# 上下合并
df1.append(df2)

# 排序
res.sort_index(axis=0, ascending=True)

# 重置index
res.sort_index(axis=0, ascending=True, ignore_index=True)


# 画图
num = pd.Series(np.random.randn(1000), index=np.arange(1000))
num = num.cumsum()
num.plot()
plt.show()


df = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
df = df.cumsum()

#ax = df.plot.scatter(x='A', y='B', color='DarkBlue', label='Class1')
#bx = df.plot.scatter(x='A', y='C', color='DarkGreen', label='Class2', ax=ax)

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 4)

ax1.scatter(df['A'].values, df['B'].values, color='DarkBlue', label='Class1')
df.plot.scatter(x='A', y='C', color='DarkGreen', label='Class2', ax=ax2)

plt.show()
