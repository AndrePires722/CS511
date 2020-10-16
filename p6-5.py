from z3 import *

#ina0=inb0.
#(outa0 = ina0) & (outa1 = outa0 * ina0) & (outa2 = outa1 * ina0).
#outb0 = (inb0 * inb0) * inb0.

#end_of_list.

#formulas(goals).

#outa2 = outb0.

ina0,inb0,outa0,outa1,outa2,outb0 = Ints('ina0 inb0 outa0 outa1 outa2 outb0')

p1 = And((outa0==ina0),(outa1==outa0*ina0),(outa2==outa1*ina0))

v = Implies((And((ina0==inb0),p1,(outb0==(inb0*inb0)*inb0))),(outa2==outb0))

s = Solver()

s.add(v)
print("V:",s.check())

s.add(Not(v))
print("Not V:", s.check())
