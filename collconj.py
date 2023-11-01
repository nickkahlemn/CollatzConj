def collatz(num, cache, largestloop):
    startnum = num
    count = 0 
    while(num > cache):
        if(num%2 == 1):
            num = 3*num+1
            count += 1
        else:
            num = num/2
            count += 1
    if (count > 400):
        if (count > largestloop):
            largestloop = count
        print (startnum, count, largestloop)
    cache = startnum
    return cache, largestloop

if __name__ == "__main__":
    num = int(input("input num > 4:"))
    cache = 4 # contains the largest num completed by function, if function does not break loop we have found solution
    largestloop = 0
    while(1):
        cache, largestloop = collatz(num, cache, largestloop)
        num += 1
