#!/usr/bin/env python

import sys

def usage():
    print >> sys.stderr, "Usage: python %s <filename>" % (sys.argv[0])


def main():
#    hello()
#    print "Program arguments are: ", sys.argv
#    print "Number of arguments is: ", len(sys.argv)
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    try:
        fp = open(sys.argv[1], "r")
    except IOError, e:
        print >> sys.stderr, "Argument is not a valid filename"
        usage()
        sys.exit(1)
    min1 = float(11.1)
    max1 = float(0.1)
    prenume1=" "
    prenume2=" "
    nume1=" "
    nume2=" "
    for idx, line in enumerate(list(fp)):
        a=line.split('\t')
        if max1 < float(a[3]):
            max1=float(a[3])
            prenume1=a[0]
            nume1=a[1]
        if min1 > float(a[3]):
            min1=float(a[3])
            prenume2=a[0]
            nume2=a[1]
    print "max: %s %s %s" % (prenume1, nume1, max1)
    print "min: %s %s %s" % (prenume2, nume2, min1)
if __name__ == "__main__":
    sys.exit(main())
