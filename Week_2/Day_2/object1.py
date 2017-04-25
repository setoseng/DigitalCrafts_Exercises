class Person:
    def __init__(self, name, email, phone,friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greeting_count = 0
    def greet(self, other_person):
        print ('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count = self.greeting_count+1
    def print_contact_info(self):
    	print(self.name,"'s email: ",self.email,self.name,"'s phone number is: ",self.phone)
    def add_friends(self,friend):
    	self.friends.append(friend)
    def num_friends(self):
    	print(len(self.friends))
    def num_unique_people_greeted(self):
    	print(self.friends)
 
    def __str__(self):
    	return 'Person:{} {} {}'.format(self.name, self.email, self.phone)

sonny = Person("Sonny","sonny@hotmail.com","888-888-8888",[])
jordan = Person("Jordan","jordan@aol.com","495-586-3456",[])
jordan.friends.append(sonny)
print(len(jordan.friends))
sonny.greet(jordan)
jordan.greet(sonny)
sonny.print_contact_info()
jordan.add_friends(sonny)
jordan.num_friends()
jordan.num_unique_people_greeted()
print(sonny)