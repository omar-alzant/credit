from cs50 import get_int

nbr = get_int("Number :  ")
nbrs = str(nbr)

l = len(nbrs)

if nbrs[0] == '3' and (nbrs[1] == '7' or '4') and l == 15:
    print("AMEX")
elif nbrs[0] == '5' and (nbrs[1] == '1' or '2' or '3' or '4' or '5') and l == 16:
    print("MASTERCARD")
else:
    if nbrs[0] == '4' and l == 13 or l == 16:
        print("VISA")
    else:
        print("INVALID")
