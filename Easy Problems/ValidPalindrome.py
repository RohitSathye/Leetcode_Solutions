class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True

        s_new = (''.join(letter for letter in s if letter.isalnum()))

        if(s_new.lower() == s_new[::-1].lower()):
            return True
        else:
            return False
        