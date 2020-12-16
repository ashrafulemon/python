#51 : introduction to oop(object orianted )
# class and object

class student :
	roll = ""
	gpa  = ""

rahim = student()
rahim.roll =101
rahim.gpa =3.44

karim = student()
karim.roll =102
karim.gpa =3.66

print(f"rahim\n roll:{rahim.roll},\n gpa:{rahim.gpa}")
print(f"karim\n roll:{karim.roll},\n gpa:{karim.gpa}")
print(isinstance(rahim,student))