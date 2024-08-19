class AtmMachine():
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
    How can I help?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. press 4 to withdraw
    5. press anything to exit                       
    
    """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()
    def create_pin(self):
        user_pin = input('Enter the Pin: ')
        confirm_pin = input('Re-enter the pin: ')
        if user_pin == confirm_pin:
            self.pin = user_pin
        else:
            self.create_pin()
        user_balance = int(input('Enter the balance: '))
        self.balance = user_balance
        print('Pin Created Successfilly!!!')
        self.menu()
    def change_pin(self):
        pass
    def check_balance(self):
        pass
    def withdraw(self):
        pass

        

atm = AtmMachine()
print(atm.pin)