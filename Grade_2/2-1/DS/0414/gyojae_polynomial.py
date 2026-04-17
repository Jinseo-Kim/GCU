class poly():
    def __init__(self, coef):
        self.coef = coef
        self.degree = len(coef)
    def print_poly(self):
        for i in range(self.degree):
            if i == self.degree-1:
                print("%d" % (abs(self.coef[i])))
            else:
                if self.coef[i] != 0.0:
                    print("%dx**%d" % (abs(self.coef[i]), self.degree-i-1), end='')
                if self.coef[i+1] >= 0:
                    print(" + ", end='')
                else:
                    print(" - ", end='')

def poly_add1(a, b) :
    z = []
    apos = bpos = cpos = 0
    degree_a = a.degree
    degree_b = b.degree

    while (apos <= degree_a) and (bpos <= degree_b ):
        if degree_a > degree_b :
            z.append(a.coef[apos])
            apos += 1
            degree_a -= 1
        elif degree_a == degree_b :
            z.append(a.coef[apos] + b.coef[bpos])
            apos += 1
            bpos += 1
        else :
            z.append(b.coef[bpos])
            degree_b -= 1
            bpos += 1
    return poly(z)

a = poly([3,0,0,0,6,3]) # creating the polynomial object.
b = poly([7,0,5,0,1])
c = poly_add1(a, b)
c.print_poly()