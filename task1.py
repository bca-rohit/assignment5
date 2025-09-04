dic={ "john": 49,"mike":78,"michael":85,
      "alan": 58}
name=input("enter a name: ")
if name in dic:
    print("{} marks:".format(name),dic[name])
else:
    print("Student not found")