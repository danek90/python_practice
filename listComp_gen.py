# #comomn generator
# for i in range(5):
# 	print(i)

# ### List comp. that stores data in memory
# xyz = [i for i in range(5)]
# print(xyz)

# # same as 

# xyz = []
# for i in range(5):
# 	xyz.append(i)
# print(xyz)	

# ### This is a generator though, does not store in memory.

# xyz = (i for i in range(5))
# print(xyz)

#### MORE stuff

input_list = [5,6,2,10,15,20,5,1,3]

def dive_by_five(num):
	if num % 5 == 0:
		return True
	else:
		return False

xyz = (i for i in input_list if dive_by_five(i))

# #written out
# for  i in input_list:
# 	if dive_by_five(i):
# 		xyz.append(i)
#----------------------
# for i in xyz:
# 	print(i)

# or you could say this. a one-liner for loop. iterating over a generator.
#[print(i) for i in xyz]
#print(xyz)

xyz = [i for i in input_list if dive_by_five(i)]
#print(xyz)

[[print(i, ii) for ii in range(5)] for i in range(5)] 

## identical to:

for i in range(5):
	for ii in range(5):
		print(i, ii)

xyz = ([[i, ii] for ii in range(5)] for i in range(5))

print(xyz)

print([i for i in xyz])