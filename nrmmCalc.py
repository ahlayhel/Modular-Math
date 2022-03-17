import math
from tkinter import *


# Create a GUI window
window = Tk()

#########################
# Compute Modular Inverse
#########################
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x

####################
# Compute WW-MM
####################
def mm(a,b,p,k,r):

    k1 = modInverse(p,r)
    k0 = (-k1) % r

    T = a * b
    for i in range(k):
        T1 = T % r
        Y = (T1 * k0) % r
        T2 = Y * p
        T3 = T + T2
        T = T3 // r
    else:
        return T


################################
# Compute Modular Multiplication
################################
def modularMult():

    a = int(e2_value.get())
    b = int(e4_value.get())
    p = int(e6_value.get())
    s = int(e12_value.get())

    k = math.ceil(s/64)
    n = 64 * k
    h = (2**(2*n)) % p
    r = 2**64

    a1 = mm(a,h,p,k,r)
    b1 = mm(b,h,p,k,r)
    u1 = mm(a1,b1,p,k,r)
    u = mm(u1,1,p,k,r)
    x = hex(u)

    # Enters results to
	# the text widget
    t2.delete("1.0", END)
    t2.insert(END,(len(hex(a))-2)*4)
    t3.delete("1.0", END)
    t3.insert(END,(len(hex(b))-2)*4)
    t4.delete("1.0", END)
    t4.insert(END,(len(hex(p))-2)*4)
    t5.delete("1.0", END)
    t5.insert(END,k)
    t1.delete("1.0", END)
    t1.insert(END,x)

# Create the Label widgets
e1 = Label(window, text = "Enter Gx")
e2_value = StringVar()
e2 = Entry(window, width = 160, textvariable = e2_value)
e3 = Label(window, text = "Enter Gy")
e4_value = StringVar()
e4 = Entry(window, width = 160, textvariable = e4_value)
e5 = Label(window, text = "Enter p")
e6_value = StringVar()
e6 = Entry(window, width = 160, textvariable = e6_value)
e7 = Label(window, text = 'Gx x Gy mod p')
e8 = Label(window, text = "Number of bits in coordinate Gx")
e9 = Label(window, text = "Number of bits in coordinate Gy")
e10 = Label(window, text = "Number of bits in prime modulus p")
e11 = Label(window, text = "Enter NRMM.s")
e12_value = StringVar()
e12 = Entry(window, width = 20, textvariable = e12_value)
e13 = Label(window, text = 'Number of iterations k')

# Create the Text Widgets
t1 = Text(window, height = 1, width = 140)
t2 = Text(window, height = 1, width = 5)
t3 = Text(window, height = 1, width = 5)
t4 = Text(window, height = 1, width = 5)
t5 = Text(window, height = 1, width = 5)

# Create the Button Widget
b1 = Button(window, text = "Compute Modular Multiplication on ECC Coordinates", command = modularMult)

# grid method is used for placing
# the widgets at respective positions
# in table like structure
e1.grid(row = 0, column = 0)
e2.grid(row = 0, column = 1)
e8.grid(row = 0, column = 2)
t2.grid(row = 0, column = 3)
e3.grid(row = 1, column = 0)
e4.grid(row = 1, column = 1)
e9.grid(row = 1, column = 2)
t3.grid(row = 1, column = 3)
e5.grid(row = 2, column = 0)
e6.grid(row = 2, column = 1)
e10.grid(row = 2, column = 2)
t4.grid(row = 2, column = 3)
e11.grid(row = 3, column = 0)
e12.grid(row = 3, column = 1)
b1.grid(row = 4, column = 1)
e13.grid(row = 3, column = 2)
t5.grid(row = 3, column = 3)
e7.grid(row = 5, column = 0)
t1.grid(row = 5, column = 1)

# Start the GUI
window.mainloop()
