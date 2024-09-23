import pandas as pd
import random

# 读取当前目录下的 Excel 文件 'List.xlsx'
df = pd.read_excel('List.xlsx')

# 确保数据没有空值
df.dropna(subset=['English'], inplace=True)

# 提供模式选择
mode = input("请选择模式（1: 顺序模式，2: 随机模式）\n请注意，你可以随时输入exit以退出：")

if mode == '1':
    # 顺序模式
    for index, row in df.iterrows():
        english_word = row['English']
        correct_answer = row['Chinese']
        
        # 提问用户
        print(f"你知道 '{english_word}' 的中文意思吗？")
        user_answer = input("请输入你的答案: ")

        # 检查答案是否正确
        if user_answer == correct_answer:
            print("回答正确！")
        elif user_answer == 'exit':
            break
        else:
            print(f"回答错误，正确答案是: {correct_answer}")
        print()  # 输出空行，便于阅读

elif mode == '2':
    # 随机模式，重复150遍
    for i in range(150):
        index = random.randint(0, len(df) - 1)
        english_word = df.iloc[index]['English']
        correct_answer = df.iloc[index]['Chinese']
        
        # 提问用户
        print(f"第 {i+1} 题: 你知道 '{english_word}' 的中文意思吗？")
        user_answer = input("请输入你的答案: ")

        # 检查答案是否正确
        if user_answer == correct_answer:
            print("回答正确！")
        elif user_answer == 'exit':
            break
        else:
            print(f"回答错误，正确答案是: {correct_answer}")
        print()  # 输出空行，便于阅读

elif mode == 'exit':
    #直接退出
    pass

else:
    print("无效的选择，请重新运行程序并选择有效的模式。")

print("测试完成！")
