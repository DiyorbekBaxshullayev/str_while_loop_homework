def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    i=0 
    while i < len(s):
        if str(s[i]).islower():
            a+=1
        i+=1
    
    return a

print(main('CodeschoolUz'))
