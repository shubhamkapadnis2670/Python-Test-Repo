class Robot():
    def __init__(self,name,color,weight):
        self.name = name 
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f'My Name is {self.name}')



class Circle():
    def __init__(self,radius):
        self.radius = radius
        

    def area(self):
        area = (22/7) * (self.radius**2)
        print(f'area : {area}')
    def circumference(self):
        circumference = (22/7) * (self.radius *2)
        print(f'circumference: {circumference}')


class BankAccount():
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self):
        deposit_amount = int(input('Enter the amount you want to deposit: '))
        self.balance = self.balance + deposit_amount
        print(f'Updated account balance is {self.balance}')

    def withdraw(self):
        withdraw_amount = int(input('Enter the amount you want to withdraw: '))
        if withdraw_amount <= self.balance:
            self.balance = self.balance - withdraw_amount
            print(f'Successfully withdrew Rs.{withdraw_amount}. Remaining amount is {self.balance}')

        else:
            print('Insufficient Balance....')
    def account_details(self):
        print(f'Account Number : {self.account_number}')
        print(f'Account Name : {self.name}')
        print(f'Account Balance : {self.balance}')


class Car():
    def __init__(self,milage,year,make,model):
        self.milage = milage
        self.year = year
        self.make = make
        self.model = model
    
    def age(self,current_year):
        return current_year - self.year
    
    def milage1(self):
        print(f'milage of car is {self.milage}')


nano = Car(45,2009,'Tata','Nano')


class Student():
    def __init__(self,name,rollno,joining_date,current_topic):
        self.name = name 
        self.rollno = rollno
        self.joining_date = joining_date
        self.current_topic = current_topic

    def cur_topic(self):
        print(f'Current topic discussed in class is {self.current_topic}')

    def str_rollno(self):
        try:
            if type(self.rollno) == str:
                print('do nothing')
            else:
                return str(self.rollno)
            
        except Exception as e:
            print(f'Error occurred {str(e)}')


    def duration(self,current_date):
        print(f'Duration of student in my class is {current_date - self.joining_date}')

    def __str__(self) -> str:
        return 'This is student class'
    

class test:
    def __init__(self):
        self.a = 5
        self._b = 10
        self.__c = 15

    def show(self):
        print(f'Public : {self.a}, Protected : {self._b}, Private : {self.__c}')

t1 = test()
t1._test__c



########## Encapsulation ##########
class Tyres():
    def __init__(self, branch,belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure

    def __str__(self):
        return(f'Tyres: \n \t Branch {self.branch} \n \t Belted Bias {str(self.belted_bias)} \n \t Optimal Pressure {str(self.opt_pressure)}')
    
class Engine():
    def __init__(self,fuel_type,noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level
    
    def __str__(self):
        return(f'Engine: \n \t Fuel Type {self.fuel_type} \n \t Noise Level {self.noise_level}')
    
class Car():
    def __init__(self,tyres, engine):
        self.tyres = tyres
        self.engine = engine
    def __str__(self):
        return(f'{str(self.tyres)} \n {str(self.engine)}')
    

    
t1 = Tyres('Nashik', True, 45)
e1 = Engine('Petrol', 'Nominal')
print(t1)
print(e1)
c1 = Car(t1, e1)
print(c1)
        




