eq='4x^2 + 4x +   (-8) = 0'

eq=eq.replace(' ','').replace(')','').replace('(','').replace('\'','').split('+')
a=int(eq[0].replace('x^2',''))
b=int(eq[1].replace('x',''))
c=int(eq[2].replace('=0',''))
print('a is',a, ',b is', b,',c is',c)

import math
x_1=(-b+math.sqrt(abs(b**2-4*a*c)))/(2*a)
x_2=(-b-math.sqrt(abs(b**2-4*a*c)))/(2*a)
print(x_1,x_2)