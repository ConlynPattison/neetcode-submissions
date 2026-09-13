class Solution:
    def isValid(self, s: str) -> bool:
        """
        must:
            each closing paren matches the prev
            each closing paren must follow an open prev
            after all handled, stack is empty
        """

        close_open = {
            "]": "[",
            ")": "(",
            "}": "{"
        }
        opens = set(close_open.values())

        stack = []
        for paren in s:
            # found an open paren, push it
            if paren in opens:
                stack.append(paren)
                continue

            # found a closing paren, check it then pop
            if paren not in close_open:
                return False
            
            if len(stack) < 1:
                return False

            expected_open = close_open[paren]
            if expected_open != stack[-1]:
                return False

            stack.pop()
        
        return len(stack) == 0