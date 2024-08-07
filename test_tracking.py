def generate_noisy_trajectory():
    import numpy as np

    # 设定参数
    initial_pause = 10  # 初始静止时间
    acceleration_time = 10  # 加速时间
    constant_speed_time = 40  # 匀速时间
    deceleration_time = 10  # 减速时间
    final_pause = 10  # 最终静止时间
    acceleration = 0.1  # 加速度
    deceleration = -0.1  # 减速度
    constant_speed = 0.7  # 匀速
    noise_sigma_x = 0.05  # 噪声标准差
    noise_sigma_y = 0.15
    time_interval = 0.1  # 时间间隔

    # 时间点
    t_initial_pause = np.arange(0, initial_pause, time_interval)
    t_acceleration = np.arange(initial_pause, initial_pause + acceleration_time, time_interval)
    t_constant_speed = np.arange(initial_pause + acceleration_time, initial_pause + acceleration_time + constant_speed_time, time_interval)
    t_deceleration = np.arange(initial_pause + acceleration_time + constant_speed_time, initial_pause + acceleration_time + constant_speed_time + deceleration_time, time_interval)
    t_final_pause = np.arange(initial_pause + acceleration_time + constant_speed_time + deceleration_time, initial_pause + acceleration_time + constant_speed_time + deceleration_time + final_pause, time_interval)

    # 位移计算
    x_initial_pause = np.zeros_like(t_initial_pause)
    x_acceleration = 0.5 * acceleration * (t_acceleration - initial_pause) ** 2
    x_constant_speed = constant_speed * (t_constant_speed - t_constant_speed[0]) + x_acceleration[-1]
    x_deceleration = constant_speed * (t_deceleration - t_deceleration[0]) - 0.5 * abs(deceleration) * (t_deceleration - t_deceleration[0]) ** 2 + x_constant_speed[-1]
    x_final_pause = np.full_like(t_final_pause, x_deceleration[-1])

    # 合并时间和位移
    t_total = np.concatenate([t_initial_pause, t_acceleration[1:], t_constant_speed[1:], t_deceleration[1:], t_final_pause[1:]])
    x_total = np.concatenate([x_initial_pause, x_acceleration[1:], x_constant_speed[1:], x_deceleration[1:], x_final_pause[1:]])
    y_total = np.zeros_like(x_total)

    # 添加噪声
    noisy_x_total = x_total + np.random.normal(0, noise_sigma_x, x_total.shape)
    noisy_y_total = y_total + np.random.normal(0, noise_sigma_y, y_total.shape)

    # 生成输出文件
    noisy_trajectory_file_path = r"C:\Users\ASUS\Desktop\second_car_noisy_trajectory_gt.txt"
    with open(noisy_trajectory_file_path, "w") as file:
        for time, x, y in zip(t_total, noisy_x_total, noisy_y_total):
            file.write(f"{time:.2f}, {x:.2f}, {y:.2f}\n")

    # return noisy_trajectory_file_path

# 调用函数生成带噪声的轨迹文件
noisy_trajectory_file = generate_noisy_trajectory()