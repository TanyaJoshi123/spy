from spy_details import spy_name,spy_rating,spy_age#importing these variables from spy_details file
print'Hello buddy'#print hello buddy
print'Let\'s get started'
STATUS_MESSAGE=['Sleeping', 'Busy', 'Do not disturb']#list
def add_status(c_status):
    if c_status != None:
        print "Your current status is "+ c_status
    else:
        print"You don't have any status currently.."
    existing_status=raw_input("You want to select from old status? Y/N")
    if existing_status.upper()=='N':
        new_status=raw_input('Enter your status : ')
        if len(new_status)>0:
            STATUS_MESSAGE.append(new_status)#adding new status to list..
    elif existing_status.upper()=='Y':
        serial_no=1
        for old_status in STATUS_MESSAGE:
            print str(serial_no)+old_status
            serial_no=serial_no+1
        user_choice=input('Enter your choice :')
        new_status=STATUS_MESSAGE[user_choice-1]
        updated_status=new_status
        return updated_status





def spy_chat(spy_name,spy_age,spy_rating): #defining the function
    print'Here are your options..'+spy_name
    current_status=None
    show_menu=True
    while show_menu:
        spy_choice=input('What do you want to do \n 1. Add a status. \n 2. Add a friend \n 3. Send a message \n 4. Read a message \n 0. exit')
        if spy_choice==1:
            updated_status_message=add_status(current_status)
            print'Updated status is '+ updated_status_message
        elif spy_choice==2:#elif for multiple conditions.
            print'Add a friend..'
        elif spy_choice==0:
            show_menu=False
        else:
            print'Invalid options..'
spy_exist=raw_input('Are you a new user : Y/N')#asking whether you are new or not
if spy_exist.upper()=='N':#when spy is an old one
    print'Welcome back '+spy_name+' age :'+str(spy_age)+' having rating of '+str(spy_rating)
    spy_chat(spy_name,spy_age,spy_rating)#calling function
elif spy_exist.upper=='Y':
    spy_name=raw_input('What is your spy_name?  ')#take input from user
    print spy_name
    if len(spy_name)>2:#checking the length of input
        print'Welcome '+spy_name +'.'#concatenating name with welcome.
        spy_salutation=raw_input('What should we call you Mr. or Ms. ')#input salutation from user
        if spy_salutation=='Mr.' or spy_salutation=='Ms.':
             spy_name=spy_salutation+' '+spy_name#concatenation
             print'Welcome '+spy_name +'. Glad to see you back..'
             print'Alright  '+spy_name+'. I would like to know a little bit more about you..'
             spy_age=input('What is your age..?')#input from user
             if 12<spy_age<50:#spy age should be between 12 to 50
                 print'Your age is correct....'
                 spy_rating=input('What is your rating..?')#input rating of spy
                 if spy_rating>5.0:
                     print'Great spy..'
                 elif 3.5<spy_rating<=5.0:
                     print'Average spy.'
                 elif 2.5<spy_rating<=3.5:
                     print'Bad spy..'
                 else:
                     print'Who hired you...'
                 spy_is_online=True#check if spy is online
                 #str to concat string with integer/float..
                 print'Authentication is completed..Welcome '+ spy_name +'age: '+str(spy_age)+ 'rating: '+str(spy_rating)
                 spy_chat(spy_name,spy_age,spy_rating)#calling function spy_chat
             else:
                 print'You are not eligible to be a spy....'
        else:
             print'Invalid salutation...'
    else:
        print 'Oops please enter a valid name..'
else:
    print'Invalid entry...'



