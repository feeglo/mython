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

class Backprogramer(Programer):
	
	def __init__(self, name, age, weight, lan):
		super(Backprogramer,self).__init__(name, age, weight)
		self.language=lan

if __name__=='__main__':
        programer=Backprogramer('gao',25,80,'Python')
        print dir(programer)
        print Programer.get_happy()
        print programer.__dict__
        print programer.get_wight
        print programer._Programer__weight
	print programer.self_in()
	print type(programer)
	print isinstance(programer, Programer)
