class Programer(object):
 
        def __init__(self, name, age):
                self.name=name
		if isinstance(age, int):
               		self.age=age
                else:
			raise Exception('age must be int')
	def __eq__(self,other):
		if isinstance(other,Programer):
			if self.age==other.age:
				return True
			else:
				return False
		else:
			raise Exception('The type of object must be progrsmer')
	def __add__(self,other):
		if isinstance(other,Programer):
			return self.age+other.age
		else:
			raise Exception('The type of object must be progrsmer')


if __name__=='__main__':
        pr1=Programer('gao',25,)
        pr2=Programer('Bill',45)
        print pr1==pr2
        print pr1+pr2

