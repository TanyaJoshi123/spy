from spy_details import spy #importing spy dictionary from spy_details file
print'Hello buddy'#print hello buddy
print'Let\'s get started'
STATUS_MESSAGE=['Sleeping', 'Busy', 'Do not disturb']#list
friends=[{'name': 'Shweta','age': 22,'rating': 2.5,'is_online':True},{'name': 'Nidhi','age':22,'rating':3.5,'is_online':True}]#dictionary within a list
def add_status(c_status):
    if c_status != None:
        print "Your current status is "+ c_status
    else:
        print"You don't have any status currently.."
    existing_status = raw_input("You want to select from old status? Y/N")
    if existing_status.upper() == 'N':
        new_status=raw_input('Enter your status : ')
        if len(new_status) > 0:
            STATUS_MESSAGE.append(new_status)#adding new status to list..
    elif existing_status.upper()=='Y':
        serial_no=1
        for old_status in STATUS_MESSAGE:#traversing the list
            print str(serial_no)+old_status
            serial_no=serial_no+1
        user_choice=input('Enter your choice :')
        new_status=STATUS_MESSAGE[user_choice-1]
    updated_status=new_status
    return updated_status
def add_friend():
    frnd= {'name':'',
           'age':0,
           'rating':0.0,
           'is_online':True}
    frnd['name']=raw_input('What is your name ?')
    frnd['age']=input('What is your age ?')
    frnd['rating']=input('What is your rating ?')
    frnd['is_online']=True
    if len(frnd['name'])>2 and 12<frnd['age']<50 and frnd['rating']>spy['rating'] :
       friends.append(frnd)
    else:
        print 'Friend cannot be added..'
    return len(friends)
def select_frnd():
    serial_no=1
    for frnd in friends:# traversing the dictionary friends to show the friends.
        print str(serial_no)+'.'+frnd['name']
        serial_no=serial_no+1
    user_selected_frnd=input('Enter your choice : ')
    user_selected_frnd_index=user_selected_frnd-1
def send_message():
    selected_frnd=select_frnd()
def read_message():
    selected_frnd=select_frnd()
def spy_chat(spy_name,spy_age,spy_rating): #defining the function
    print'Here are your options..'+spy_name
    current_status=None
    show_menu=True
    while show_menu:
        spy_choice=input('What do you want to do \n 1. Add a status. \n 2. Add a friend \n 3. Send a message \n 4. Read a message \n 0. exit')
        if spy_choice==1:
            current_status= add_status(current_status)
            print 'Updated status is '+ current_status
        elif spy_choice==2:#elif for multiple conditions.
            no_of_friends=add_friend()
            print 'You have '+ str(no_of_friends) +' friends.'
        elif spy_choice==3:
            send_message()
        elif spy_choice==4:
            read_message()
        elif spy_choice==0:
            show_menu=False
        else:
            print'Invalid options..'
spy_exist=raw_input('Are you a new user : Y/N')#asking whether you are new or not
if spy_exist.upper()=='N':#when spy is an old one
    print'Welcome back '+spy['name']+' age :'+str(spy['age'])+' having rating of '+str(spy['rating'])
    spy_chat(spy['name'],spy['age'],spy['rating'])#calling function
elif spy_exist.upper=='Y':
    spy={                      #dictionary..
        'name':'',
        'age': 0,
        'rating':0.0
    }
    spy['name']=raw_input('What is your spy_name?  ')#take input from user
    print spy['name']
    if len(spy['name'])>2:#checking the length of input
        print'Welcome '+spy['name'] +'.'#concatenating name with welcome.
        spy_salutation=raw_input('What should we call you Mr. or Ms. ')#input salutation from user
        if spy_salutation=='Mr.' or spy_salutation=='Ms.':
             spy['name']=spy_salutation+' '+spy['name']#concatenation
             print'Welcome '+spy['name'] +'. Glad to see you back..'
             print'Alright  '+spy['name']+'. I would like to know a little bit more about you..'
             spy['age']=input('What is your age..?')#input from user
             if 12<spy['age']<50:#spy age should be between 12 to 50
                 print'Your age is correct....'
                 spy['rating']=input('What is your rating..?')#input rating of spy
                 if spy['rating']>5.0:
                     print'Great spy..'
                 elif 3.5<spy['rating']<=5.0:
                     print'Average spy.'
                 elif 2.5<spy['rating']<=3.5:
                     print'Bad spy..'
                 else:
                     print'Who hired you...'
                 spy_is_online=True#check if spy is online
                 #str to concat string with integer/float..
                 print'Authentication is completed..Welcome '+ spy['name'] +'age: '+str(spy['age'])+ 'rating: '+str(spy['rating'])
                 spy_chat(spy['name'],spy['age'],spy['rating'])#calling function spy_chat
             else:
                 print'You are not eligible to be a spy....'
        else:
             print'Invalid salutation...'
    else:
        print 'Oops please enter a valid name..'
else:
    print'Invalid entry...'



