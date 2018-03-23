print'Hello Buddy!'
print'Let\'s get started'
spy_name=raw_input('What is your spy_name?  ')
if len(spy_name)>2:
    print'Welcome '+spy_name+' Glad to have you back with us..'
    spy_salutation=raw_input('What should we call you Mr. or Ms. ')
    if spy_salutation=='Mr.' or spy_salutation=='Ms.':
         spy_name=spy_salutation+' '+spy_name
         print'Alright  '+spy_name+'. I would like to know a little bit more about you..'
         spy_age=input('What is your age..?')
         if 12<spy_age<50:
             print'Your age is correct....'
             spy_rating=input('What is your rating..?')
             if spy_rating>5.0:
                 print'Great spy..'
             elif 3.5<spy_rating<=5.0:
                 print'Average spy..'
             elif 2.5<spy_rating<=3.5:
                 print'Bad spy..'
             else:
                 print'Who hired you...'
         else:
             print'You are not eligible to be a spy....'


    else:
         print'Invalid salutation...'
else:
    print 'Oops please enter a valid name..'

