def prime_number_info(min,max):
    prime_numbers=[]
    for x in range(min,max+1):
        prime=True
        if x==1:
            prime=False
        elif x==2:
            prime=True
        else:
            for n in range(2,x):
                if x%n==0:
                    prime=False
        if prime:
            prime_numbers.append(x)
    return prime_numbers

