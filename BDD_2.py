# import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# 1. Carry.txt BDD 그리기
s = ['x3', 'x2', 'x1', 'x0', 'y3', 'y2', 'y1', 'y0']
# s = [['x3'], ['x2'], ['x1'], ['x0'], ['y3'], ['y2'], ['y1'], ['y0']]

# 읽어와도 될 것 같은데 -> 그러면 또 txt 파일 바꿔야 됨.

tt1 = open('Carry.txt','r')
g = nx.Graph()

# node 그리기: x3 ~ y_0까지 8개를 트리 모양으로 쭉 펼친다.
for i in range(len(s)):
    for num in range(2**i):
        g.add_node(s[i] + f'_{num}')
g.add_node('0')
g.add_node('1')

# edge 그리기
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        g.add_edge(s[i], s[j])
g.add_edge('y0', '0')
g.add_edge('y0', '1')


# 좌표 설정: 트리 모양
import random

pos = {}
for i in s:
    pos[s[i]] = (random.random(), 1-i/4)
pos['0'] = (0, -1)
pos['1'] = (1, -1)

nx.draw(g, pos, with_labels = True)
plt.show()


