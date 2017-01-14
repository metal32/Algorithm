## Calendar Month Program
terminate=False
days_in_month=(31,28,31,30,31,30,31,31,30,31,30,31)
month_names=('January','Feburary','March','April','May','June','July','August','September','October','November','December')
day_name=("Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday")


print format("Program will display a calendar month between 1800 and 2099\n")
while not terminate:
    month=int(input("Enter month (1-12) format, Enter -1 for terminating\n"))
    if month==-1:
            terminate=True
    else:
        while month>12 or month<1: 
            print "Invalid input, enter month in between 1-12"
            month=int(input("Enter month (1-12) format\n"))
        year=int(input("Enter year (yyyy) format\n"))
        while year < 1800 or year > 2099:
            print "Invalid input, enter year in between 1800-2099"
            year = int(input("Enter year (yyyy) format\n"))
        if year%4==0 and (not(year%100==0) or (year%400==0)):
            leap_year=True
        else: leap_year=False
    ## Finding the day of the week    
        century_digits=year//100 
        year_digits= year%100
        value=year_digits+(year_digits//4)
        if century_digits==18:
            value=value+2
        elif century_digits==20:
            value=value+6
        if month==1 and not leap_year:
            value=value+1
        elif month==2:
            if leap_year:
                value=value+3
            else:
                value=value+4
        elif month==3 or month==11:
            value=value+4
        elif month==5:
            value=value+2
        elif month==6:
            value=value+5
        elif month==8:
            value=value+3
        elif month==9 or month==12:
            value=value+6
        elif month==10:
            value=value+1
        days_of_week=(value+1)%7
        print "The month is starting on {}".format(day_name[days_of_week])
# First day of month for jan 1
        print "\n"+month_names[month-1], year
        if days_of_week==0:
            starting_col=7
        else:
            starting_col=days_of_week
        current_col=1
        column_width=3
        blank_char=" "
        blank_column=format(blank_char,str(column_width))
        while current_col<starting_col:
            print blank_column,
            current_col+=1
        current_day=1
        if month==2 and leap_year:
            num_of_days_month=29
        else:
            num_of_days_month=days_in_month[month-1]
        while current_day<=num_of_days_month:
            if current_day<10:
                print format(blank_char,"2")+str(current_day),
            else:
                print format(blank_char,"1")+str(current_day),
            if current_col<7:
                current_col+=1
            else:
                current_col=1
                print ("")
            current_day+=1
        print("\n")



        
    

