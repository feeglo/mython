#!/usr/bin/env python
# -*-coding: utf-8 -*-

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


	def self_in(self):
		print 'My name is %s\nMy favorite language is %s\n'%(self.name,self.language)

def introduce(programer):
		if isinstance(programer,Programer):
			programer.self_in()


if __name__=='__main__':
	programer=Programer('gao',25,80)
	backprogramer=Backprogramer('gao',25,80,'Python')
        introduce(programer)
        introduce(backprogramer)

