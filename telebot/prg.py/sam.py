
r = [10, 22, 5, 75, 65, 80]

p1, p2 = 0, 0
minpr1, minpr2 = float('inf'), float('inf')
    
for i in r:
    minpr1 = min(minpr1, i)
    
    p1 = max(p1, i - minpr1)
    
    minpr2 = min(minpr2, i - p1)
    
    p2 = max(p2, i - minpr2)
    
print(p2)