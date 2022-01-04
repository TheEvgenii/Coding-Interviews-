n  =  10 
temp = format(5,"b")
bitmask = n 
bitmask |= (bitmask >> 1)
print(bitmask ^ n)