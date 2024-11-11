# 初始化解列表
solutions = []

# 遍历所有可能的组合
for x in range(0, 6):  # 1元硬币最多5枚，因为每枚1元，超过5枚就不够5元了
    for y in range(0, 11):  # 5角硬币最多10枚，因为每枚5角，超过10枚也不够5元了
        z = 50 - 10 * x - 5 * y  # 剩下的就是1角硬币的数量
        if z >= 0:  # 确保1角硬币的数量是非负的
            solutions.append((x, y, z))

# 输出所有解
print("所有可能的解：")
for sol in solutions:
    print(f"1元硬币: {sol[0]}枚, 5角硬币: {sol[1]}枚, 1角硬币: {sol[2]}枚")

# 输出解的总数
print(f"总共有 {len(solutions)} 种方案")