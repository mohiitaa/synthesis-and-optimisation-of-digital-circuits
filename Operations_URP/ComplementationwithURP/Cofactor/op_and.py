'''
# Simple AND operation between a and b.
# Constraint:Neither a nor b can be null("00")
# Simple steps:
#  i) If a and b are equal, the result is equal to one of them
#  ii) If a="11" or b="11", the result is b or a i.e if a ="11" a(AND)b=b.
#      Similarly,it goes the other way round
#  iii)Otherwise the result is null
'''

def op_and(a,b):
    if a=="00" or b=="00":
        print("ERROR! 00 not a valid input")
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
