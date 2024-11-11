# 初始化解列表
solutions = []

# 遍历所有可能的组合
for x in range(0, 17):  # 男人最多16人，因为每个男人吃3元，超过16人就不够50元了
    for y in range(0, 26):  # 女人最多25人，因为每个女人吃2元，超过25人也不够50元了
        z = 30 - x - y  # 剩下的就是小孩的数量
        if 3 * x + 2 * y + z == 50:
            solutions.append((x, y, z))

# 输出所有解
print("所有可能的解：")
for sol in solutions:
    print(f"男人: {sol[0]}人, 女人: {sol[1]}人, 小孩: {sol[2]}人")

# 输出解的总数
print(f"总共有 {len(solutions)} 种方案")