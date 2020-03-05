parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka').
parent('Rashid' , 'Hasib'). grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

findGp :- write('Grandchild: '), read(X), write('Grandparent: '),
		grandparent(Y,X), write(Y), tab(5), fail.
findGp.
