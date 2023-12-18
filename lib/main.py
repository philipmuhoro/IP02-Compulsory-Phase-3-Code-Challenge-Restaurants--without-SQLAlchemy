from lib.Review import Review

class Customer:
    # Class variable to store all instances of Customer
    all_customers = []
    
    def __init__(self, given_name, family_name):
        # Instance variables for each customer
        self.given_name = given_name
        
        
    def given_name(self):
        return self.given_name