''' op_and is stored in the subpackage Operations of CS.
 Constraint:Neither a nor b can be null("00")
 Simple AND operation between a and b.
 Simple Steps:
 i) If a and b are equal, the result is one of them.
 ii) If either one of them is 11, the result is the other implicant.
       i.e if a is "11", a OR b=b. Similarly the other way round 
 iii) Else the result is "00"
'''

def op_and(a,b):

    if a=="00" or b=="00":
        print "ERROR! 00 not a valid input"
        return
    if a==b:
        s=b
    elif a=="11":
        s=b
    elif b=="11":
        s=a
    else:
        s="00"
    return s
