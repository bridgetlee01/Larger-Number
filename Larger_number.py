# This function prints true if a > b, false if a=b or a<b

def larger_number(a, b):
    if len(a) > len(b):
        return True
    elif len(b) > len(a):
        return False
    elif len(a) == len(b):
        for i in range(len(a)):
            if a[i] == b[i]:
                continue
            elif a[i] > b[i]:
                return True
            elif a[i] < b[i]:
                return False
        return False


print(larger_number("134", "136"))
print(larger_number("132", "125"))