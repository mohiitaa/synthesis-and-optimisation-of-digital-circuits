''' op_or is stored in the subpackage Operations of CS.
 Constraint:Neither a nor b can be null("00")
 Simple OR between a and b
 Simple Steps:
 i) If either a or b is "11", then the result is "11"
 ii) If they are equal, the result is one of them
 iii) Else just return one of them
'''
def op_or(a,b):
    if a=="00" or b=="00":
        print "ERROR! 00 not a valid input"
        return
    if a=="11" or b=="11":
        s="11"
    elif a==b:
        s=a
    else:
        s="11"
    return s
