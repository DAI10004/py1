# 初始化解列表
solutions = []

# 遍历所有可能的组合
for x in range(0, 21):  # 鸡翁最多20只，因为每只5钱，超过20只就不够100钱了
    for y in range(0, 34):  # 鸡母最多33只，因为每只3钱，超过33只也不够100钱了
        z = 100 - x - y  # 剩下的就是鸡雏的数量
        if 15 * x + 9 * y + z == 300:
            solutions.append((x, y, z))

# 输出所有解
print("所有可能的解：")
for sol in solutions:
    print(f"鸡翁: {sol[0]}只, 鸡母: {sol[1]}只, 鸡雏: {sol[2]}只")