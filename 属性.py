class Programer(object):
	happy='play computer'
	def __init__(self, name, age, weight):
		self.name=name
		self._age=age
		self.__weight=weight
	@classmethod
	def get_happy(cls):
		return cls.happy
	@property
	def get_wight(self):
		return self.__weight
	def self_in(self):
		print 'My name is %s\nI am %s years old\n'%(self.name,self._age)


if __name__=='__main__':
	programer=Programer('gao',25,80)
	print dir(programer)
	print Programer.get_happy()
	print programer.__dict__
	print programer.get_wight
	print programer._Programer__weight
	print programer.self_in()
