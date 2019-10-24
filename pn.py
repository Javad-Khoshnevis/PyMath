print ("\033c")
while 1 == 1 :
    num = input("Enter Your Number :")
    if (num > 1) :
        m = 2
        while 1 < m < num :
            b = divmod(num, m)
            a = b[1]
            if (a != 0) :
                m = m + 1
            else :
                print num, "by", m, "is divisible!"
                break
        else:
            print("this is a prime number!")
        y = 1
        n = 2
        done = input("Do you have another question? (y/n)")
        if (done is 2) :
            execfile('main.py')
        else :
            continue;

    elif (num == 1) :
        print("this is an spacial number !")
        continue;
    else :
        print("Primes are only considered in the range of natural numbers!\nTry again!")
        continue;