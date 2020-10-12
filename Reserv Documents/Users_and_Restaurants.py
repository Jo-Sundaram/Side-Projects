class User:
    # initialize constructor with attributes
    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.__city = city
        self.__recent_restaruants = [] # list of recently booked restaurants by the user, stores restaurant objects
        self.__booked_restaurants = [] # list of restaurants currently booked by the user, stores restaruant objects

    def str(self):
        string = 'User: '+self.get_name() + '\nAge: '+str(self.get_age()) + '\nCity: ' + self.get_city()
        return string

    # getters and setters (or updaters) for class attributes
    def get_name(self):
        return self.__name
    
    def update_name(self,newName):
        self.__name = newName
        return self.__name
      
    def get_age(self):
        return self.__age

    def update_age(self, newAge):
        self.__age = newAge
        return self.__age

    def get_city(self):
        return self.__city

    def update_city(self, newCity):
        self.__city = newCity
        return self.__city


    def get_recent_restaurants(self):
        return self.__recent_restaruants


    def add_recent_restaurant(self,restaurant):
        # add a recently visited restaurant to user's list
        #inserts to beginning of list, returns restaurant object
        self.__recent_restaruants.insert(0,restaurant)
        return restaurant

    def book_restaurant(self,restaurant, table_type, table_size):
        # add booked restaurant to list
        # will add user to restaurants booked users
        self.__booked_restaurants.append(restaurant)
        self.add_recent_restaurant(restaurant)
        restaurant.add_booked_user(self,table_type,table_size)

    
        

    




class Restaurant:
    def __init__(self, name, cuisine, address, zip_code):
        self.__name = name
        self.__cuisine = cuisine
        self.__address = address
        self.__zip_code = zip_code
        self.__recent_users = [] # list of users who visited this restaurant, stores user objects
        self.__booked_users = [] # list of users currently booked at this restaurant
        self.__available_tables = [] # list of currently available tables, table sizes at restaurant
        self.__booked_tables = [] # list of currently booked tables at restaurant


    def str(self):
        string = "Restaurant Name: " + self.__name + "\nCuisine: " + self.__cuisine + "\nAddress: " + self.__address
        return string

        
   # getters for restaurant attributes
    def get_name(self):
        return self.__name
    
    def get_cuisine(self):
        return self.__cuisine

    def get_address(self):
        return self.__address
    
    def get_zip_code(self):
        return self.__zip_code

    def get_recent_users(self):
        return self.__recent_users
    
    def add_recent_user(self, user):
        # add recent user to the recent_users list
        pass


    def get_booked_users(self):
        return self.__booked_users
    
    def add_booked_user(self, user, table_type,table_size):
        # add recent user who reserves a table to the booked_users list, along with their requested table type/size
        # appends at end of list, returns user object
        # book the requested table
        self.__booked_users.append(user)
        self.book_table(table_type,table_size)
        return user

    def remove_booked_user(self, user, table_type, table_size):
        # remove a user from the booked list when their reservation is over
        # remove their table from booked tables list
        # returns user
        user_index = self.__booked_users.index(user)
        removed_user = self.__booked_users.pop(user_index)
        self.remove_booked_table(table_type,table_size)
        return removed_user

    def add_available_table(self, table):
        # add tables to restaurant, can take a list of table objects or single table objects
        if type(table) == list:
            self.__available_tables += table
        else:
            self.__available_tables.append(table)
    
    def get_available_tables(self):
        return self.__available_tables

    def get_booked_tables(self):
        return self.__booked_tables

    def book_table(self, table_type,table_size):
        # reserve table by type and size
        # table will be removed from available tables and be added to booked tables
        for table in self.__available_tables:
            if table.get_type() == table_type and table.get_size() == table_size:
                self.__booked_tables.append(table)
                table_index =  self.__available_tables.index(table)
                self.__available_tables.pop(table_index)
                break
    
    def remove_booked_table(self,table_type,table_size):
        # remove booked table from list 
        # table will be re-added to available tables list
        for table in self.__booked_tables:
            if table.get_type() == table_type and table.get_size() == table_size:
                self.__available_tables.append(table)
                table_index =  self.__booked_tables.index(table)
                self.__booked_tables.pop(table_index)
                break  
    

        



class Table:
    # Different restaurants will have different seating arrangements, that includes the type of tables (booth, regular, patio/outdoor) 
    # and size (2 seater, 4 seater, etc) inputted as numbers 
    def __init__(self,type,size):
        self.__type = type
        self.__size = size
    
    def str(self):
        string = "Type: " + self.__type + "\nSize: " + str(self.__size)
        return string

    def get_type(self):
        return self.__type

    def get_size(self):
        return self.__size





def main():
    bob = User("Bob", 19, "Ottawa")
    restaurant = Restaurant("Bob's Burgers","Burger Joint","123 Burger Street", "A1A 2B2")

    tables = [Table("booth", 4), Table("regular",4), Table("patio",2), Table("patio",4)]

    restaurant.add_available_table(tables)

    print("\n--All tables--\n")

    for t in restaurant.get_available_tables():
        print(t.str())
    


    bob.book_restaurant(restaurant,"booth",4)
    
    print("\n--Booked Users--\n")
    for user in restaurant.get_booked_users():
        print(user.get_name())

    print("\n--Bob Booked--\n")
    for t in restaurant.get_booked_tables():
        print(t.str())

    print("\n--Available tables--\n")
    for t in restaurant.get_available_tables():
        print(t.str())

    restaurant.remove_booked_user(bob,"booth",4)
    
    print("\n--After Bob leaves--\n")
    print("\n--Available tables--\n")
    for t in restaurant.get_available_tables():
        print(t.str())

    print("\n--Booked tables--\n")
    for t in restaurant.get_booked_tables():
        print(t.str())

    print("\n--Booked Users--\n")
    for user in restaurant.get_booked_users():
        print(user.get_name())

    print("\n--Bob's recent restaurants--\n")
    for r in bob.get_recent_restaurants():
        print(r.str())


main()







    

