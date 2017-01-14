#Calculate age of a person
import datetime
Year, Month, Day=map(int,raw_input("Enter your DOB in the format of YEAR MONTH DATE \n").split())

current_year=datetime.date.today().year
current_month=datetime.date.today().month
current_day=datetime.date.today().day

numsec_day=24*60*60
numsec_year=(365*60*60*24)

avg_numsec_year=(4*numsec_year+numsec_day)/4

avg_numsec_month=avg_numsec_year/12

numsec_1900=(Year-1900)*avg_numsec_year+(Month-1)*avg_numsec_month+(Day*numsec_day)
numsec_current=(current_year-1900)*avg_numsec_year+(current_month-1)*avg_numsec_month+(current_day*numsec_day)

Age_sec=numsec_current-numsec_1900
Age_year=Age_sec/avg_numsec_year
print "You are ", Age_year," years old."
