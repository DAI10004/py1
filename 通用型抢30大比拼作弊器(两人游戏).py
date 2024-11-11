'''
原始游戏：从1开始顺序数数，每次只能数1-2个数，谁先
数到30谁胜。新要求：从任意数开始，比如从5开始；每次可以数n个数，比如每次最多4个，怎么取
胜？
'''

def cheat_game(start_num, max_count, target_num):
    multiple = max_count + 1
    key_num = (target_num - start_num) % multiple
    if key_num == 0:
        return 0
    return multiple - key_num

def play_game(start_num, max_count, target_num):
    current_num = start_num
    while current_num < target_num:
        opponent_move = int(input("对方数几个数？"))
        current_num += opponent_move
        print(f"当前数字变为：{current_num}")
        if current_num >= target_num:
            print("对方获胜了。")
            break
        cheat_move = cheat_game(current_num, max_count, target_num)
        print(f"你应该数{cheat_move}个数。")
        current_num += cheat_move

start_num = int(input("请输入起始数字："))
max_count = int(input("请输入每次最多数的个数："))
target_num = int(input("请输入目标数字："))
play_game(start_num, max_count, target_num)