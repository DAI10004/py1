import math
import random

def show_menu():
    print("欢迎使用系统功能菜单")
    print("1. 计算 Pi (使用 math 库)")
    print("2. 计算 Pi (使用级数)")
    print("3. 估计 Pi (使用随机采样)")
    print("4. 退出系统")
    choice = input("请输入您的选择(1-4): ")
    return choice

def calculate_pi_with_math():
    print("Pi is:", math.pi)

def calculate_pi_with_series(terms=1000000):
    pi = 0
    for n in range(terms):
        term = (-1)**n / (2*n + 1)
        pi += term
    pi *= 4
    print("Calculated Pi is:", pi)

def estimate_pi_with_sampling(num_samples=1000000):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if (x**2 + y**2) < 1:
            inside_circle += 1
    pi_estimate = (inside_circle / num_samples) * 4
    print("Estimated Pi is:", pi_estimate)

def exit_system():
    print("感谢使用，再见！")
    exit(0)

def main():
    while True:
        choice = show_menu()
        if choice == '1':
            calculate_pi_with_math()
        elif choice == '2':
            calculate_pi_with_series()
        elif choice == '3':
            estimate_pi_with_sampling()
        elif choice == '4':
            exit_system()
        else:
            print("无效输入，请重新选择！")

if __name__ == "__main__":
    main()