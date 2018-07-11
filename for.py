print('Now let us do something about "for" and "while"\n let go')
number=input('suppose we input name and age output \n"xxx is xx years old"\n now please input the numbwer of peoplo what you want:')
names=[]
ages=[]
while number!=0:
	name=raw_input('input name:')
	names.append(name)
	age=input('input his age:')
	ages.append(age)
	number=number-1
print'will input'
for na,ag in zip(names,ages):
	print na,'is', ag,'years old'
