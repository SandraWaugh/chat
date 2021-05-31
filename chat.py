def read_file(filename):
	lines = []
	with open(filename,"r",encoding = "UTF-8") as f:
		for line in f:
			lines.append(line.strip())  #去掉換行符號
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines: 
		if line == "Sandra":
			person = "Sandra"
			continue
		elif line == "Mini":
			person = "Mini"
			continue
		if person:
			new.append(person + ":" + line)	
	return new

def write_file(filename,lines):
	with open(filename,"w",encoding = "UTF-8") as f:
		for line in lines:
			f.write(line + "\n")

def main():
	lines = read_file("input.txt")
	print(lines)
	lines = convert(lines)
	write_file("output.txt",lines)

main()