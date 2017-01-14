## Calendar Month Program
terminate=False
days_in_month=(31,28,31,30,31,30,31,31,30,31,30,31)
month_names=('January','Feburary','March','April','May','June','July','August','September','October','November','December')
day_name=("Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday")
calendar_year=[]
month_seperator=format(' ','8')
blank_week=format(' ','21')
blank_col=format(' ','3')

print format("Program will display a calendar month between 1800 and 2099\n")
while not terminate:
    year=int(input("Enter year (yyyy) format between 1800 and 2099\n Enter -1 for terminating the program\n"))
    if year==-1:
            terminate=True
    else:
        while year < 1800 or year > 2099:
            print "Invalid input, enter year in between 1800-2099"
            month=int(input())
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
        if not leap_year:
            value=value+1
 # First day of month for jan 1
        first_day_month=(value+1)%7
        print "\n",year
        print "The year {} is starting on {}".format(year,day_name[first_day_month])
# Printing calendar for each month of that particular year
        for month_num in range(12):
            month_name=month_names[month_num]
            print month_name,"\n"
            current_day=1
            if first_day_month==0:
                starting_col=7
            else:
                starting_col=first_day_month
            current_col=1
            calendar_week=' '
            calendar_month=[]
            while current_col<starting_col:
                print blank_col,
                current_col+=1
        
            if month_name=="Feburary" and leap_year:
                num_of_days_month=29
            else:
                num_of_days_month=days_in_month[month_num]

            while current_day<=num_of_days_month:
                if current_day<10:
                    print format(" ","2")+str(current_day),
                else:
                    print format(" ","1")+str(current_day),
                if current_col<7:
                    current_col+=1
                else:
                    calendar_month=calendar_month+[" "]
                    current_col=1
                    print ("") #Increaseing the gap between two rows
                current_day+=1
            calendar_month=calendar_month+[blank_week[0:(7-current_col)*3]]
            
            first_day_month=current_col
            calendar_year=calendar_year+calendar_month
            calendar_month=[]
            print "\n" #Increasing the gap between two months
        print "Calendar Year {}".format(year)
        
        calendar_year=[]



        
    

