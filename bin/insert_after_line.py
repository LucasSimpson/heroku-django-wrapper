import sys

# get system arguments
filename = sys.argv [1]
line_to_find = sys.argv [2]
line_to_insert = sys.argv [3]

# read file and strip of \n
f = open (filename, 'r')
lines = [line.rstrip () for line in f.readlines ()]
f.close ()

# find the FIRST INSTANCE of the line_to_find, insert line_to_insert, then break
for a in range (len (lines)):
	if lines [a] == line_to_find:
		lines.insert (a+1, line_to_insert)
		break

# put the \n back in
lines = [line + '\n' for line in lines]

# write modified lines to file
f = open (filename, 'w')
for a in lines:
    f.write (a)
f.close ()