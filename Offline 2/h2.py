in_state=[(1,1,2),
          (2,1,3),
          (3,2,1),
          (8,1,1),
          (4,2,3),
          (7,3,2),
          (6,2,2),
          (5,3,3)]

goal_state=[(1,1,1),
            (2,1,2),
            (3,1,3),
            (8,2,1),
            (4,2,3),
            (7,3,1),
            (6,3,2),
            (5,3,3)]

distance=0

for i in range(8):
    distance+=abs(in_state[i][1]-goal_state[i][1])+abs(in_state[i][2]-goal_state[i][2])

print('Heuristics 2:',distance)
