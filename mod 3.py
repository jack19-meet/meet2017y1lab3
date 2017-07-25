Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> ​ "Don't" + "forget" + "to" + "conserve" + "water"
SyntaxError: invalid character in identifier
>>> "Don't" + "forget" + "to" + "conserve" + "water"
"Don'tforgettoconservewater"
>>> 'Don't' + ' forget' + 'to' + ' conserve ' +
'water'
SyntaxError: invalid syntax
>>> 'rakan    ' * 50
'rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    rakan    '
>>> "the"*3 + "beautiful" + "Earth"
'thethethebeautifulEarth'
>>> "the "*20 + "beautiful" + "Earth"
'the the the the the the the the the the the the the the the the the the the the beautifulEarth'
>>> 2 * 'true'
'truetrue'
>>> a = 'save
SyntaxError: EOL while scanning string literal
>>> a = 'save'
>>> b = 'the'
>>> c = 'earth'
>>> print'a + b + c'
SyntaxError: invalid syntax
>>> abc
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> a
'save'
>>> a b c
SyntaxError: invalid syntax
>>> b
'the'
>>> a + b + c
'savetheearth'
>>> a = 4
>>> b = pandabears
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b = pandabears
NameError: name 'pandabears' is not defined
>>> b = 'pandabears'
>>> a + b
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 'a + b'
'a + b'
>>> a
4
>>> b
'pandabears'
>>> a + b
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a+b
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a = '4'
>>> a+b
'4pandabears'
>>> my = 'name'
>>> len(my)
4
>>> test = (meet)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    test = (meet)
NameError: name 'meet' is not defined
>>> test = 'meet'
>>> test.upper()
'MEET'
>>> a = “MEET”
b = “meet” c = “Meat”
SyntaxError: invalid character in identifier
>>> a = “MEET”
b = “meet” c = “Meat”
SyntaxError: invalid character in identifier
>>> a = 'MEET'
>>> b = 'meet'
>>> c = 'Meat
SyntaxError: EOL while scanning string literal
>>> c = 'Meat'
>>> a == b
False
>>> a == c
False
>>> b == c
False
>>> a != b
True
>>> 2 == 3
False
>>> 2 != 4
True
>>> 2 != 3
True
>>> 2 != 2
False
>>> my_string = 'thinkBig'
>>> my_string = 'thinkBIG'
>>> meet_value = 'alexadamfarahkatamir'
>>> len(my_string)
8
>>> meet_value[0:8]
'alexadam'
>>> meet_value = 'alexadam'
>>> meet_value== my_string
False
>>> my_string
'thinkBIG'
>>> len(meet_value) == len(my_string)
True
>>> my_string = “bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: invalid character in identifier
>>> my_string = 'bananayellowthinkhatgreyBIGcalifornia314'
>>> meet_value = my_string [12:16]
>>> meet_value
'thin'
>>> meet_value = my_string [12:17] + [24:27]
SyntaxError: invalid syntax
>>> meet_value = my_string [12:17] + my_string [24:27]
>>> meet_value
'thinkBIG'
>>> meet_value.upper()
'THINKBIG'
>>> meet_value.lower()
'thinkbig'
>>> meet_value.replace('t' , 'd')
'dhinkBIG'
>>> 
