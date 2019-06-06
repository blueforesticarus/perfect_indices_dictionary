#Dictionary of cardinally specific ordinal numbers.
#List of cardinally unique lists of unique members.

v = ["a","e","i","o","u","oo","ie","ou","oi","ea","ia"]
#v = ["oo","ie","ou","oi","ea","ia"]
#c = ["b","k","d","f","g","h","j","l","m","n","p","r","s","t","v","w"]
c = ["s","n","h","b","k","d","f","g","j","l","m","p","r","t","v","w","z","y"]


str=""
def map(i, n):
    ii = i
    nn = n-i+1
    str = ""
    while nn != 0 or ii != 0:
        str += c[ nn % len(c) ]
        nn = nn // len(c)
        if ii or nn:
            str += v[ ii % len(v) ]
        ii = ii // len(v)
    suffix = str[-1]
    str = str[:-1]
    if suffix == "n":
        suffix = "nd"
    elif suffix == "s":
        suffix = "rst"
    elif suffix == "h":
        suffix == "rd"
    else: 
        suffix += "th"
    return str+ suffix

def read(str):
    if str[-2:] == "nd":
        str = str[:-2] + "n"
    
    elif str[-3:] == "rst":
        str = str[:-3] + "s"

    elif str[-2:] == "rd":
        str = str[:-2] + "h"
    elif str[-2:] == "th":
        str = str[:-2]

    import re
    pattern = re.compile(r"([%s])" % "".join(c) )
    str = re.sub(pattern, r"|\1|", str)

    units = str.split("|") 
    vmode = False
    ii = 0
    nn = 0

    vo = 1
    co = 1
    for char in units:
        if char == "":
            continue
        if vmode: 
            i = v.index(char)
            nn += i * vo  
            vo *= len(v) 
        else:
            i = c.index(char)
            ii += i * co  
            co *= len(c)
        vmode = not vmode

    return ii, nn, ii+nn-1

def main():
    for n in range(1, 20):
        for i in range(1, n+1):
            str = map(i,n)
            nn,ii,NN = read(str)
            print("%s -- %dth, %dth to last, out of %d" % (str,ii,nn,NN))
            assert NN == n
            assert ii == i

main()
