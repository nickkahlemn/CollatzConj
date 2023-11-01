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
    if (count > 400): # ignore loops less than 400 since it becomes
                      # too much in the console, can be changed to any value
        if (count > largestloop):
            largestloop = count
        print (startnum, count, largestloop)
    cache = startnum
    return cache, largestloop

if __name__ == "__main__":
    num = int(input("input a positive integer:"))
    cache = 1 # contains the largest num completed by function, 
              # if function does not break loop we have found solution
    
    largestloop = 0 # Does NOT equal total number of steps to 1, 
                    # only the first value will be the total number of steps 
                    # the rest will be steps to the cache value (num-1)
    print("num / count / longest loop to cache")
    while(1):
        cache, largestloop = collatz(num, cache, largestloop) # update global variables with computed results 
        num += 1