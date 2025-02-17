class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        words = path.split('/')
        for word in words:
            if word == '' or word == '.':
                continue
            elif word == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(word)

        return '/' + '/'.join(stack)
