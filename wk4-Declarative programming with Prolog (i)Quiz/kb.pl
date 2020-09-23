%q1%
eats(X,Y):-likes(X,Y).
eats(X,Y):-hungry(X),edible(Y).


%q3%
reflection(point(X,Y), point(Y,X)).

%q5%
/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

diagnosis(no_lenses, _,_, RATE) :- low_tear_rate(RATE).
diagnosis(hard_lenses, AGE, yes, RATE) :- young(AGE), normal_tear_rate(RATE).
diagnosis(soft_lenses, AGE, no, RATE) :- young(AGE), normal_tear_rate(RATE).


%q6%
directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).

contains(X,Y):-directlyIn(Y,X).
contains(X,Y):-directlyIn(Z,X), contains(Z,Y).


%q7%
solution(V1,V2,V3,H1,H2,H3):-
	word(V1,_,V11,_,V12,_,V13,_),
	word(V2,_,V21,_,V22,_,V23,_),
	word(V3,_,V31,_,V32,_,V33,_),
	word(H1,_,V11,_,V21,_,V31,_),
	word(H2,_,V12,_,V22,_,V32,_),
	word(H3,_,V13,_,V23,_,V33,_).

%q8%
mirror(leaf(X),leaf(X)).
mirror(tree(X,Y), tree(A,B)) :- mirror(Y,A), mirror(X,B).