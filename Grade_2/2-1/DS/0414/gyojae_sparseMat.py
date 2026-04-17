class sparse_matrix():
    def __init__(self, data, rows, cols):
        self.data = data
        self.cols = cols
        self.rows = rows
        self.terms = len(data)
        
def print_matrix(self): 
    pass

def matrix_add(a, b):
    z = []
    apos = bpos = 0

    while (apos < a.terms) and (bpos < b.terms):
        inda = a.data[apos][0] * a.cols + a.data[apos][1]
        indb = b.data[bpos][0] * b.cols + b.data[bpos][1]

        if inda < indb:
            z.append(a.data[apos])
            apos += 1
        elif inda == indb:
            z.append([a.data[apos][0], a.data[apos][1], a.data[apos][2] + b.data[bpos][2]])
            apos += 1
            bpos += 1
        else:
            z.append(b.data[bpos])
            bpos += 1

    # 남은 데이터들 처리 (루프 밖으로 나옴)
    while (apos < a.terms):
        z.append(a.data[apos])
        apos += 1
    while (bpos < b.terms):
        z.append(b.data[bpos])
        bpos += 1

    return sparse_matrix(z, a.rows, a.cols) # 함수 마지막에 반환
    
a = sparse_matrix( [[1, 1, 5], [2, 2, 9]], 3, 3)
b = sparse_matrix( [[0, 0, 5], [2, 2, 9]], 3, 3)
c = matrix_add(a, b)
print(f'{c.data}, {c.cols}, {c.rows}')