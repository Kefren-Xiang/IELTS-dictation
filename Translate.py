import pandas as pd
from googletrans import Translator

# 初始化翻译器
translator = Translator()

# 读取当前目录下的 Excel 文件 'List.xlsx'
df = pd.read_excel('List.xlsx')

# 确保数据没有空值
df.dropna(subset=['English'], inplace=True)

# 对于尚未翻译的单词进行翻译
for index, row in df.iterrows():
    if pd.isna(row['Chinese']) or row['Chinese'] == '':
        english_word = row['English']
        translated_text = translator.translate(english_word, src='en', dest='zh-cn').text
        df.at[index, 'Chinese'] = translated_text
        print(f"翻译: {english_word} -> {translated_text}")

# 将结果保存回原始 Excel 文件
df.to_excel('List.xlsx', index=False)

print("翻译完成，未翻译的单词已补充翻译")
