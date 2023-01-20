# -*- coding: utf-8 -*-
"""CSE422_lab1_Task1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ekp83DSHF4STwQi5_Qdg9WnlcUbet5QR
"""

# TASK-1:
file = open('E:\\BRAC Study\\CSE422\\Lab1\\input.txt')

fdata = file.read()

file2 = open('E:\\BRAC Study\\CSE422\\Lab1\\output.txt', 'w')

data = fdata.split('\n')

data_matrix = []

for i in range(len(data)):
   data_matrix.append([])

   for j in data[i]:

       if j == 'N':
           data_matrix[i].append(0)

       if j == 'Y':
           data_matrix[i].append(1)

row = len(data_matrix)
col = len(data_matrix[0])

visited_matrix = []

for i in range(row):
   visited_matrix.append([0] * col)

# up,down,side,diagonal co-ordinates
# lower axis, middle axis, upper axis
up_dw_s_d = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

max_people = 0


def dfs(visited_matrix, data_matrix, i, j, up_dw_s_d, row, col, count):
   global max_people

   visited_matrix[i][j] = 1

   for k in up_dw_s_d:
       row2, col2 = i + k[0], j + k[1]

       if (row2 >= 0 and row2 < row):

           if (col2 >= 0 and col2 < col):

               if data_matrix[row2][col2] != visited_matrix[row2][col2]:
                   count += 1
                   max_people = max(max_people, count)
                   dfs(visited_matrix, data_matrix, row2, col2, up_dw_s_d, row, col, count)


for i in range(row):
   for j in range(col):
       if data_matrix[i][j] != visited_matrix[i][j]:
           dfs(visited_matrix, data_matrix, i, j, up_dw_s_d, row, col, 1)

print(max_people)
file2.write(str(max_people))
