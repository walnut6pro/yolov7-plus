import numpy as np
from scipy.interpolate import BSpline

def generate_noisy_trajectory_fine_bspline():
    # 参数设置
    initial_pause = 10
    acceleration_time = 10
    constant_speed_time = 40
    deceleration_time = 10
    final_pause = 10
    acceleration = 0.1
    deceleration = -0.1
    constant_speed = 0.7
    time_interval = 0.1

    # 计算时间点
    t_initial_pause = np.arange(0, initial_pause, time_interval)
    t_acceleration = np.arange(initial_pause, initial_pause + acceleration_time, time_interval)
    t_constant_speed = np.arange(initial_pause + acceleration_time, initial_pause + acceleration_time + constant_speed_time, time_interval)
    t_deceleration = np.arange(initial_pause + acceleration_time + constant_speed_time, initial_pause + acceleration_time + constant_speed_time + deceleration_time, time_interval)
    t_final_pause = np.arange(initial_pause + acceleration_time + constant_speed_time + deceleration_time, initial_pause + acceleration_time + constant_speed_time + deceleration_time + final_pause, time_interval)

    # 计算位移
    x_initial_pause = np.zeros_like(t_initial_pause)
    x_acceleration = 0.5 * acceleration * (t_acceleration - initial_pause) ** 2
    x_constant_speed = constant_speed * (t_constant_speed - t_constant_speed[0]) + x_acceleration[-1]
    x_deceleration = constant_speed * (t_deceleration - t_deceleration[0]) - 0.5 * abs(deceleration) * (t_deceleration - t_deceleration[0]) ** 2 + x_constant_speed[-1]
    x_final_pause = np.full_like(t_final_pause, x_deceleration[-1])

    # 合并时间和位移
    t_total = np.concatenate([t_initial_pause, t_acceleration[1:], t_constant_speed[1:], t_deceleration[1:], t_final_pause[1:]])
    x_total = np.concatenate([x_initial_pause, x_acceleration[1:], x_constant_speed[1:], x_deceleration[1:], x_final_pause[1:]])
    y_total = np.zeros_like(x_total)

    # 控制点设置和噪声
    num_control_points = 150 # 增加控制点数量
    control_points = np.linspace(0, len(t_total) - 1, num_control_points).astype(int)
    control_noise_x = np.random.normal(0, 0.2, num_control_points)  # 减小噪声标准差
    control_noise_y = np.random.normal(0, 0.18, num_control_points)

    # 创建B样条
    k = 3
    tck_x = BSpline(control_points, control_noise_x, k)
    tck_y = BSpline(control_points, control_noise_y, k)

    # 计算所有时间点的噪声
    noisy_x_total = x_total + tck_x(np.arange(len(t_total)))
    noisy_y_total = y_total + tck_y(np.arange(len(t_total)))

    # 生成输出文件路径
    noisy_trajectory_file_path = r"C:\Users\ASUS\Desktop\second_noisy_trajectory_fine_bspline.txt"
    with open(noisy_trajectory_file_path, "w") as file:
        for time, x, y in zip(t_total, noisy_x_total, noisy_y_total):
            file.write(f"{time:.2f}, {x:.2f}, {y:.2f}\n")

# 调用函数生成带细腻噪声的轨迹
generate_noisy_trajectory_fine_bspline()
