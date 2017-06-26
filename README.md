
ReadFile.py:
used to list the directory contents without using os.scandir, os.walk, glob.

SearchInsert.py :
The list can grow to a maximum length of 10. Make this limit as a configurable at

the instantiation part of the class.

○ The insert function should get a string as its argument, insert the string to

the list and return the index in which it was inserted. If the length of the list

reaches maximum length, the oldest item accessed with select should be

deleted and the new item should be inserted in its place.

○ The select function should accept an integer as argument and return the

value at that index in the list.
