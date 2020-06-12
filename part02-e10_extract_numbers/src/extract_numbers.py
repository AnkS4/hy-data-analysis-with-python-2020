#!/usr/bin/env python3

import re

def extract_numbers(s):
    #s = re.findall(r'([+-]?\d+[.]?\d*)',s)
    s = s.split()
    l = []
    for i in s:
        try:
            l.append(int(i))
        except (ValueError):
            try:
                l.append(float(i))
            except Exception:
                pass
    return l

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
