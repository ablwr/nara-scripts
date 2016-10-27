import os, re, glob

file = 'm384-import-1.xml'
filenames = glob.glob("*.xml")

counter = 2
outputfile = file

print 'Combining XML files...'
for fname in filenames:  	
	in_size = (os.stat(fname).st_size / 1000000)
	try:
		out_size = (os.stat(file).st_size / 1000000)
	except OSError:
		out_size = 0
	if (in_size + out_size) > 75:
		file = re.split('\.', outputfile)[0] + '_' + str(counter) + '.xml'
		counter = counter + 1
	with open(file, 'a') as outfile:   
		with open(fname) as infile:
			for line in infile:
				outfile.write(line)
print "Complete."
