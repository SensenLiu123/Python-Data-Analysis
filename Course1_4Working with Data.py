#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:24:07 2018

@author: Sensen
"""

"""
Project: Working with Dates
The project consists of multiple problems. Each problem will utilize functions
 you wrote for the previous problems, so we strongly suggest that implement and
 test these functions in the given order. We have provided the following 
 template that you can use to get you started. It includes the signatures 
 (name, parameters, and docstrings) for all of the functions that you will 
 need to write. The code however, simply returns some arbitrary value no matter
 what the inputs are, so you will need to modify the body of the function to 
 work correctly. You should not change the signature of any of the functions in
 the template, but you may add any code that you need to.

"""

"""
Problem 1: Computing the number of days in a month
First, you will write a function called days_in_month that takes two integers:
    a year and a month. The function should return the number of days in that 
    month. You may assume that both inputs are valid (in other words, you do 
    not need to write any code to check whether or not they are reasonable, you
    can just assume that the month input is a number between 1 and 12 and the 
    year input is a number between datetime.MINYEAR and datetime.MAXYEAR).


"""
import datetime


def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month.
    """
    if year <= datetime.MAXYEAR and year >= datetime.MINYEAR:
        date1 = datetime.date(year,month,1)
        # date of the next month!
        # consider case Dec!
        date2 = datetime.date(year+(month)//12,(month)%12+1,1)
        diff = date2 - date1
        return diff.days
    return    
    
# tester:    
#print(days_in_month(1973, 11))  
        
"""    
Problem 2: Checking if a date is valid
Next, you will write a function called is_valid_date that takes three integers:
    a year, a month, and a day. The function should return True if that date is
    valid and False otherwise. This function should not assume that the inputs 
    are valid. Rather, this function should check that all three inputs combine
    to form a valid date, with a year between datetime.MINYEAR and 
    datetime.MAXYEAR, a month between 1 and 12, and a day between 1 and the 
    number of days in the given month. Notice that the function 
    days_in_month that you wrote for Part 1 will be useful here!

"""



def is_valid_date(year,month,day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if isinstance(year,int) and year <= datetime.MAXYEAR and year >= datetime.MINYEAR:
        if isinstance(month,int) and month <=12 and month >=1:
            if day <= days_in_month(year,month) and day >= 1:
                return True
# default is False            
    return False
        


#print(is_valid_date(1998,19,42))    



"""
Problem 3: Computing the number of days between two dates
Now that we have a way to check if a given date is valid, you will write a 
function called days_between that takes six integers 
(year1, month1, day1, year2, month2, day2) and returns the number of days from 
an earlier date (year1-month1-day1) to a later date (year2-month2-day2). 
If either date is invalid, the function should return 0. 
Notice that you already wrote a function to determine if a date is valid or not! 
If the second date is earlier than the first date, the function should also return 0.
"""

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """

    if is_valid_date(year1,month1,day1) and is_valid_date(year2,month2,day2):
        date1 = datetime.date(year1,month1,day1)
        date2 = datetime.date(year2,month2,day2)
        difference = date2 - date1
        return max (difference.days,0)
    
    return 0

#print(days_between(2001,2,23,1998,2,12))


"""
Problem 4: Calculating a person's age in days
Finally, you will write a function called age_in_days that takes three integers
 as input: the year, month, and day of a persons birthday. The function should 
 return that person's age in days as of today. The function should return 0 if 
 the input date is invalid (remember you have a function to check that!). 
 The function should also return 0 if the input date is in the future.

Remember that you already have a function that returns the number of days 
between two dates that you wrote in Part 3. Which two dates could you pass to 
that function to solve this problem?
"""



def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    
    today = datetime.date.today()
    age = days_between(year, month, day, today.year, today.month, today.day)
    return age


print(age_in_days(2017,1,1))

    
        