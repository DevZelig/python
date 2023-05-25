fname = input("What is your first name")
lname = input("What is your last name")
print(fname[0]+"."+lname+"@gmail.com is your email")

phonenumber = input("what is your phone number")

if phonenumber.isdigit() and len(phonenumber) == 10:
    print('thank you for the number')
else:
    print("invalid number")

sntc = input("Tell me a sentence")

l = sntc.split()
l.reverse()
sntc = ' '.join(l)
print(sntc) 