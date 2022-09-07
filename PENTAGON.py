matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

""" Simple matrix solution proposed to me by friend on day ~3 of my studies"""
def PENTAGON(input):
    outputs = input[:]
    input.reverse()
    x = len(input)
    y = 0
    while y != x:
        z = input[y]
        y += 1
        for o in outputs:
            o.append(z[0])
            del z[0]
    print(outputs)

PENTAGON(matrix)

