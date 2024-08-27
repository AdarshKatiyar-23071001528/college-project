n = complex((input("Enter complex number:")))
real = n.real
img = n.imag
if(real-img > 0):
    print("Real part is greatest")
elif(real-img == 0):
    print("Both are equal")
else:
    print("Imaginary part is greatest")