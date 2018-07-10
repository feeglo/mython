#!/bin/bash
people={
'Bob':{'ph':'1234',
	'add':'foo drive 12'
},
'Li':{
	'ph':'1245',
	'add':'bar street 42'
},
'Gao':{
	'ph':'4569',
	'add':'Baz street 56'
}
}
lab={'ph':'phone numbber',
	'add':'address'
}
name=raw_input('Name:')
requst=raw_input('phone number (p) or address(a)?')
if requst=='p':key='ph'
if requst=='a':key='add'

if name in people:print "%s's %s is %s."% \ (name,lab[key],people[name][key])
