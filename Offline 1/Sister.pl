parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka').
parent('Rashid' , 'Hasib').
female('Rebeka').

sister(X, Z) :- parent(Y,X), parent(Y,Z),female(Z),(X \= Z).

findSis:-write('Name:'), read(X), write('Sister:'),
	sister(X,Z),write(Z),tab(5),fail.
findSis.
