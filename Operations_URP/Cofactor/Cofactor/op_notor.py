'''
# Simple OR operation between a and c.
# Constraint:Neither a nor c can be null("00")
# c is complemented in the begining (b=c') .Then we proceed
# ahead by following these simple steps:
#
#  i) If a and b are equal, the result is equal to one of them
#  ii) If a="11"  the result is "11"
#  iii) If b="00", the result is a 
#  iii)Otherwise the result is "11"
'''

def op_notor(a,c):
    
    if a=="00" or c=="00":
        print "ERROR! 00 not a valid input"
        return

    if c=="11":
        b="00"
    elif c=="01":
        b="10"
    else:
        b="01"

    
    if a=="11":  
        s="11"
    elif a==b:
        s=a
    elif b=="00":
        s=a
    else:
        s="11"
    return s
