print "Check if you are running this file from the same directory as the document"
fname = raw_input('Enter the file name:')


fh = open(fname)
fn = open('result.txt','w')
set1 = set()
count = 0

for line in fh:
	line.rstrip()
	for word in list(line.split()):
		if '@' in word:
			if '.' in word:
				set1.add(word)
				count += 1

for item in set1:
	fn.write(item)
	fn.write("\n")

print "Results stored in result.txt. Previous data will be overwritten (if any)"
print count,"distinct email-ids extracted"
