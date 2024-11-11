'''
巨噬细胞分裂2：为了探究巨噬细胞对新冠病毒的杀伤能力，需要培养巨噬细胞。如果初始值
=27，按刚才的规则分裂 ，研究人员要得到10W个巨噬细胞，最少需要多长时间？
'''

initial_value = 27
target_value = 100000
hours = 0
current_value = initial_value

while current_value < target_value:
    current_value = current_value * 2 - 1
    hours += 1

print(f"得到 10W 个巨噬细胞最少需要 {hours} 小时。")

'''











'''