class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_pairs.values():
                stack.append(char)
            elif char in bracket_pairs.keys():
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False
            else:
                return False

        return not stack
    
    pass

  

