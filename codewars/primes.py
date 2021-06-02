def prime(n):
    counter = 0
    lis = []
    
    for num in range(2, n+1):
        for div in range(1, num+1):
            if num % div == 0:
                counter += 1
        if counter > 2:
                counter = 0
                continue
        else:
            lis.append(num)
            counter = 0
    return lis
