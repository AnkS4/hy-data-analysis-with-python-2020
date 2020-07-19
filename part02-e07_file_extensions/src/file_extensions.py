#!/usr/bin/env python3

def file_extensions(filename):
	d = {}
	l = []
	with open(filename, 'r') as f:
		for i in f:
			if '.' in i:
				s = i.split('.')
				k = s[-1].strip()
				value = i.strip()
				if k not in d:
					d[k] = [value]
				else:
					d[k].append(value)
			else:
				l.append(i.strip())
	return (l, d)

def main():
    l, d = file_extensions("src/filenames.txt")
    print(f"{len(l)} files with no extension")
    for i in sorted(d.keys()): #d.items()
    	print(f"{i} {len(d[i])}")

if __name__ == "__main__":
    main()
