def generate_trajectory():
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

    # 时间点
    t_initial_pause = np.linspace(0, initial_pause, initial_pause + 1)
    t_acceleration = np.linspace(initial_pause, initial_pause + acceleration_time, acceleration_time + 1)
    t_constant_speed = np.linspace(initial_pause + acceleration_time,
                                   initial_pause + acceleration_time + constant_speed_time, constant_speed_time + 1)
    t_deceleration = np.linspace(initial_pause + acceleration_time + constant_speed_time,
                                 initial_pause + acceleration_time + constant_speed_time + deceleration_time,
                                 deceleration_time + 1)
    t_final_pause = np.linspace(initial_pause + acceleration_time + constant_speed_time + deceleration_time,
                                initial_pause + acceleration_time + constant_speed_time + deceleration_time + final_pause,
                                final_pause + 1)

    # 位移计算
    x_initial_pause = np.zeros_like(t_initial_pause)
    x_acceleration = 0.5 * acceleration * (t_acceleration - initial_pause) ** 2
    x_constant_speed = constant_speed * (t_constant_speed - t_constant_speed[0]) + x_acceleration[-1]
    x_deceleration = constant_speed * (t_deceleration - t_deceleration[0]) - 0.5 * abs(deceleration) * (
                t_deceleration - t_deceleration[0]) ** 2 + x_constant_speed[-1]
    x_final_pause = np.full_like(t_final_pause, x_deceleration[-1])

    # 合并时间和位移
    t_total = np.concatenate(
        [t_initial_pause, t_acceleration[1:], t_constant_speed[1:], t_deceleration[1:], t_final_pause[1:]])
    x_total = np.concatenate(
        [x_initial_pause, x_acceleration[1:], x_constant_speed[1:], x_deceleration[1:], x_final_pause[1:]])
    y_total = np.zeros_like(x_total)

    # 生成输出文件
    with open("trajectory.txt", "w") as file:
        for time, x, y in zip(t_total, x_total, y_total):
            file.write(f"{time:.2f}, {x:.2f}, {y:.2f}\n")

    # return "trajectory.txt"


# 调用函数生成轨迹文件
trajectory_file = generate_trajectory()
# trajectory_file
