import sys
import os
import jieba
import jieba.analyse  
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.metrics.pairwise import cosine_similarity  
import re

STOP_WORDS = ['我','的', '了']
# 文本预处理函数  
def preprocess_text(text):  
    text = delete_punct(text)
    words = jieba.cut(text)  
    filtered_words = [word for word in words if word not in STOP_WORDS]
    return ' '.join(filtered_words)  
  
# 计算TF-IDF向量  
def compute_tfidf_vectors(texts):  
    vectorizer = TfidfVectorizer()  
    tfidf_matrix = vectorizer.fit_transform(texts)  
    return tfidf_matrix, vectorizer  
  
# 计算余弦相似度  
def compute_cosine_similarity(tfidf_matrix, index1, index2):  
    similarity = cosine_similarity(tfidf_matrix[index1:index1+1], tfidf_matrix[index2:index2+1])  
    return similarity[0][0]  

def check_command(argv):
    """
    检查命令行文件路径数量是否正确并检查两个待检测的文件是否存在，保存结果的目录路径夹是否存在。
    """
    if len(argv) != 4:
        raise ValueError("parameter error!")
    
    original_path = sys.argv[1]
    plagiarized_path = sys.argv[2]
    result_path = sys.argv[3]
    
    try:
        with open(original_path, 'r',encoding='utf-8') as f:
            original_txt = f.read()
    except FileNotFoundError :
        raise"ERROR: original_path not found!"

    try:    
        with open(plagiarized_path, 'r',encoding='utf-8') as f:
            plagiarized_txt = f.read()
    except FileNotFoundError :
        raise"ERROR: plagiarized_path not found!"

    result_file,_ = os.path.split(result_path)
    if not os.path.isdir(result_file):
        raise FileNotFoundError("result_file not found!")
    
    return original_txt,plagiarized_txt,result_path

def get_duplicate_checking(original_txt, plagiarized_txt):
    tfidf_matrix, _ = compute_tfidf_vectors([original_txt, plagiarized_txt])
    
    # 计算相似度  
    return compute_cosine_similarity(tfidf_matrix, 0, 1)  

def delete_punct(text):
    # 使用正则表达式删除符号
    return re.sub(r'[\n\s,.，。、’“”:：;!！?？()（）"\'\-]', "", text)

def main():
    original_txt, plagiarized_txt, result_path = check_command(argv=sys.argv)
    original_txt = preprocess_text(original_txt)
    plagiarized_txt = preprocess_text(plagiarized_txt)

    result = get_duplicate_checking(original_txt, plagiarized_txt) * 100
    print(f"文本相似度: {result}")
    with open(result_path, 'w', encoding='utf-8') as f:
        f.write(f"{sys.argv[2]}的查重率为：{result}%")

if __name__ == '__main__':
    main()

  

