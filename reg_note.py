import numpy as np

clp = open('My Clippings.txt', 'r')

# rest = open('rest.txt', 'w', encoding = 'utf-8')

lines = clp.readlines()
arr_lines = np.array(lines)

title = '被讨厌的勇气：“自我启发之父”阿德勒的哲学课 ((曰）岸见一郎，（日）古贺史健)\n'

# print(arr_lines[1]=='==========\n')
# print(arr_lines[np.where(arr_lines==title)])

# a tuple containing a numpy array of list of index
title_index = np.where(arr_lines==title)

title_output = []
for ele in title_index[0]:
    title_output.extend([ele+1, ele+2, ele+3, ele+4])

# print(title_output)
with open('note.txt', 'w+', encoding = 'utf-8') as note:
    for i in range(0, len(arr_lines[title_output])):
        note.write(arr_lines[title_output][i])

clp.close()
note.close()
# rest.close()
