seriessum(0,_,_,0):- !.
seriessum(N,I,F,S2):- N1 is N-1, seriessum(N1,I,F,S1), S2 is S1+F+(N-1)*I.

