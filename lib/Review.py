class Review:
    # Class variable to store all instances of Review
    all_reviews = []
    
    def __init__(self, customer, restaurant, rating):
        # Instance variables for each review
        self.customer_instance = customer
        self.restaurant_instance = restaurant
        self._rating = rating = rating
        Review.all_reviews.append(self)  # Add the instance to the class variable
        customer.reviews.append(self)   # Add the review to the customer's list of reviews
        restaurant.reviews.append(self)  # Add the review to the restaurant's list of reviews

    def get_rating(self):
        # Method to get the rating for this review
        return self._rating

    @classmethod
    def all(cls):
        # Class method to get a list of all review instances
        return cls.all_reviews

    def get_customer(self):
        # Method to get the customer object for this review
        return self.customer_instance

    def get_restaurant(self):
        # Method to get the restaurant object for this review
        return self.restaurant_instance
