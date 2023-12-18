from lib.Review import Review

class Customer:
    # Class variable to store all instances of Customer
    all_customers = []
    
    def __init__(self, given_name, family_name):
        # Instance variables for each customer
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)  # Add the instance to the class variable
        self.reviews = []  # List to store reviews associated with this customer
        
        
    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def all(cls):
        return cls.all_customers

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        # Class method to find a customer by full name
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        # Class method to find all customers by given name
        return [customer for customer in cls.all_customers if customer.given_name == name]

    def add_review(self, restaurant, rating):
        # Method to add a review for this customer
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        return review