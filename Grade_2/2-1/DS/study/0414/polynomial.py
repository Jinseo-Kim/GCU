class polynomial():
    def __init__(self, coef):
        self.coef = coef
        self.degree = len(coef)-1

flag = 0
coef = [1, 0, 0, 4, 5]
coef2 = [6, 1, 0, 2, 4, 3]

poly = polynomial(coef)
poly2 = polynomial(coef2)

start = len(poly.degree) - len(poly2.degree)


print(f'max degree: {poly.degree}')
for idx, value in enumerate(poly.coef):
    if value == 1:
        print(f'x^{poly.degree-idx}', end ="")
    elif (poly.degree-idx) == 0:
        print(f'{value}', end ="")
    elif value != 0:
        print(f'{value}x^{poly.degree-idx}', end ="")
    
    if value != 0 and poly.degree-idx != 0:
        print("+", end ="")
    