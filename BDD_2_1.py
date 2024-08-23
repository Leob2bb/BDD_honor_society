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
# 각 노드는 2개의 자식을 가지고, 트리의 높이는 7
g = nx.generators.classic.balanced_tree(2, 8) # 수정

g.add_node('num0')
g.add_node('num1')

# edge, 가중치 추가하기: 노드의 홀짝성 같으면 가중치 1, 아니면 0

for u in g.nodes(): # 수정필요
    g.add_edge(str(u), 'num0')
for u in range(511):
    g.add_edge(str(u), 'num1')

for u, v in g.edges():
    # if (u + v)%2 == 0:
    g[u][v]['weight'] = 1
    # else:
    #     g[u][v]['weight'] = 0

# 가중치에 따라 색깔 지정하기
edge_colors = []
for u, v, data in g.edges(data = True):
    weight = data['weight']
    if weight == 0:
        edge_colors.append('green')
    else:
        edge_colors.append('red')

# 트리 그래프를 시각화:
pos = nx.spring_layout(g)

plt.figure(figsize=(12, 12))
nx.draw(g, pos, with_labels = True, edge_color = edge_colors, node_size = 50, node_color = "lightblue", font_size = 5)
plt.show()

# 트리 끝부분에 0 또는 1 표시
# i = 0
# for node, (x, y) in pos.items():
#     if node >= 256:
#         plt.text(x, y, s = tt1_list[i][8]) # s_out
#         if EOFError:
#             break
#         i += 1
