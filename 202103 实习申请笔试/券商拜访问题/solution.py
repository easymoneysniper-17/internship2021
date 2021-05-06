#导入包
from docplex.mp.model import Model
import pandas as pd
from cplex import Cplex
from cplex.exceptions import CplexSolverError

# 相关数据和类型的简单处理
m = 525
n = 67

M = [i for i in range(0,m-1)]
N = [i for i in range(0,n-1)]
A = [(i,j) for i in M for j in N]


survey = pd.read_excel("E:\研究生文件\研一\实习\嘉实基金\券商拜访问题\调研库.xlsx",engine='openpyxl')
corp = survey["股票简称"].unique()
broker = survey["券商"].unique()
weight_a = [[0]*n for _ in range(m)]


for i in range(0,m-1):
    for j in range(0,n-1):
        if survey.loc[(survey["股票简称"] == corp[i]) & (survey["券商"] == broker[j])].iloc[:,0].size == 0:
            weight_a[i][j] = 0
        else:
            weight_a[i][j] = survey.loc[(survey["股票简称"] == corp[i]) & (survey["券商"] == broker[j])].iloc[0,3]

weight_dict_a = {(i,j):weight_a[i][j] for i in M for j in N}

# 定义模型种类， 这里是混合整数规划“MIP"
mdl = Model('MIP') #mdl是英文单词“model" 的缩写

# 定义变量，
y = mdl.binary_var_dict(N, name='y')
x = mdl.binary_var_dict(A, name='x')

for i in M:
    for j in N:
        if(weight_dict_a[i,j]==0):
            x[i,j] = 0

#定义约束条件
mdl.add_constraints(x[i,j] <= y[j] for i in M for j in N)
mdl.add_constraints(mdl.sum(x[i,j] for j in N) <= 1 for i in M)

for k in range(1,5):
    mdl.add_constraints(mdl.sum(weight_dict[i,j]*x[i,j] for i in M for j in N) <= 2000*k)
    mdl.add_constraints(mdl.sum(weight_dict[i,j]*x[i,j] for i in M for j in N) >= 2000*(k-1))
    
    for p in range(1,5):
        mdl.add_constraints(mdl.sum(y[j] for j in N) <= 13*p)
        mdl.add_constraints(mdl.sum(y[j] for j in N) >= 13*(p-1))
        #定义目标函数
        mdl.minimize(mdl.sum(y[j] for j in N))
        mdl.maximize(mdl.sum(weight_dict[i,j]*x[i,j] for i in M for j in N))
        #求解模型并显示
        solution = mdl.solve()
        print(k)
        print(p)
        print(solution)


