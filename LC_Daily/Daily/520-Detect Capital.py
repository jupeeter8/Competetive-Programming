# 520. Detect Capital
# We have to check if the word is in all caps, all lower case or only the first letter is capital

def detect_capital():
    n = len(word)
        pos = 0
        
        # Check if all the letters are in upper case
        # We Loop until the first lower case letter is found
        while pos < n and word[pos].isupper():
            pos += 1

        # If I have found multiple upper case letters but not all
        # of the them, then the word is not all caps
        # return False
        if pos > 1 and pos < n:
            return False

        # I check the remaining letters to be all small case
        # If I find a capital letter, then I return Flase
        # Because it Uppercase can not come after Lowercase
        while pos < n:
            if not word[pos].islower():
                return False
            pos += 1
        return True