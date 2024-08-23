# import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import pydot
import matplotlib.image as mping

os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'

# txt 파일에서 값 가져오기: tt_list
def read_truthtable(file_name):
    tt_vars = []
    tt_list = []
    tt = open(file_name, 'r')
    tt_vars = tt.readline().strip()
    for line in tt.readlines()[1: ]: # 첫째 줄 제외 한 줄씩 각 리스트의 원소로 저장됨
        temp = line.strip().split()
        tt_list.append(temp)
    tt.close()
    return tt_vars, tt_list

# node 그리기
g = pydot.Dot(graph_type = 'digraph')

vars, l = read_truthtable('Carry.txt')

n = 8
node_num = 0

parent = dict()
parent[(n, 0)] = None

i = 0

def draw_tree(n, node_num):
    global i

    current_node = (n, node_num)

    if node_num == 0:
        u = pydot.Node(str(current_node), label = f'.')
        g.add_node(u)
        
    else:
    # current node의 parent와 current node 간 edge 그리기
        u = pydot.Node(str(parent[current_node]), label = f'{vars[parent[current_node][0]]}', style = 
                    'filled', fillcolor = 'lightblue')
        g.add_node(u)

        v = pydot.Node(str(current_node), label = f'{vars[n]}')
        g.add_node(v)

        edge = pydot.Edge(str(parent[current_node]), str(current_node))
        g.add_edge(edge)

    if n <= 1:
    # node for base
        u = pydot.Node(str(current_node), label = f'{vars[n]}')
        g.add_node(u)

        v = pydot.Node(str((n, i)), label = f'{n}', shape = 'plaintext')
        g.add_node(v)

        edge = pydot.Edge(str(current_node), str((n, i)), dir = 'backward')
        g.add_edge(edge)
        return n
    
    i += 1
    child = (n - 1, i)
    parent[child] = current_node

    print(i, n) # i 초기화 안됨
    return draw_tree(*child)
    
draw_tree(8, 0)

graph_image_path = 'graph.png'
g.write_png(graph_image_path)

# matplotlib을 사용하여 이미지 시각화
img = mpimg.imread(graph_image_path)
plt.imshow(img)
plt.axis('off')  # 축 숨기기
plt.show()
