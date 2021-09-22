for i in range (10000):
    if i>=0 and i<10:
        if i == i**1:
            print (i)
    if i>= 10 and i<100:
        a = i // 10
        b = i - (a*10)
        if i == (a**2 + b**2):
            print(i)
    if i>= 101 and i<1000:
        a = i // 100
        b = (i - (a*100)) // 10
        d = i - (a*100 + b*10)
        if i == (a**3 + b**3 + d**3):
            print(i)
    if i>= 1000 and i<=10000:
        a = i // 1000
        b = (i - a*1000) // 100
        c = (i - (a*1000 + b*100)) // 10
        d = i - (a*1000 + b*100 + c*10)
        if i == (a**4 + b**4 + c**4 + d**4):
            print(i)
