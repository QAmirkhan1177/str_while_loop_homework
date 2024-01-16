def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    c=0
    while i<len(s):
        if not s[i].isalpha() and not s[i].isdigit() and not s[i].isspace():
            c+=1
        i+=1              
    return c
print(main("bulls1234@*%$&#"))