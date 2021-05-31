infile = open ('people.txt', 'r')
outfile=open('names-formated.txt', 'w')
contents = infile.read()
print(contents.title(),file=outfile)
infile.close
outfile.close