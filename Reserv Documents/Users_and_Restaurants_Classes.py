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

    # getters and setters (or updaters) for user  attributes
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
        # adds a recently visited restaurant to user's recent_restaurants list
        pass

    def book_restaurant(self,restaurant, table_type, table_size): # (See Table class below)
        # adds restaurant to user's booked_restaurants list 
        # this will also add the user to that restaurant's booked users list, 
        # as well as booking the specified table type and size for the user using the restaurant.add_booked_user() method
        pass

    
    def unbook_restaurant(self, restaruant, table_type,table_size):
        # remove restaurant from user's booked_restaurants list
        # this will aslo remove the user from that restaruant's booked users list
        # as well as removing their requested table from the restaurant's booked tables list
        # using the restaurant.remove_booked_user() method
        pass
        

    




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
        # adds user who reserved a table to the booked_users list, along with their requested table type/size
        # this should also book their table using the book_table() method
        pass

    def remove_booked_user(self, user, table_type, table_size):
        # removes a user from the booked list when their reservation is over
        # this should also remove their table from booked tables list using 
        # the remove_booked_table() method
        pass

    def add_available_table(self, table):
        # add table objects to restaurant's available tables list
        pass
    
    def get_available_tables(self):
        return self.__available_tables


    def book_table(self, table_type,table_size):
        # users reserve a table by type and size
        # table will be removed from available tables list and be added to booked tables list
        pass
    
    def remove_booked_table(self,table_type,table_size):
        # removes the given table from the booked_tables list 
        # this table will be re-added to available tables list 
        pass
    

    def get_booked_tables(self):
        return self.__booked_tables
        



class Table:
    # Different restaurants will have different seating arrangements, that includes the type of tables (ex: booth, regular, patio/outdoor) 
    # and number of seats at eatch table (ex: 2,4, etc)
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













    

