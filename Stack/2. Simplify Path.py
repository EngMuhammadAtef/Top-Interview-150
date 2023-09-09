class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        s = []
        for d in path:
            if d == '..':
                if s:
                    s.pop()
            elif d not in ('', '.'):
                s.append(d)
            
        return "/" + "/".join(s)