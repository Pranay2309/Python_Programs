for  r in range(1,5):
    for c in range(1,r+1):
        if c%2!=0:
            print("1",end=' ')
        if c%2==0:
            print("0",end=' ')
    print()
