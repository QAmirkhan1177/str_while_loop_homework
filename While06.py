def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    i=0
    c=0
    while i<len(s):
        if s[i].lower()!="a" and s[i].lower()!="e" and s[i].lower()!="i" and  s[i].lower()!="o" and s[i].lower()!="u" and not s[i].isdigit():
            c+=1
        i+=1
    return c
print(main("sdfgaeih2343jklsdf"))    