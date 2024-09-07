q = int(input("Enter 1 for decimal to binary and enter 0 binary to decimal : "))
if q==1:
    n = int(input("Enter Any Positive integer Number : "))
    N_res = res = 0
    count = 0
    rem1=0
    if n>=0:
        while(n>0):
            rem = n%2
            rem1 = rem1+rem
            if rem1==0:
                count +=1
            n = n//2
            res = res*10+rem
        while res>0:
            ld = res%10
            res=res//10
            N_res = N_res*10+ld
        print (N_res*(10**count))

    else:
        print("Please Enter Positive Number")
elif q==0:
    n = int(input("Enter any number :  "))
    n1=n
    count1,count,sum =0,0,0
    if n>=0:
        while n!=0:
            ld1 = n%10
            if ld1==1 or ld1==0:
                n//=10
                ld =  n1%10
                sum += ld*(2**count)
                n1 //=10
                count+=1
                continue
            else:
                print("Binary number base 2 so number could not be greater than 1")
                count1+=1
                break
        if count1==0:
            print(sum)
    else:
        print("Accepted only positive number")
else:
    print("Enter valid input")