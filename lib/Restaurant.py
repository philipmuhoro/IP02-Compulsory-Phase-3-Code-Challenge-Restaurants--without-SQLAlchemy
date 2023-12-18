class Restaurant:
    # Class variable to store all instances of Restaurant
    all_restaurants = []
    
    def __init__(self, name):
        # Instance variables for each restaurant
        self.name = name
        self.reviews = []  # List to store reviews associated with this restaurant
        Restaurant.all_restaurants.append(self)  # Add the instance to the class variable
        
    def get_name(self):
        # Method to get the name of the restaurant
        return self.name