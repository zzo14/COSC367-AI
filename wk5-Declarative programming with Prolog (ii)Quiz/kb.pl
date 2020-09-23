%q1%
second([_|[X|_]], X).


%q2%
swap12([S, H|T], [H,S|T]).


%q3%
listtran([],[]).
listtran([H1|T1], [H2|T2]) :- tran(H1, H2), listtran(T1, T2).


%q4%
twice([],[]).
twice([H|T1],[H|[H|T2]]) :- twice(T1,T2).


%q5%
remove(_, [], []).
remove(X, [H|T], L) :- X=H, remove(X, T, L).
remove(X, [H|T1], [H|T2]) :- remove(X, T1, T2).


%q6%
split_odd_even([], [], []).
split_odd_even([X], [X], []).
split_odd_even([H1, H2|T], [H1|O], [H2|E]) :- split_odd_even(T, O, E).


%q7%
preorder(leaf(A), L) :- append([A],[], L).
preorder(tree(ROOT, LEFT, RIGHT), L) :- append([ROOT], LEVEL, L), 
    append(L1, L2, LEVEL),
    preorder(LEFT, L1),
    preorder(RIGHT, L2).
