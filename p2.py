from z3 import *

# declaring propositional variables x,y
p1,p2,p3,p4 = Bools('p1 p2 p3 p4')

# DNF
dnf = 	Or(
		And(p1,p2,p3,p4),
		And(p1,p2,Not(p3),Not(p4)),
		And(p1,p3,Not(p2),Not(p4)),
		And(p1,p4,Not(p2),Not(p3)),
		And(p2,p3,Not(p1),Not(p4)),
		And(p2,p4,Not(p1),Not(p3)),
		And(p3,p4,Not(p1),Not(p2)),
		And(Not(p1),Not(p2),Not(p3),Not(p4))
	)
#CNF
cnf =	And(
		Or(p1,p2,p3,Not(p4)),
		Or(p1,p2,Not(p3),p4),
		Or(p1,Not(p2),p3,p4),
		Or(Not(p1),p2,p3,p4),
		Or(p1,Not(p2),Not(p3),Not(p4)),
		Or(Not(p1),p2,Not(p3),Not(p4)),
		Or(Not(p1),Not(p2),p3,Not(p4)),
		Or(Not(p1),Not(p2),Not(p3),p4)

	)
#BIC - biconditional
bic = p1 == (p2 == (p3 == p4))

s = Solver()
s.add(dnf)
s.add(cnf)
s.add(bic)

# check that the above formulas are satisfiable
print s.check()

#check DNF == CNF == BIC, by showing that not(dnf == cnf == bic) is unsatisfiable, 
#we show that dnf == cnf == bic is a tautology.
s.add(Not(dnf==cnf))
print s.check()
