# import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# 1. Carry.txt BDD 그리기
s = ['x3', 'x2', 'x1', 'x0', 'y3', 'y2', 'y1', 'y0', '0', '1']
# 읽어와도 될 것 같은데 -> 그러면 또 txt 파일 바꿔야 됨.

tt1 = open('Carry.txt','r')
g = nx.Graph()

# node 그리기
for i in range(len(s)):
    g.add_node(s[i])

# edge 그리기
for i in range(len(s)-2):
    for j in range(i+1, len(s)):
        g.add_edge(s[i], s[j])


# 좌표 설정
pos = {}
for i in range(len(s)):
    pos[s[i]] = (i%3/3, i//3/3)

nx.draw(g, pos, with_labels = True)
plt.show()


