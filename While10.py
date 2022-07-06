def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a=0
    i=0
    while i<len(s):
        if str(s[i]).isdigit():
            if int(s[i])%2==1:
                a+=int(s[i])

            else:
                a+=0
            i+=1
    
    return a
print(main('12342'))
