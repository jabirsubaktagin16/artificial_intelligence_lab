parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka').
parent('Rashid' , 'Hasib'). parent('Hasib', 'Kabir'). parent('Sohel', 'Anika').

female('Rebeka'). female('Anika').

aunt(X,Z):-parent(Y,X),parent(P,Y),parent(P,Z),female(Z),(Y\=Z).

findAunt:-write('Name:'),read(X),write('Aunt:'),
	aunt(X,Z),write(Z),tab(5),fail.
findAunt.
