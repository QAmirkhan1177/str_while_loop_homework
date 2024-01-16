def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    c=0
    while i<len(s):
        if s[i].isalpha():
            c+=1
        i+=1
    return c
print(main("bulls1234"))
