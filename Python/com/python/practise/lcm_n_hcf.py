def lcm(num1, num2):
    if num1>num2:
        greater=num1
    else:
        greater=num2

    while (True):
        if((greater % num1 == 0)and(greater % num2 == 0)):
            lcm=greater
            break

        greater+=1
    return lcm

def hcf(num1, num2):
    if num1>num2:
        smaller=num1
    else:
        smaller=num2

    for i in range(1,smaller+1):
        if((num1 % i == 0)and(num2 % i == 0)):
            hcf = i

    return hcf