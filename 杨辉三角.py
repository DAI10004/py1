n = 10  # 定义杨辉三角的行数
triangle = []

for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)

# 计算最大宽度，用于对齐输出
max_width = len(' '.join(map(str, triangle[-1])))

for row in triangle:
    # 使用center方法进行居中对齐
    print(' '.join(map(str, row)).center(max_width))