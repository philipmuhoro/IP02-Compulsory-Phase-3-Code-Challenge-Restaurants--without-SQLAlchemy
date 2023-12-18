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
    
    @classmethod
    def all(cls):
        # Class method to get a list of all restaurant instances
        return cls.all_restaurants

    def get_reviews(self):
        # Method to get a list of all reviews for this restaurant
        return self.reviews

    def customers(self):
        # Method to get a list of all unique customers who have reviewed this restaurant
        return list(set(review.customer() for review in self.reviews))

    def average_star_rating(self):
        # Method to calculate the average star rating for this restaurant based on its reviews
        if not self.reviews:
            return 0
        total_ratings = sum(review.get_rating() for review in self.reviews)
        return total_ratings / len(self.reviews)
    

# Create restaurants
restaurant1 = Restaurant("Mama Oliech Restaurant")
restaurant2 = Restaurant("Pilau Whole Bar and Restaurant")

# Accessing information about restaurants
print("Restaurant 1 Name:", restaurant1.get_name())
print("Restaurant 2 Name:", restaurant2.get_name())