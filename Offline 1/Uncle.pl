parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka').
parent('Rashid' , 'Hasib'). parent('Hasib', 'Kabir'). parent('Sohel', 'Anika').

female('Rebeka'). female('Anika').

uncle(X,Z):-parent(Y,X),parent(P,Y),parent(P,Z),not(female(Z)),(Y\=Z).

findUncle:-write('Name:'),read(X),write('Uncle:'),
	uncle(X,Z),write(Z),tab(5),fail.
findUncle.
