# import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

import pydot

# txt 파일에서 값 가져오기: tt_list
def read_truthtable(file_name):
    tt_list = []
    tt = open(file_name, 'r')
    for line in tt.readlines()[1: ]: # 첫째 줄 제외 한 줄씩 각 리스트의 원소로 저장됨
        temp = line.strip().split()
        tt_list.append(temp)
    tt.close()
    return tt_list

# node 그리기
g = nx.generators.classic.balanced_tree(2, 8) # 수정
# g = pydot.Dot(graph_type = 'graph')
pos = nx.spring_layout(g)

g.add_node('num0')
g.add_node('num1')
pos['num0'] = (-1, -1)
pos['num1'] = (1, -1)


# edge, 가중치 추가하기

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

# 트리 그래프를 시각화:

plt.figure(figsize=(12, 12))
nx.draw(g, pos, with_labels = True, edge_color = edge_colors, node_size = 50, node_color = "lightblue", font_size = 5)
plt.show()

# for node, (x, y) in pos.items():
#     if node >= 256:
#         plt.text(x, y, s = tt_list[i][8]) # s_out

