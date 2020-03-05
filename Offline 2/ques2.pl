neighbor(i,a,35). neighbor(i,b,45). neighbor(a,c,20).
neighbor(a,d,30). neighbor(b,d,25). neighbor(b,e,35).
neighbor(b,f,27). neighbor(c,d,30). neighbor(c,g,47).
neighbor(d,g,30). neighbor(e,g,25).

lenpath(X,Y,L):-neighbor(X,Y,L).
lenpath(X,Y,L):-neighbor(X,Z,L1),lenpath(Z,Y,L2),L is L1+L2.
