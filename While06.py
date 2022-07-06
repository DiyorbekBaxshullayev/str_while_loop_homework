def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    a=0
    i=0
    s = str(s).lower()
    while i<len(s):
        if str(s[i]).isalpha():
            if str(s[i]) == "a" or str(s[i]) == "o" or str(s[i]) == "u" or str(s[i]) == "e" or str(s[i]) == "i":
                a+=0

            else:
                a+=1

        i+=1
    
    return a

print(main('CodeschoolUz'))
