;;;;   execute at the linux prompt by issuing the command:
;;;;   > z3 hmwk2.smt2

(declare-const p1 Bool)
(declare-const p2 Bool)
(declare-const p3 Bool)
(declare-const p4 Bool)

(declare-fun dnf (Bool Bool Bool Bool) Bool)
(declare-fun cnf (Bool Bool Bool Bool) Bool)
(declare-fun bic (Bool Bool Bool Bool) Bool)

(assert (= (dnf p1 p2 p3 p4)
    	(or 
		(and p1 p2 p3 p4) 
		(and p1 p2 (not p3) (not p4)) 
		(and p1 p3 (not p2) (not p4)) 
		(and p1 p4 (not p2) (not p3)) 
		(and p2 p3 (not p1) (not p4)) 
		(and p2 p4 (not p1) (not p3)) 
		(and p3 p4 (not p1) (not p2))
		(and (not p1) (not p2) (not p3) (not p4))
	) ) )

(assert (= (cnf p1 p2 p3 p4)
	(and
		(or p1 p2 p3 (not p4))
		(or p1 p2 (not p3) p4)
		(or p1 (not p2) p3 p4)
		(or (not p1) p2 p3 p4)
		(or p1 (not p2) (not p3) (not p4))
		(or (not p1) p2 (not p3) (not p4))
		(or (not p1) (not p2) p3 (not p4))
		(or (not p1) (not p2) (not p3) p4)
	) ) )

(assert (= (bic p1 p2 p3 p4) (= p1 (= p2 (= p3 p4)))) )

;check that the above formulas are satisfiable
(check-sat)

;check DNF == CNF == BIC, by showing that not(dnf == cnf == bic) is unsatisfiable, 
;we show that dnf == cnf == bic is a tautology.
(define-fun test () Bool (= (dnf p1 p2 p3 p4) (cnf p1 p2 p3 p4) (bic p1 p2 p3 p4)))
(assert (not test))
(check-sat)




