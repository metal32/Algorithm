## Let's make a simple game
import datetime
import random
terminate=False
string=[" ","1","5","10","25"]
print "Today's date is", datetime.date.today()
print "Enter the coin values as 1, 5, 10, 25 "
print "Enter space and enter to stop putting the coins "
while not terminate:
    amount=random.randint(1,99)
    print "Enter coins that add up to ",amount,"one per line. \n"
    gameover=False
    total=0
    while not gameover:
        valid=False
        while not valid:
            if total==0:
                entry=raw_input("Enter your first coin\n")
            else:
                entry=raw_input("Enter your next coin\n")
            if entry in string:
                valid=True
            else:
                print "Enter a valid coin domination"
        if entry==string[0]:
            if total==amount:
                print "Correct! You won the game"
            else:
                print "You only entered ", total,"cents. "
            gameover=True
        else:
            total=total+int(entry)
            if total>amount:
                print "You have exceeded the {}".format(amount)
        if gameover:
            invalid=True
            while invalid:
                decision=raw_input("For playing again (Y/N) ") 
                if decision not in ("Y","N"):
                    print "Enter Y or N only "
                else:
                    invalid=False 
            if decision=="N":
                terminate=True
print "Thanks for playing the game. "