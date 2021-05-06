#导入包
from docplex.mp.model import Model

# 相关数据和类型的简单处理
m = 5
n = 8
M = [i for i in range(1,m+1)]
N = [i for i in range(1,n+1)]
A = {(i,j) for i in M for j in N}
W = 5000
weight = [[1050, 1730, 2575, 3540, 1220, 1340, 1530, 1270],[1050, 1730, 2575, 3540, 1220, 1340, 1530, 1270],[1050, 1730, 2575, 3540, 1220, 1340, 1530, 1270],[1050, 1730, 2575, 3540, 1220, 1340, 1530, 1270],[1050, 1730, 2575, 3540, 1220, 1340, 1530, 1270]]
weight_dict = {(i,j):weight[i-1][j-1] for i in M for j in N}

# 定义模型种类， 这里是混合整数规划“MIP"
mdl = Model('MIP') #mdl是英文单词“model" 的缩写

# 定义变量，
y = mdl.binary_var_dict(M, name='y')
x = mdl.binary_var_dict(A, name='x')

#定义目标函数
mdl.minimize(mdl.sum(y[i] for i in M))
mdl.maximize(mdl.sum(x[i,j]*weight_dict[i,j] for i in M for j in N))

#定义约束条件
mdl.add_constraints(mdl.sum(x[i,j] for i in M)==1 for j in N)
mdl.add_constraints(mdl.sum(x[i,j]*weight_dict[i,j] for j in N) <= W*y[i] for i in M)

#求解模型并显示
solution = mdl.solve()
print(solution)