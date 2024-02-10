
class UserInfo():

    def __init__(self, name, email, password, budget=0):
        self.name = name
        self.id = id(self)
        self.email = email
        self.password= password
        self.budget = budget
    

    