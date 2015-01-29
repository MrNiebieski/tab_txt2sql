from Tkinter import Tk
from tkFileDialog import askopenfilename
import re
import cStringIO as StringIO

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(filetypes=[("txt Files","*.txt")]) # show an "Open" dialog box and return the path to the selected file
tablename = filename.rstrip(".txt")
#print tablename
outname = tablename + ".sql" 
print outname
re_tab = re.compile("\t")
re_return = re.compile("\n")
with open(filename) as infile:
	line_list = infile.readlines()
	outs = StringIO.StringIO()
	for i, line in enumerate(line_list):
		result = re_tab.sub("','", line)
		result = re_return.sub("'),\n", result)
		result = "('" + result
		if i is 0:
			outs.write("INSERT INTO `%s` "%tablename.split("/")[-1])
			result = re.sub("'","`",result)
			outs.write(result)
			outs.seek(-2,2)
			outs.write(" VALUES\n")
		else:
			outs.write(result)
	outs.seek(-2,2)
	outs.write(';')
	with open(outname,"w") as fout:
		fout.write(outs.getvalue())
	print outs.getvalue()