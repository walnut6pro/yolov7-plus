import numpy as np

# 设置参数
num_rows = 50
num_cols = 4
side_length = 10
z_height = 1.2

# 生成时间和xy坐标数据
time = np.linspace(0, 50, num_rows)
x = np.zeros(num_rows)
y = np.zeros(num_rows)

# 生成正方形轨迹,在顶点处有弧度
for i in range(num_rows):
    if 0 <= time[i] < 12.5:
        x[i] = side_length * (time[i] / 12.5)
        y[i] = 0
    elif 12.5 <= time[i] < 25:
        x[i] = side_length
        y[i] = side_length * ((time[i] - 12.5) / 12.5)
    elif 25 <= time[i] < 37.5:
        x[i] = side_length * (1 - (time[i] - 25) / 12.5)
        y[i] = side_length
    else:
        x[i] = 0
        y[i] = side_length * (1 - (time[i] - 37.5) / 12.5)

# 生成固定高度的z坐标
z = np.full(num_rows, z_height)

# 将数据合并成一个2D数组
data = np.column_stack((time, x, y, z))

# 将数据保存到txt文件
np.savetxt("exp_car_output.txt", data, fmt="%.2f", delimiter=",")