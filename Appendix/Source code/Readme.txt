
Introduction:
This prototype, which is used to compute the result R of forgetting some set V of atoms 
from a give CTL formula F (in the "Filename" below), is implemented in Prolog.  

1. How to run this prototype
1.1 Two method:
(1)Call "satCall(Filename, P, PN, ResultF)" in SWI-Prolog.
	Where "Filename" expresses the filename of the formula which we want to cope with, "P" is the number of atoms which we
want to forget, "PN" is a reserve parameter to extend our prototype in the future and "ResultF" is the folder name of the output.

(2) Call "new_ctlForget(F, V, Res, Ack, R, Exist,LenSNF, LenRes)" in SWI-Prolog.
	Where "F" is a CTL formula, "V" is the set of atoms to be forgotten, 
"Res" is the result of those steps before use the "Generalised Ackermann’s Lemma" and "remove the start", and 
"Ack" is result of using "Generalised Ackermann’s Lemma" (see below for more detail). (Ir Res is empty, then the 
result of forgetting V from F is  "true".)
...


1.2 Result (for (1) above, the one for (2) is obvious)
	The output, which has the same name with the formula, is in the folder of "ResultF" talked above. It contains the following
several items:
P1: the set of atoms to be forgotten.
T: the formula in the "Filename".
UsedTime: The CPU time cost for forgetting atoms in P1 from the formula in T.  
Res===========: the result of those steps before use the "Generalised Ackermann’s Lemma" and "remove the start".
ArcM===========: the result of using "Generalised Ackermann’s Lemma", i.e. a set of item "pair(X, Y)", in which X means the atom
that will be replaced and Y is the formula used to replace X.



Note: in our prototype, we only allow the following operators to be invisible or explicit for convenience.



2. Operators are the following:
&: and, \/: or,  -: not, ->: implies,  <->: equivalence 
@: global, ?: future, *: next,  $: until
~: forall, ^: exist 



3. Examples
(1) This is accordance with our example in the paper.

F = (~((p & q)$ (f \/ m)) & r), this is corresponding with the CTL formula (A((p and q) U (f or m)) and r).
V = [p, r],
then by calling the "new_ctlForget(F, V, Res, Ack, R, Exist,LenSNF, LenRes)" we have the following result:

Res=[formula_ind(ax,[x2],[[f,m,q]]),formula_ind(ax,[x2],[[f,m,x2]]),formula_ind(ax,[x2],[[q,x1]]),
formula_ind(ax,[x2],[[x1,x2]]),formula_ind(start,[start],[[f,m,q]]),formula_ind(start,[start],[[f,m,x2]]),
formula_ind(start,[start],[[q,x1]]),formula_ind(start,[start],[[x1,x2]]),formula_ind(start,[start],[[z]]),
formula_ind(true,[true],[[f,m,q,-z]]),formula_ind(true,[true],[[f,m,x2,-z]]),formula_ind(true,[true],[[q,x1,-z]]),
formula_ind(true,[true],[[-x1,f,m]]),formula_ind(true,[true],[[-x2,q]]),formula_ind(true,[true],[[-z,x1,x2]]),
formula_ind(af,[z],[[x1]])]

Ack=[pair(z, ((((~ ?x1)& (x1\/x2))& (q\/x1))& (f\/m\/x2))& (f\/m\/q)),pair(x1,f\/m), pair(w0, true)]

where, formula_ind(TempOp, Y, Z) expresses "Y -> TempOp Z", for example:
formula_ind(ax,[x2],[[f,m,q]]) means: x2 -> (~(*(f\/m\/q))).  

We can see that in this example x2, which introduced in the transformation process, can not be eliminated by our algorithm.
And in this case, Exist = 0.

(2) Let F = ((^ * ((a\/b)& (a->c)))& -c), V = [a], then by calling the "new_ctlForget(F, V, Res, Ack, R, Exist,LenSNF, LenRes)" we have the following result:

Res=[formula_ind(ex,[z],[[b,c],[x1]]),formula_ind(start,[start],[[z]]),formula_ind(start,[start],[[-c]]),formula_ind(true,[true],[[b,c,-x1]]),formula_ind(true,[true],[[-z,-c]])]

Ack=[pair(z,-c& (^ * ((b\/c)&x1))),pair(x1,b\/c)]

This means all the atoms introduce in the transformation can be eliminated with "x1" is replaced by "b\/c" and  "x2" is replaced by "-c& (^ * ((b\/c)&x1))".
And in this case, Exist = 1.