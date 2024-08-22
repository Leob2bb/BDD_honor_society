# import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# 1. 가장 기본 형태 BDD 그리기

# txt 파일에서 값 가져오기
tt1_list = []

tt1 = open('Carry.txt', 'r')
for line in tt1.readlines()[1: ]: # 한 줄씩 각 리스트의 원소로 저장됨
    temp = line.strip().split()
    tt1_list.append(temp)
tt1.close()

# node 그리기
# https://frhyme.github.io/python-lib/nx_layout_for_tree/ 참조
# 각 노드는 2개의 자식을 가지고, 트리의 높이는 9 (변수 9개)
g = nx.generators.classic.balanced_tree(2, 9)
pos = nx.spring_layout(g)

# edge, 가중치 추가하기: 노드의 홀짝성 같으면 가중치 1, 아니면 0
for u, v in g.edges():
    if (u + v)%2 == 0:
        g[u][v]['weight'] = 1
    else:
        g[u][v]['weight'] = 0

# 가중치에 따라 색깔 지정하기
edge_colors = []
for u, v, data in g.edges(data = True):
    weight = data['weight']
    if weight == 0:
        edge_colors.append('green')
    else:
        edge_colors.append('red')

# 트리 그래프를 시각화: 이거 트리 형태로는 안되나?  
plt.figure(figsize=(12, 12))
nx.draw(g, pos, with_labels = True, edge_color = edge_colors, node_size = 50, node_color = "lightblue", font_size = 5)
plt.show()

# 각 edge에 가중치를 가해보자

