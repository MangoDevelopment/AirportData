'''
Created on Jan 17, 2018

@author: Bodie Brewer
@copyright 2017 Mango Development
'''
# error program
def error():
    print('There was an error.')
# age checking system
def ageChecker():
    age = input('Please enter your age.')
    if age < 18:
        error()
        if age > 102: 
            error()
# boarding pass info
def boardPass():
    passnum = input('Please enter your 8 digit boarding pass. If you would like to buy a ticket, please type in eight zeros.')
    if passnum == 00000000:
        location = input('Please type in the destination location.')
        print('We have tickets to ' + location + ' for a rate of $600 round trip.')
        amttic = input('How many tickets do you want?')
        price = amttic * 600
        print('The price is '+ price + '.')
        print('Your boarding pass is: '+ 15759514)
        passnum = input('Please enter your 8 digit boarding pass.')
        if len(passnum) ==  8:
            print('Thank you. Please see the on-site ticket help for gate number.')
        else:
            error()
