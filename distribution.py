def distributingMoney(x, y, z, k): 
    if (x + y + z + k) % 3 == 0:       
        target = (x + y + z + k) // 3  
        if target >= max(x, y, z):     
            return 1
        else:
            return 0
    else:
        return 0

x, y, z, k = map(int, input().split())
print(int(distributingMoney(x, y, z, k)))
