def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    c=0
    while i<len(s):
        if s[i].isdigit() and int(s[i])%2==1:
            c+=1
        i+=1
    return c
print(main("123dh!@#64"))