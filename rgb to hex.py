def rgb(r, g, b):
    output = ""
    table = {0: "0",
             1: "1",
             2: "2",
             3: "3",
             4: "4",
             5: "5", 
             6: "6",
             7: "7",
             8: "8", 
             9: "9",
             10: "A",
             11: "B",
             12: "C",
             13: "D",
             14: "E",
             15: "F"}

    rrest = r % 16
    rrest = int(rrest)
    rval = (r - rrest) / 16
    rval = int(rval)

    grest = g % 16
    grest = int(grest)
    gval = (g - grest) / 16
    gval = int(gval)

    brest = b % 16
    brest = int(brest)
    bval = (b - brest) / 16
    bval = int(bval)

    if r < 0:
        rval = 0
        rrest = 0
    if r > 255:
        rval = 15
        rrest = 15

    if g < 0:
        gval = 0
        grest = 0
    if g > 255:
        gval = 15
        grest = 15

    if b < 0:
        bval = 0
        brest = 0
    if b > 255:
        bval = 15
        brest = 15

    output += table[rval]
    output += table[rrest]
    output += table[gval]
    output += table[grest]
    output += table[bval]
    output += table[brest]
    
    print(output)
    
    return output



rgb(20, 155, 25)
rgb(200, 145, 25)
rgb(20, 0, 125)