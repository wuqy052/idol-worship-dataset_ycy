# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:44:51 2020
@author: qianying
adapted from https://blog.csdn.net/The_lastest/article/details/81027387
Chinese text segmentation 
For the analysis of Idol Worship Questionnaire
"""

# -*- coding: UTF-8 -*-
import jieba
import jieba.analyse
import jieba.posseg as pseg
import re
from collections import Counter
import matplotlib.pyplot as plt

# 1. row by row
cut_words1=[]
for line in rows:
    line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”（）！、…]", "", line)
    seg_list=jieba.cut(line,cut_all=False)
    cut_words1.append(" ".join(seg_list))

# 2. output 1 string
cut_words2=""
for line in rows:
    line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”（）！、…]", "", line)
    seg_list=jieba.cut(line,cut_all=False)
    cut_words2+=("，".join(seg_list))
    cut_words2+='，'
all_words=cut_words2.split()
c=Counter()
for x in all_words:
    if len(x)>1 and x != '\r\n':
        c[x] += 1
# keywords extraction
desc=list() # descriptions
weight=list() #weight of the description
keywords = jieba.analyse.extract_tags(cut_words2, topK=40, withWeight=True, allowPOS=('a','ad','an','ag','al','l','d'))
for item in keywords:
    desc.append(list(item)[0])
    weight.append(list(item)[1])
    print(item[0], item[1])
    

# 3. Output a list
cut_words3=list();
for line in rows:
    line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”（）！、…]", "", line)
    cut_words3+=jieba.lcut(line,cut_all=False)
c=Counter(cut_words3)

# count results
print('\n词频统计结果：')
for (k,v) in c.most_common(80): #output 20 most frequent words
    print("%s:%d"%(k,v))

# barplot
plt.rcParams['font.sans-serif']=['FangSong'] # Chinese
plt.figure(figsize=(10, 8), dpi=80) #generate a canvas
adj= ['真实','有趣','颜值','可爱','真诚','搞笑','乐观','好看','努力'] #adjatives
freq=[30,26,18,10,6,4,4,4,4] #frequency
x=range(len(adj))
plt.bar(x,freq,width=0.8, color='powderblue')
plt.xticks(x, adj)
plt.ylabel("频数", rotation=0, horizontalalignment="right",size=20)
plt.tick_params(labelsize=20)
plt.show()












