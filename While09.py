def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    c=0
    while i<len(s):
        if s[i].isdigit():
            c+=int(s[i])
        i+=1
    return c
print(main("123dh!@#64"))