#!/usr/bin/python3

def njoin(filename, outfn="", n=3, linesuffix=" "):
    if not outfn:
        outfn = filename + ".join"
    with open(filename) as infh, open(outfn, "w") as outfh:
        nline = 0
        for line in infh:
            if nline % n != n-1:
                line = line.rstrip() + linesuffix
            outfh.write(line)
            nline += 1
            
        
