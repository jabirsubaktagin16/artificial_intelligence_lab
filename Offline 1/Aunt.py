tupleList1=[('parent', 'Hasib', 'Rakib'),('parent', 'Rakib', 'Sohel'),('parent', 'Hasib', 'Kabir'),
             		('parent', 'Rakib', 'Rebeka'),('parent', 'Rashid', 'Hasib'),('parent','Sohel','Anika'),('parent','Rebeka','Zahir')]
female=[('Rebeka'),('Anika')]

# Procedure to find the Aunt of X
X=str(input("Nephew/Niece's Name:"))
print('Aunt:', end=' ')
i=0
while(i<=3):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(4):
            if((tupleList1[j][0]=='parent')&(tupleList1[i][1]==tupleList1[j][2])):
               for k in range(4):
                   if ((tupleList1[k][0] == 'parent') & ( tupleList1[j][1] == tupleList1[k][1])&( tupleList1[k][2] in female)&(tupleList1[j][2] != tupleList1[k][2])):
                      print(tupleList1[k][2], end=' ')
    i=i+1
