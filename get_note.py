import numpy as np
import re


clp = open('My Clippings.txt', 'r')

# rest = open('rest.txt', 'w', encoding = 'utf-8')

lines = clp.readlines()
arr_lines = np.array(lines)

title = '被讨厌的勇气：“自我启发之父”阿德勒的哲学课 ((曰）岸见一郎，（日）古贺史健)\n'

# a tuple containing one numpy array of index as the only element
title_index = np.where(arr_lines==title)

# store the np.array of title index in title_index
title_index = title_index[0]


def get_a_blob(ind, source):
    # ind: the index of title
    # source: the source array
    # return a list of three elements(position, \n, content)
    blob = []
    blob.extend([ source[ind+1], source[ind+2], source[ind+3] ])
    return blob

# a nested list, of which every inner list is a blob
output_blobs = []
for ele in title_index:
    output_blobs.append( get_a_blob(ele, arr_lines) )

# trim off words in position line of every blob, leave only one position interger
for item in output_blobs:
    item[0] = int(re.findall(r'[0-9]+', item[0])[0])

# by default the notes in 'My Clippings.txt' is ordered by the time you made the note,
# this would be troublesome when you read a book more than 1 time and make additional notes
# So sort by position is more reasonable.
output_blobs.sort()

# print(len(output_blobs[0]))
with open('note.txt', 'w+', encoding = 'utf-8') as note:
    for i in range(0, len(output_blobs)):
        # convert int to str, else write() will not accept
        note.write(str(output_blobs[i][0]))
        for j in range(1, 3):
            note.write(output_blobs[i][j])

clp.close()
note.close()
# rest.close()
