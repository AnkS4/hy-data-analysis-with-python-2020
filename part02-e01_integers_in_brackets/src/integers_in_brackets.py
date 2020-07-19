#!/usr/bin/env python3

import re

def integers_in_brackets(s):
	mo = re.findall(r'\[\s*([+-]?\d+)\s*\]', s)
	mo = [int(i) for i in mo]
	#mo = list(map(int, mo))
	return mo

def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
