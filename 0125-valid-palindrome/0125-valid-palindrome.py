class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        l = []
        r = []

        for i in range(len(s)):
            if s[i].isalnum():
                l.append(s[i])
        
        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                r.append(s[i])
        
        if l == r:
            return True
        
        return False




























        # s = s.lower()

        # list1 = []

        # for el in s:
        #     if el.isalnum():
        #         list1.append(el) 

        # list2 = []

        # for el in list1:
        #     list2.append(el)

        # list2.reverse()

        # if list1 != list2:
        #     return False
            
        # return True

