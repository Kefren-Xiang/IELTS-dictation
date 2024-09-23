# 项目名称

这是一个用于翻译和训练单词的项目，包含两个 Python 脚本和一个 Excel 表格文件。

## 文件说明

- `List.xlsx`：Excel 文件，包含需要翻译的英文单词及其对应的中文翻译。
- `Translate.py`：用于将 `List.xlsx` 中未翻译的英文单词自动翻译为中文，并将结果保存回 Excel 文件。
- `Train.py`：用于通过单词训练的脚本，提供顺序模式和随机模式，帮助用户记忆翻译。

## 依赖库

项目中使用了以下第三方 Python 库：
- **pandas**：用于读取和处理 Excel 文件。
  - 安装方法：
    ```bash
    pip install pandas
    ```
- **googletrans**：用于将英文单词翻译成中文。
  - 安装方法：
    ```bash
    pip install googletrans==4.0.0-rc1
    ```

## 如何运行

1. 确保你已安装所有必要的依赖库。
2. 将 `List.xlsx` 文件与 `Translate.py`、`Train.py` 放在同一目录下。
3. 运行 `Translate.py`，自动将未翻译的英文单词翻译为中文：
    ```bash
    python Translate.py
    ```
4. 运行 `Train.py`，开始单词训练：
    ```bash
    python Train.py
    ```

## 注意事项

- 请确保 `List.xlsx` 文件中 "English" 列为英文单词，"Chinese" 列为对应的中文翻译。如果某个单词没有翻译，`Translate.py` 会自动为你翻译。
