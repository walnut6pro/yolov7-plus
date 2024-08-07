def extract_data(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    extracted_data = []
    for i in range(1, len(lines)):
        line = lines[i]
        columns = line.strip().split(',')
        first_column = str(int(columns[0]) / 10000000000)
        eighth_column = columns[7]
        ninth_column = columns[8]
        tenth_column = columns[9]
        extracted_data.append(' '.join([first_column, eighth_column, ninth_column, tenth_column]))

    with open(output_file, 'w') as f:
        f.write('\n'.join(extracted_data))

    print(f"提取的数据已保存到 {output_file} 中。")

input_file = r'D:\yolov7-main_2\yolov7-main\true.txt'  # 输入文件名
output_file = r'D:\yolov7-main_2\yolov7-main\true2.txt'  # 输出文件名

extract_data(input_file, output_file)