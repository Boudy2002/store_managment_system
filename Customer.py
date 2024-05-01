class Customer:
    def __init__(self, first_name, last_name, email, address, city, state, zipcode, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.zipcode = zipcode
        self.password = password
        self.id = None
        self.city = city
        self.state = state