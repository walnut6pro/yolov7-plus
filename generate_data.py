# 读取原始文本文件
with open(r'E:\true_moving_output.txt', 'r') as f:
    lines = f.readlines()

# 处理每一行数据
output_lines = []
for line in lines:
    # 分割每一行的数据
    data = line.split()
    if len(data) >= 4:
        # 修改第三列和第四列的值
        data[2] = '-2.1'
        data[3] = '1'
    # 将修改后的行添加到输出列表
    output_lines.append(' '.join(data) + '\n')

# 将输出列表写入新的文本文件
with open(r'E:\true_moving_output_.txt', 'w') as f:
    f.writelines(output_lines)