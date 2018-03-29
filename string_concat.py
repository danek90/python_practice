names = ['Jeff', 'Gary', 'Jill', 'Samantha']

# for name in names:
# 	print "hello there, " + name

# 	print ' '.join(['Hello there, ', name])

#print ', '.join(names)

import os

# location_of_file = 'path/to/file'
# file_name = 'example.txt'

# ###reading files

# #this works but is not great.
# print location_of_file + 'file/path' + file_name

# #this is better
# with open(os.path.join(location_of_file, file_name)) as f:
# 	print f.read


###String formatting

who = 'Gary'
how_many = 12
# Gary bought 12 apples today

#bad method
print who, 'bought', how_many, 'apples today.'

#better way, needs index values for 2.7

print '{0} bought {1} apples today.'.format(who, how_many)