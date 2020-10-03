from z3 import *

x,y,z,u = Ints('x y z u')

Animal = Function('Animal', IntSort(), BoolSort())
Wolf = Function('Wolf', IntSort(), BoolSort())
Fox = Function('Fox', IntSort(), BoolSort())
Bird = Function('Bird', IntSort(), BoolSort())
Caterpillar = Function('Caterpillar', IntSort(), BoolSort())
Snail = Function('Snail', IntSort(), BoolSort())
Grain = Function('Grain', IntSort(), BoolSort())
Plant = Function('Plant', IntSort(), BoolSort())
Smaller = Function('Smaller', IntSort(), IntSort(), BoolSort())
Eats = Function('Eats', IntSort(), IntSort(), BoolSort())



s = Solver()


s.add(ForAll([x],Implies(Wolf(x),Animal(x))))
s.add(ForAll([x],Implies(Fox(x),Animal(x))))
s.add(ForAll([x],Implies(Bird(x),Animal(x))))
s.add(ForAll([x],Implies(Caterpillar(x),Animal(x))))
s.add(ForAll([x],Implies(Snail(x),Animal(x))))
s.add(ForAll([x],Implies(Grain(x),Plant(x))))

s.add(Exists([x], Wolf(x)))
s.add(Exists([x], Fox(x)))
s.add(Exists([x], Bird(x)))
s.add(Exists([x], Caterpillar(x)))
s.add(Exists([x], Snail(x)))
s.add(Exists([x], Grain(x)))


s.add(ForAll([x],(Implies((Animal(x)),(Or(
	(ForAll([y],Implies((Plant(y)),(Eats(x,y))))),
	(ForAll([z],Implies((And((Animal(z)),(Smaller(z,x)),(Exists([u],(And(Plant(u),Eats(z,u))))))),(Eats(x,z)))))
))))))

s.add(ForAll([x,y],(Implies(And(Caterpillar(x),Bird(y)),Smaller(x,y)))))
s.add(ForAll([x,y],(Implies(And(Snail(x),Bird(y)),Smaller(x,y)))))
s.add(ForAll([x,y],(Implies(And(Bird(x),Fox(y)),Smaller(x,y)))))
s.add(ForAll([x,y],(Implies(And(Fox(x),Wolf(y)),Smaller(x,y)))))
s.add(ForAll([x,y],(Implies(And(Bird(x),Caterpillar(y)),Eats(x,y)))))

s.add(ForAll([x],(Implies((Caterpillar(x)),(Exists([y],And(Plant(y),Eats(x,y))))))))
s.add(ForAll([x],(Implies((Snail(x)),(Exists([y],And(Plant(y),Eats(x,y))))))))

s.add(ForAll([x,y],Implies((And(Wolf(x),Fox(y))),(Not(Eats(x,y))))))
s.add(ForAll([x,y],Implies((And(Wolf(x),Grain(y))),(Not(Eats(x,y))))))
s.add(ForAll([x,y],Implies((And(Bird(x),Snail(y))),(Not(Eats(x,y))))))

s.add(Exists([x,y],(And(Animal(x),Animal(y),Eats(x,y),(ForAll([z],Implies(Grain(z),Eats(y,z))))))))

s.add(Exists([x,y],And(Wolf(x),Snail(y),Smaller(x,y))))

print s.check()
