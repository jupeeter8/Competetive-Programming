# 290. Word Pattern
# Given a pattern and a string, find if string follows the pattern.
# If the pattern is "abba", then the string should be "dog cat cat dog".

# This means every character in the pattern should be mapped to a word and
# every word should be mapped to character.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Creating a list of words from the string
        s = list(s.split(" "))
        patlen = len(pattern)
        slen = len(s)

        # If the length of pattern and the list are not equal
        # return False
        if patlen != slen:
            return False
        # Approach 1: Using a dictionary
        # I will first create an array of lenght 26 That will map each character
        # To a word array, for example if a maps to dog then array[ord(a) - 97]
        # = dog

        # Then I will create a dictonary that will map each word to it's
        # position in the array
        dic = {}
        array = [""] * 26

        # Pointer to iterate through the pattern and the list
        x = 0

        while x < patlen and x < slen:

            # If the word s[x] is already in the dictionary
            if dic.get(s[x]) is not None:
                # Set the array at the position = s[x]
                # Once a word is mapped to a character, if another character
                # tries to map to the same word, word still goes to position
                # Stored in the dictionary
                array[dic.get(s[x])] = s[x]

            else:
                # If the word is not in the dictionary, then map in the
                # array and dictionary at position pattern[x] - 97
                # If a word is alredy mapped it will be over written
                # In the arrya but not in the dictionary
                array[ord(pattern[x]) - 97] = s[x]
                dic[s[x]] = ord(pattern[x]) - 97
            x += 1

        # Finally check if the array and the pattern match
        for i in range(patlen):
            if array[ord(pattern[i]) - 97] != s[i]:
                return False
        return True


def main():

    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))


main()

# Modification: We can check if the map pos in dic matches the current pos and
# we can also see if the current word id not overwriting a previous word
