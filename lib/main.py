# Example usage for the Customer, Restaurant, and Review classes
# Import your classes
from Customer import Customer
from Restaurant import Restaurant
from Review import Review
# Create customers
customer1 = Customer("Philip", "Muhoro")
customer2 = Customer("Linda", "Mukami")

# Create restaurants
restaurant1 = Restaurant("Mama Oliech Restaurant")
restaurant2 = Restaurant("Pilau Whole Bar and Restaurant")

# Customers adding reviews for restaurants
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Accessing information about customers
print("Customer 1 Full Name:", customer1.full_name())
print("Customer 2 Full Name:", customer2.full_name())

# Accessing information about restaurants
print("Restaurant 1 Name:", restaurant1.get_name())
print("Restaurant 2 Reviews:", restaurant2.get_reviews())

# Accessing reviews for a specific customer
print("Customer 1 Reviews:", [review.get_rating() for review in customer1.reviews])

# Accessing information about a review
review1 = customer1.reviews[0]
print("Review 1 Rating:", review1.get_rating())
print("Review 1 Customer:", review1.get_customer().full_name())
print("Review 1 Restaurant:", review1.get_restaurant().name)

# Accessing unique customers who reviewed a restaurant
print("Restaurant 1 Customers:", [customer.full_name() for customer in restaurant1.customers()])

# Calculating average star rating for a restaurant
print("Restaurant 1 Average Star Rating:", restaurant1.average_star_rating())

# Finding a customer by name
found_customer = Customer.find_by_name("Philip Muhoro")
print("Found Customer:", found_customer.full_name() if found_customer else "Customer not found")

# Finding all customers by given name
all_customers_with_given_name = Customer.find_all_by_given_name("Philip")
print("All Customers with Given Name 'Philip':", [customer.full_name() for customer in all_customers_with_given_name])
