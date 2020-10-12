class User:

    # initialize constructor with attributes
    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.__city = city
        self.__friends = []

    def str(self):
        string = 'User: '+self.getName() + '\nAge: '+str(self.getAge()) + '\nCity: ' + self.getCity()
        return string

    # getters and setters (or updaters) for class attributes
    def getName(self):
        return self.__name
    
    def updateName(self,newName):
        self.__name = newName
        return self.__name
      
    def getAge(self):
        return self.__age

    def updateAge(self, newAge):
        self.__age = newAge
        return self.__age

    def getCity(self):
        return self.__city

    def updateCity(self, newCity):
        self.__city = newCity
        return self.__city

    # get user's friends list (returns list)
    def getFriendsList(self):
        return self.__friends 

    # print user's friends list
    def printFriendsList(self):
        print("Here are "+ self.__name+"'s friends:")
        for friend in self.__friends:
            print(friend.getName())

        print()

    # add another user to friends list, takes user object
    # this will add the current user to the other user's friend list as well
    def addFriend(self, user):
        # return 0 if adding friend is successful else return 1
        if user not in self.__friends:
            self.__friends.append(user)
            user.__friends.append(self)
            return 0
        else:
            return 1

    # remove user from friends list, takes user object
    # this will remove the current user from the other user's friend list as well
    def removeFriend(self, user):
         # return 0 if removing friend is successful else return 1
        if user in self.__friends:
            self.__friends.pop(self.__friends.index(user))
            user.__friends.pop(user.__friends.index(self))
            return 0
        else:
            return 1


# function to create a new user by entering attribute information, returns a user object
def createNewUser():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    city = input('Enter your city: ')
    print('User created!')

    return User(name,age,city)

# print all user objects 
def displayUsers(users_list):
    print('Enter user number to view their details, enter -1 to go back:\n ')
    for i in range(len(users_list)):
        print(i,end = ". ")
        print(users_list[i].getName() +'\n')

    select = int(input())
    if select ==-1:
        return
    else:
        # print('Name: ' + users_list[select].getName() + '\nAge: ' + str(users_list[select].getAge())+'\nCity: ' + users_list[select].getCity())
        print(users_list[select].str())
        users_list[select].printFriendsList()

# add a friend by name
def addFriend(current_user, users_list):
    name = input('Enter the name of the user you wish to friend: ')
    try:
        for user in users_list:
            if user.getName() ==name:
                other_user = user
                break

        success = current_user.addFriend(other_user)

        message = user.getName() + " is now your friend!\n" if success ==0 else user.getName() + " is already your friend! \n"
        print(message)
    except UnboundLocalError:
        print('User does not exist! \n')        
        return    

# remove friend by name
def removeFriend(current_user,users_list):
    name = input('Enter the user you wish to remove from your friends list: ')
    try:
        for user in users_list:
            if user.getName() ==name:
                other_user = user
                break
    except:
        print('User does not exist!')            

    success = current_user.removeFriend(other_user)
    message = user.getName() + " is removed :(\n" if success ==0 else user.getName() + " is not in your friends list!\n"
    print(message)

# edit/update user information (attributes)
def editUser(user):
    print(user.str())
    print('What would you like to edit? \n1. Edit name\n2. Edit age\n3. Edit city\n')
    action = int(input('Enter number, enter -1 to finish editing your user: '))

    while action != -1:
        if action ==1:
            newName = input('Enter a new name: ')
            user.updateName(newName)
        elif action ==2:
            newAge = int(input('Enter a new age: '))
            user.updateAge(newAge)
        elif action ==3:
            newCity = input('Enter a new city: ')
            user.updateCity(newCity)

        print('What would you like to edit? \n1. Edit name\n2. Edit age\n3. Edit city\n')
        action = int(input('Enter number, enter -1 to finish editing your user: '))




# makes a set of 4 premade users with attributes and friends-list set up
# Returns list of users
def premadeUsers():
    All_Users = [] # array to store all users

    # pre-made users
    bob = User('bobby',19,'ottawa')
    jim = User('jim',17,'montreal')
    sharon = User('sharon',26,'toronto')
    anna = User('anna', 21, 'ottawa')

    bob.addFriend(anna)
    bob.addFriend(jim)

    jim.addFriend(anna)
    sharon.addFriend(anna)

    All_Users.append(bob)
    All_Users.append(jim)
    All_Users.append(sharon)
    All_Users.append(anna)

    return All_Users

def main():
    All_Users = premadeUsers() # initialize premade users
        
    # 'login' message
    # a 'returning user' can enter the name of a premade user (bobby, jim, sharon, anna)
    login_successful = -1
    print('\t\tW E L C O M E\n ')
    while login_successful ==-1:
        select = int(input('Are you a new user or a returning user?\n1. New User\n2. Returning User\n'))
        try: 
            if select ==1:
                All_Users.append(createNewUser())
                current_user = All_Users[-1]
            else:
                name = input('Enter user name: ')

            
                for user in All_Users:
                    if user.getName() == name:
                        current_user = user
                        break

            print('Welcome, ' + current_user.getName()+'\n')
            login_successful = 0

        except UnboundLocalError:
                print('User does not exist! Please Try Again \n: ')

    

    # your user can perform some actions
    print('What would you like to do? \n1. Display all users\n2. Add Friend\n3. Remove Friend\n4. Edit your user\n')
    print('Enter action number, enter -1 to exit: ')
    action = int(input())

    while action != -1:

        while action <1 or action >4:
            print('Please select a valid action: ')
            action = int(input())

        if action ==1:
            displayUsers(All_Users)
        elif action ==2:
            addFriend(current_user,All_Users)
        elif action ==3:
            removeFriend(current_user,All_Users)
        elif action ==4:
            editUser(current_user)
    
        print('What would you like to do? \n1. Display all users\n2. Add Friend\n3. Remove Friend\n4. Edit your user\n')
        print('Enter action number, enter -1 to exit: ')
        action = int(input())
    
   
    print('Logging off ... \nGoodbye :)')

 




main()



