import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# 1. 가장 기본 형태 BDD 그리기

# https://frhyme.github.io/python-lib/nx_layout_for_tree/ 참조

# 각 노드는 2개의 자식을 가지고, 트리의 높이는 9 (변수 9개)
g = nx.generators.classic.balanced_tree(2, 9)
pos = nx.spring_layout(g)

# 트리 그래프를 시각화: 이거 트리 형태로는 안되나?  
plt.figure(figsize=(12, 12))
nx.draw(g, pos, with_labels=True, node_size=50, node_color="lightblue", font_size=8, edge_color="gray")
plt.show()

# 각 edge에 가중치를 가해보자

