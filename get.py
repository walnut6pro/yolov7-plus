import numpy as np


def create_rounded_rectangle_trajectory(length, width, radius, num_points_per_edge):
    # 圆角的点数需要足够多，以确保平滑过渡
    num_points_per_corner = num_points_per_edge // 2

    # 计算圆角矩形的直边部分的点
    straight_edge_length = length - 2 * radius
    straight_edge_width = width - 2 * radius
    edge_xs = np.linspace(radius, straight_edge_length + radius, num_points_per_edge)
    edge_ys = np.linspace(radius, straight_edge_width + radius, num_points_per_edge)

    # 创建四个圆角的点
    corner_angles = np.linspace(np.pi, -np.pi, num_points_per_corner, endpoint=False)
    top_right_corner = radius * np.c_[np.sin(corner_angles[:num_points_per_corner // 4]),
    np.cos(corner_angles[:num_points_per_corner // 4])] + [length - radius, radius]
    bottom_right_corner = radius * np.c_[np.sin(corner_angles[num_points_per_corner // 4:num_points_per_corner // 2]),
    np.cos(corner_angles[num_points_per_corner // 4:num_points_per_corner // 2])] + [length - radius, width - radius]
    bottom_left_corner = radius * np.c_[
        np.sin(corner_angles[num_points_per_corner // 2:3 * num_points_per_corner // 4]),
        np.cos(corner_angles[num_points_per_corner // 2:3 * num_points_per_corner // 4])] + [radius, width - radius]
    top_left_corner = radius * np.c_[np.sin(corner_angles[3 * num_points_per_corner // 4:]),
    np.cos(corner_angles[3 * num_points_per_corner // 4:])] + [radius, radius]

    # 组合圆角矩形的边界点
    x_coords = np.concatenate((edge_xs[:-1],
                               top_right_corner[:, 0],
                               edge_xs[::-1][:-1] + (straight_edge_length - edge_xs[0]),
                               bottom_left_corner[:, 0],
                               edge_xs[:-1] - edge_xs[0],
                               bottom_right_corner[:, 0],
                               edge_xs[::-1][:-1],
                               top_left_corner[:, 0]))

    y_coords = np.concatenate((np.full(num_points_per_edge - 1, radius),
                               top_right_corner[:, 1],
                               np.full(num_points_per_edge - 1, width - radius),
                               bottom_left_corner[:, 1],
                               np.full(num_points_per_edge - 1, width - radius)[::-1],
                               bottom_right_corner[:, 1],
                               np.full(num_points_per_edge - 1, radius)[::-1],
                               top_left_corner[:, 1]))

    z_coords = np.zeros_like(x_coords)  # Z坐标为0

    # 时间戳
    timestamps = np.linspace(0, len(x_coords), len(x_coords), endpoint=False)

    return timestamps, x_coords, y_coords, z_coords


def write_to_txt(file_name, timestamps, x_coords, y_coords, z_coords):
    with open(file_name, 'w') as f:
        for t, x, y, z in zip(timestamps, x_coords, y_coords, z_coords):
            f.write(f"{t:.2f}\t{x:.2f}\t{y:.2f}\t{z:.2f}\n")
    return file_name


# 参数
length = 20.0  # 长度
width = 10.0  # 宽度
radius = 2.0  # 圆角半径
num_points_per_edge = 50  #  每条边的点数

# 生成圆角矩形的轨迹点
timestamps, x_coords, y_coords, z_coords = create_rounded_rectangle_trajectory(length, width, radius,
                                                                               num_points_per_edge)

# 文件保存路径
file_name = 'rounded_rectangle_trajectory.txt'

# 写入文件
output_file = write_to_txt(file_name, timestamps, x_coords, y_coords, z_coords)

