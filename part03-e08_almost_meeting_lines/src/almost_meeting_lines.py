#!/usr/bin/python3

import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):
    op = np.linalg.lstsq([[a1, -1], [a2, -1]], [-b1, -b2])
    return op[0], bool(op[2]==2)
    '''
    try:
        op = np.linalg.solve([[a1, -1], [a2, -1]], [-b1, -b2])
        f = True
    except np.linalg.LinAlgError:
        op = np.linalg.lstsq([[a1, -1], [a2, -1]], [-b1, -b2])[0]
        f = False
    return op, f
    '''

def main():
    a1=1
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()
