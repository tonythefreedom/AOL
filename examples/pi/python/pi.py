# Gregory-Leibniz formula for 'pi'
# http://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
def calcPi(n):
    pi,numer = 0,4.0
    for i in range(n):
        denom = (2*i+1)
        term = numer/denom
        if i%2:
            pi -= term
        else:
            pi += term
    return(pi)


# here we use 16000 terms - try higher numbers, and lower ones too
print(calcPi(999999))