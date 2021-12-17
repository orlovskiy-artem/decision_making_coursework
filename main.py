from solution import Solution 
import numpy as np

f_1 = np.array([ 7,  9, 13, 14])
g_1 = np.array([ 9, 15, 28, 30])
x_1 = np.arange(4)
y_1 = np.arange(4)
f_1_x_d = dict(zip(x_1,f_1))
g_1_y_d = dict(zip(y_1,g_1))


sol = Solution([f_1_x_d, g_1_y_d], [x_1,y_1], 3)
num = sol.solve()
print(num)