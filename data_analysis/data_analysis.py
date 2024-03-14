import jieba
import re
import os
import matplotlib.pyplot as plt

plot_n = 10 # 展示的前n个词的数量
def plot(word_count, n):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置

    plt.xlabel('词')
    plt.ylabel('次数')
    plt.title('中文词出现的次数')

    x_label = []
    y = []
    i = 1
    for word, num in word_count:
        if len(x_label) > n:
            break
        x_label.append(word)
        y.append(num)

    first_bar = plt.bar(range(len(y)), y, color='blue')  # 初版柱形图，x轴0-9，y轴是列表y的数据，颜色是蓝色
    plt.xticks(range(len(x_label)), x_label)

    for data in first_bar:
        y = data.get_height()
        x = data.get_x()
        plt.text(x + 0.15, y, str(y), va='bottom')  # 0.15为偏移值，可以自己调整，正好在柱形图顶部正中

    plt.savefig("./data_analysis/word_frequency.png")
    plt.show()

def main():
    with open('../Test/orig.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    text = re.sub(r'[\n\s\.,.，。、’“”:：;!！?？()（）"\'\-]', "", data)
    word_count = {}
    words = jieba.cut(text)
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    print(word_count)
    result_path = 'word_frequency.txt'
    os.remove(result_path)
    with open('word_frequency.txt', 'a', encoding='utf-8') as f:
        for word, num in word_count:
            f.write(f"{word}：{num}" + '\n')
    # 绘图
    plot(word_count, plot_n)
if __name__ == '__main__':
    main()