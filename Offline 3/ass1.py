d=dict()
with open("fl1.py") as f:
    for line in f:
        (name, dept, cgpa) = line.split('\t')
        cgpa=cgpa.rstrip("\n")
        d[str(name)]=[dept,cgpa]
f.close
print(d)
new_key=str(input("Enter the Name: "))
for key, value in d.items():
    if (new_key == key):
        new_cgpa= str(input("Enter the New CGPA: "))
        value[1] = new_cgpa
f1=open("fl1.py", "w")       
for key,value in d.items():
        std=key+"\t"+value[0]+"\t"+value[1]
        print(std, end="\n", file=f1)
        print("\n")
f1.close
