print'Hello buddy'
print'Let\'s get started'
spy_name=raw_input('What is your spy name? ')#take name as input from user
if len(spy_name)>2:#check that the length of name is greater than 2
    print'Welcome '+ spy_name +'.Glad to have you back with us.'#concatenating welcome with spy name
    spy_salutation=raw_input('What should we call you Mr. or Ms.')#input salutation
    if spy_salutation=='Mr.'or spy_salutation=='Ms.':
        spy_name=spy_salutation +' '+ spy_name
        print 'Alright '+spy_name+ '. I would like to know a little bit more about you'
        spy_age=input('What is your age? ')#input age
        if 12<spy_age<50:#fixing age of user to be between 12 to 50
            print'Your age is correct..'
            spy_rating=input('What is your rating? ')
            if spy_rating>5.0:
                print'Great spy..'
            elif 3.5<spy_rating<=5.0:
                print'Average spy..'
            elif 2.5<spy_rating<=3.5:
                print'Bad spy..'
            else:
                print'Who hired you..?'
            spy_is_online=True

        #concatenating string and integer/float value using str

        print 'Authentication complete.Welcome '+ spy_name +' age :'+str(spy_age) +'rating: '+str(spy_rating)
    else:
        print'Enter a valid salutation..'

else:
    print'Ooops Enter a vlid name'





