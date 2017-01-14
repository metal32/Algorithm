##Encrypting or Decrypting password
print "The program will encrypt or decrypt user password\n"
password_out=""
case_changer=ord("a")-ord("A")
encryption_key=(('a','m'),('b','h'),('c','t'),('d','f'),('e','g'),('f','k'),('g','b'),('h','p'),('i','j'),('j','w'),('k','e'),('l','r'),('m','q'),('n','s'),
            ('o','l'),('p','n'),('q','i'),('r','u'),('s','o'),('t','x'),('u','z'),('v','y'),('w','v'),('x','d'),('y','c'),('z','a'))
which=raw_input("Enter e for encryption and d for decryption: ")
valid=False
while not valid:
    if which=="e" or which=="d":
        valid=True
    else: 
        which=raw_input("Enter e for encryption and d for decryption: ")

if which=="e":
    encrypting=True
else:
    encrypting=False

password_in=raw_input("Enter Password: ")

if encrypting:
    from_index=0
    to_index=1
else:
    to_index=0
    from_index=1
for ch in password_in:
    letter_Found=False
    for t in encryption_key:
        if ('a'<=ch and ch<='z') and ch==t[from_index]:
            password_out=password_out+t[to_index]
            letter_Found=True
        elif ('A'<=ch and ch<='Z') and chr(ord(ch)+case_changer)==t[from_index]:
            password_out=password_out+chr(ord(t[to_index])-case_changer)
            letter_Found=True
    if not letter_Found:
        password_out=password_out+ch
if encrypting:
    print "Your encrypted password is {}".format(password_out)
else:
    print "Your decrypted password is {}".format(password_out)
