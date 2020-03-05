parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka').
parent('Rashid' , 'Hasib').
female('Rebeka').

brother(X, Z) :- parent(Y,X), parent(Y,Z),not(female(Z)),(X \= Z).

findBro:-write('Name:'), read(X), write('Brother:'),
	brother(X,Z),write(Z),tab(5),fail.
findBro.
