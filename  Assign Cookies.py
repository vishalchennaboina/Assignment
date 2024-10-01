def findContentChildren(g, s):
    g.sort()
    s.sort()
    child_i = 0
    cookie_j = 0
    
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            child_i += 1
        cookie_j += 1
    
    return child_i

#Example-1
g1 = [1, 2, 3]
s1 = [1, 1]
print(findContentChildren(g1, s1))  

# Example-2
g2 = [1, 2]
s2 = [1, 2, 3]
print(findContentChildren(g2, s2))