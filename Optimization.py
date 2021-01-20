from gekko import GEKKO

# Objective function: x1+x2
# constraint1 : x1>=10
# constraint2 : x1^2+x2^2>100



m= GEKKO(remote=True)


x1,x2 = [m.Var() for i in range(2)]


x1.value = 0
x2.value = 1


m.Equation(x1>10)
m.Equation(x1**2+x2**2>100)

m.Obj((x1+x2))

m.options.IMODE=3

m.solve()

print('x1 = ', str(x1.value))
print('x2 = ', str(x2.value))

