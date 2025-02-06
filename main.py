# Important Conventions Used in the Project :-
#       PascalCase -> Class Name
#       camelCase -> Function's / Method's  Name
#       snake_case -> Attribute's / Variables  Name


# All the Important and Useful Modules / Packages are Imported Here.

import os
import time
import hashlib
import re
import json
from abc import ABC, abstractmethod


# If you Don't Have Installed Tabulate and Maskpass Modules (External Modules) then Don't Worry.
# We will Install Them for you Just Run the Application and Wait Few Seconds.
try:
    import tabulate
except:
    os.system('pip install tabulate')
    import tabulate

try:
    import maskpass
except:
    os.system('pip install maskpass')
    import maskpass



# These are the Builtin Modules (You Already Have).



# To clear the terminal.
def clearScreen():
    
    # For Windows
    if os.name == 'nt':  
        os.system('cls')
    
    
    # For MacOs and Linux
    else:
        os.system('clear')


# To Print Simple Text with Animation.
def printAnimated(text, delay=0.001):
    
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    
    print()

# To check the Strength of Password.
def isStrongPassword(password):
    
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return (False, 'Password must be Greater than 8 Characters!')
    
    # Check if the password contains at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return (False, 'Password must Contain at least one Uppercase letter')
    
    # Check if the password contains at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return (False, 'Password must Contain at least one Lowercase letter')
    
    # Check if the password contains at least one digit
    if not re.search(r"[0-9]", password):
        return (False, 'Password must Contain at least one Digit')
    
    # Check if the password contains at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return (False, 'Password must Contain at least one Special Character')
    
    return (True, 'Password is Strong Enough')


# To Handle the User Input Errors
class WrongInputError(Exception):
    pass

# To Hash Password for Security Purposes.
def hashPassword(password):
        return hashlib.sha256(password.encode()).hexdigest()


# Class : 1
# Account Class (Abstract Class) which is used by both Customer and Admin Class.
class Account(ABC):
    
    def __init__(self, first_name, last_name, gender, date_of_birth, email, username) -> None:
        
        # All the Personal Deatails of a Customer or Admin.
        self._first_name = first_name        
        self._last_name = last_name       
        self._username = username        
        self._email = email               
        self._date_of_birth = date_of_birth        
        self._gender = gender
    
    
    @abstractmethod
    def __str__(self) -> str:
        
        res = f'{self._first_name} {self._last_name} {self._username} {self._email} {self._date_of_birth} {self._gender}'
        return res


# Class : 2
class Customer(Account):
    
    def __init__(self, first_name, last_name, gender, date_of_birth, email, username, password, encoded = False):
        super().__init__(first_name, last_name, gender, date_of_birth, email, username)

        if not encoded:
            self.password = hashPassword(password)
        
        else:
            self.password = password
        self.cart = Cart(self)
    
    
    def __str__(self) -> str:
        pass

    
    # Getters and Setters for Customer's Attributes.
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) == str:
            self._first_name = new_first_name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) == str:
            self._last_name = new_last_name
    
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, new_gender):
        if type(new_gender) == str:
            self._gender = new_gender
    
    @property
    def date_of_birth(self):
        return self._date_of_birth
    
    @date_of_birth.setter
    def date_of_birth(self, new_date_of_birth):
        if type(new_date_of_birth) == str:
            self._date_of_birth = new_date_of_birth
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        if type(new_email) == str:
            self._email = new_email
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if type(new_username) == str:
            self._username = new_username
    
    
    # To Update Personal Details of the Customer on his Demand.
    def updatePersonalDetails(self):
        
        data = [
            [1, 'First Name'],
            [2, 'Last Name'],
            [3, 'Gender'],
            [4, 'Date of Birth'],
            [5, 'E-mail'],
            [6, 'Username'],
        ]

        clearScreen()
        print()
        printAnimated('What You Want to Update?')
        print()
        print(tabulate.tabulate(data, tablefmt='pretty', colalign=('center', 'left')))
        print()
        
        choice = input()

        if choice == '1':
            new_first_name = input('Enter New First Name : ')
            self.first_name = new_first_name
            printAnimated('Your First Name is Changed Successfully...')
            time.sleep(2)

        elif choice == '2':
            new_last_name = input('Enter New Last Name : ')
            self.last_name = new_last_name
            printAnimated('Your Last Name is Changed Successfully...')
            time.sleep(2)

        elif choice == '3':
            new_gender = input('Enter New Gender : ')
            self.gender = new_gender
            printAnimated('Your Gender is Changed Successfully...')
            time.sleep(2)

        elif choice == '4':
            new_date_of_birth = input('Enter New Date of Birth : ')
            self.date_of_birth = new_date_of_birth
            printAnimated('Your Date of Birth is Changed Successfully...')
            time.sleep(2)

        elif choice == '5':
            new_email = input('Enter New Email : ')
            self.email = new_email
            printAnimated('Your Email is Changed Successfully...')
            time.sleep(2)

        elif choice == '6':
            new_username = input('Enter New Username : ')
            self.username = new_username
            printAnimated('Your Username is Changed Successfully...')
            time.sleep(2)

        else:
            printAnimated('Invalid Option')

        self.saveToFile()


    # To Check Password.
    def checkPassword(self, password):
        return self.password == hashPassword(password)


    # To Change Password on User's demand.
    def changePassword(self, old_password, new_password):
        
        # If Old Password is Matched.
        if self.checkPassword(old_password):
            
            flag = isStrongPassword(new_password)
            if not flag[0]:
                printAnimated(flag[1])
                time.sleep(2)
                return

            self.password = hashPassword(new_password)
            self.saveToFile()
            printAnimated("Password Changed Successfully!")
            time.sleep(2)
        
        # If Old Password does not Matched.
        else:
            printAnimated("Old Password is Incorrect!")
            time.sleep(2)


    # To Save User's Credentials to his File which is named by his Username. 
    def saveToFile(self):

        with open(f'{self._username}.txt', 'w') as file:
            file.write(f"{self._first_name}\n{self._last_name}\n{self._gender}\n{self._date_of_birth}\n{self._email}\n{self._username}\n{self.password}")


    # Loading Data from User's File.
    @staticmethod
    def loadFromFile(username):
        
        # If File is Present.
        try:
            with open(f'{username}.txt', 'r') as file:
                lines = file.read().splitlines()
                if len(lines) != 7:
                    return None
                return Customer(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], True)
        

        # If File is not there.
        except FileNotFoundError:
            return None



    # To save User's Purchasing Details in his File which is named by username_database File.
    def savePurchase(self, items, total):
        
        with open(f'{self.username}_database.txt', 'a') as file:
            file.write(f"Purchase on {time.ctime()}:\n")
            for item in items:
                product = item['product']
                quantity = item['quantity']
                file.write(f"Product: {product.name}, Quantity: {quantity}, Subtotal: ${product.price * quantity:.2f}\n")
            file.write(f"Total: ${total:.2f}\n\n")


    # To show User's Past Purchases on his Demand.
    def viewPurchases(self):
        # If Customer is not coming First Time.
        try:
            with open(f'{self.username}_database.txt', 'r') as file:
                printAnimated(file.read())
        
        # If Customer is New Here.
        except FileNotFoundError:
            printAnimated("No purchase history found!")
            time.sleep(2)


# Class : 3
class Admin(Customer):
    
    def __init__(self, first_name, last_name, gender, date_of_birth, email, username, password, encoded = False):
        super().__init__(first_name, last_name, gender, date_of_birth, email, username, password, encoded)
        self.saveAdminToFile()

    
    # Getters and Setters for Admin's Attributes.

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) == str:
            self._first_name = new_first_name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) == str:
            self._last_name = new_last_name
    
    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, new_gender):
        if type(new_gender) == str:
            self._gender = new_gender
    
    @property
    def date_of_birth(self):
        return self._date_of_birth
    
    @date_of_birth.setter
    def date_of_birth(self, new_date_of_birth):
        if type(new_date_of_birth) == str:
            self._date_of_birth = new_date_of_birth
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        if type(new_email) == str:
            self._email = new_email
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if type(new_username) == str:
            self._username = new_username
    
    # To Update Personal details of Admin.
    def updatePersonalDetails(self):
        
        clearScreen()
        print()
        printAnimated('What You Want to Update?')
        print()
    
        data = [
            [1, 'First Name'], 
            [2, 'Last Name'], 
            [3, 'Gender'], 
            [4, 'Date of Birth'], 
            [5, 'Email'], 
            [6, 'Username']
        ]
    
        print(tabulate.tabulate(data, tablefmt='pretty', colalign=('center', 'left')))
        print()
        
        choice = input()

        if choice == '1':
            new_first_name = input('Enter New First Name : ')
            self.first_name = new_first_name
            printAnimated('Your First Name is Changed Successfully...')
            time.sleep(2)

        elif choice == '2':
            new_last_name = input('Enter New Last Name : ')
            self.last_name = new_last_name
            printAnimated('Your Last Name is Changed Successfully...')
            time.sleep(2)

        elif choice == '3':
            new_gender = input('Enter New Gender : ')
            self.gender = new_gender
            printAnimated('Your Gender is Changed Successfully...')
            time.sleep(2)

        elif choice == '4':
            new_date_of_birth = input('Enter New Date of Birth : ')
            self.date_of_birth = new_date_of_birth
            printAnimated('Your Date of Birth is Changed Successfully...')
            time.sleep(2)

        elif choice == '5':
            new_email = input('Enter New Email : ')
            self.email = new_email
            printAnimated('Your Email is Changed Successfully...')
            time.sleep(2)

        elif choice == '6':
            new_username = input('Enter New Username : ')
            self.username = new_username
            printAnimated('Your Username is Changed Successfully...')
            time.sleep(2)

        else:
            printAnimated('Invalid Option!')

        self.saveAdminToFile()


    # To add product in the Shopping Inventory.
    def addProduct(self, store, product, quantity):
        
        store.addProduct(product, quantity)
        printAnimated(f"Product {product.name} Added Successfully With Quantity {quantity}!")
        time.sleep(2)

    
    # To remove Product from the Shopping Inventory.
    def removeProduct(self, store, product_id, quantity):
        
        # If the Quantity is Not Greater Than the Present Quantity of Product.
        if store.removeProduct(product_id, quantity):
            printAnimated(f"Product With ID {product_id} Quantity {quantity} Removed Successfully!")
            time.sleep(2)
    
        else:
            printAnimated(f"Product With ID {product_id} not Found or Insufficient Quantity!")
            time.sleep(2)

    
    # To Save Admin's Credentials to his File named by his Username.
    def saveAdminToFile(self):
    
        file = open(f'{self._username}_admin.txt','w')
        file.write(f'{self._first_name}\n{self._last_name}\n{self._gender}\n{self._date_of_birth}\n{self._email}\n{self._username}\n{self.password}')
        file.close()
    
    
    # To get Admin's Details From his File.
    @staticmethod
    def loadAdminFromFile(username):
    
        file = open(f'{username}_admin.txt', 'r')
        data = file.readlines()
        data = [x.strip() for x in data]
        return Admin(data[0], data[1], data[2], data[3], data[4], data[5], data[6], True)


# Class : 4
class Product:
    
    def __init__(self, product_id, name, price, quantity):
    
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity = quantity
    
    
    # Returning Details of Product in a Dictionary.
    def toDict(self):
    
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
    

    # Getters and Setters for Product's Attributes.

    @property
    def name(self):
        return self._name

    @property
    def product_id(self):
        return self._product_id

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str:
            self._name = new_name

    @product_id.setter
    def product_id(self, new_product_id):
        if type(new_product_id) == str:
            self._product_id = new_product_id

    @price.setter
    def price(self, new_price):
        if type(new_price) == int:
            self._price = new_price

    @quantity.setter
    def quantity(self, new_quantity):
        if type(new_quantity) == int:
            self._quantity = new_quantity


    # Returning Product type Object from the Provided Details of the Product.  
    @staticmethod
    def fromDict(data):
    
        return Product(data['product_id'], data['name'], data['price'], data['quantity'])


# Class : 5
class Cart:
    
    def __init__(self, customer):
    
        self.user = customer    # User type Object.
        self.items = {}

    
    # To add Item in Customer's Cart.
    def addItem(self, product, quantity):
        
        # Out of Stock Condition.
        if quantity > product.quantity:
            printAnimated(f"Cannot add {quantity} items. Only {product.quantity} available.")
            time.sleep(2)
            return False
        
        # If Product is Already Present inside the Cart.
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        
        # If the Product is not Already in Cart.
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}
        
        # Decreasing Quantity of Product from the Inventory.
        product.quantity -= quantity
        return True


    # To Remove Product From Customer's Cart.
    def removeItem(self, product_id, quantity):
        
        # If Product is Present inside the Customer's Cart.
        if product_id in self.items:
            
            # If Quantity to Remove is Less Than the Quantity inside the Cart.
            if self.items[product_id]['quantity'] > quantity:
                self.items[product_id]['quantity'] -= quantity
                self.items[product_id]['product'].quantity += quantity
                return True
            

            # If Quantity to Remove is Equal to the Quantity inside the Cart.
            elif self.items[product_id]['quantity'] == quantity:
                self.items[product_id]['product'].quantity += quantity
                del self.items[product_id]
                return True
            
            
            # If Quantity to Remove is Greater Than the Quantity inside the Cart.
            else:
                printAnimated("Quantity to Remove Exceeds Quantity in Cart!")
                time.sleep(2)
                return False
        

        # If Product is not in Cart.
        else:
            printAnimated("Product is not in Your Cart!")
            time.sleep(2)
            return False

    
    # To show the Cart of Customer on his Demand.
    def viewCart(self):
    
        # If Cart is Empty.
        if not self.items:
            printAnimated("Your cart is empty!")
            time.sleep(2)
            return False

        # Counting Total Price.
        total = 0
        

        # Counting Total Price as well as Showing Customer his Products.
        headers = ['ID', 'NAME', 'QUANTITY', 'SUB-TOTAL in PKR']
        data = []

        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            subtotal = product.price * quantity
            total += subtotal
            temp = [product.product_id, product.name, quantity, subtotal]
            data.append(temp)
            #print_animated(f"ID: {product.product_id} | Name: {product.name} | Quantity: {quantity} | Subtotal: ${subtotal:.2f}")
        
        print(tabulate.tabulate(data, headers, tablefmt='grid', colalign=('center', 'center', 'center', 'center')))

        # Showing Customer his Total Price.
        printAnimated(f"\nTotal: ${total:.2f}")
        
        time.sleep(2)
        return True

    
    # When Customer wants to Checkout.
    def checkout(self):
    
        # If Cart is Empty.
        if not self.items:
            clearScreen()
            printAnimated("Your Cart is Empty!")
            time.sleep(2)
            return

        self.viewCart()
        
        confirm = input("\nDo You Want to Proceed to Checkout? [Yes / No]: ")
        
        # If Customer Confirms to Checkout.
        if confirm.lower() == 'yes':
            total = sum(item['product'].price * item['quantity'] for item in self.items.values())
            self.user.savePurchase(self.items.values(), total)
            self.items = {}
            printAnimated("Checkout Successful! Your cart is now Empty.")
            time.sleep(2)
        

        # If User Choose not to Checkout.
        else:
            printAnimated("Checkout Cancelled.")
            time.sleep(2)


# Class : 6
class Store:
    
    def __init__(self):
    
        self.products = {}
        self.users = {}
        self.admins = {}
        self.loadProducts()

    
    # To Add Product in the Shopping Inventory.
    def addProduct(self, product, quantity):
    
        # If Product is Already Present in the Shopping Inventory.
        if product.product_id in self.products:
            self.products[product.product_id].quantity += quantity
        
        # If Product is not Present in the Shopping Inventory.
        else:
            self.products[product.product_id] = product
            self.products[product.product_id].quantity = quantity

    
    
    # To Remove Product from the Shopping Inventory.
    def removeProduct(self, product_id, quantity):
        
        # If Product is Present in the Shopping Inventory.
        if product_id in self.products:
        
            # If Quantity to Remove is not Greater Than Quantity of Product.
            if self.products[product_id].quantity >= quantity:
                self.products[product_id].quantity -= quantity

                # If Quantity Of Product Becomes Zero Then Remove That Product.
                if self.products[product_id].quantity == 0:
                    del self.products[product_id]
        
                return True
        
        return False

    
    def getProduct(self, product_id):
    
        return self.products.get(product_id)

    
    # To Register Customer.
    def registerUser(self, first_name, last_name, gender, date_of_birth, email, username, password):
    
        # If Customer with this Username Already Exists.
        if os.path.exists(f'{username}.txt'):
            printAnimated("User With this Username Already Exists!\nPlease Try a Different One...")
            time.sleep(2)
            
            return False
    

        # If Username is Unique.
        user = Customer(first_name, last_name, gender, date_of_birth, email, username, password)
        user.saveToFile()
        self.users[username] = user
        printAnimated(f"User {username} Registered Successfully!")
        time.sleep(2)
        
        return True

    
    # To Register Admin.
    def registerAdmin(self, first_name, last_name, gender, date_of_birth, email, username, password):
    
        # If Admin with this Username Already Exists.
        if os.path.exists(f'{username}_admin.txt'):
            printAnimated("Admin With This Username Already Exists!")
            time.sleep(2)
    
            return False

        # If Admin's Username is Unique.
        admin = Admin(first_name, last_name, gender, date_of_birth, email, username, password)
        self.admins[username] = admin
        printAnimated(f"Admin {username} Registered Successfully!")
        time.sleep(2)
    
        return True


    # When a Customer is Logging In.
    def authenticateUser(self, username, password):
        
        user = Customer.loadFromFile(username)
        
        # If Password Matches.
        if user and user.checkPassword(password):
            printAnimated(f"\nCustomer {username} Logged In Successfully!")
            time.sleep(2)
            return user
        
        # If Password does not Match Or No Customer Exists with this Username.
        printAnimated("\nInvalid Username Or Password!")
        time.sleep(2)
        
        return None

    
    # When an Admin is Logging In.
    def authenticateAdmin(self, username, password):
        
        # If Admin is Present with this Username.
        if os.path.exists(f'{username}_admin.txt'):
            admin = Admin.loadAdminFromFile(username)
    
            # If Password Matches.
            if hashPassword(password) == admin.password:
                printAnimated(f'\nAdmin {username} Logged In Successfully...')
                time.sleep(2)
                return admin
    
            # If Password does not match.
            else:
                printAnimated('\nPassword is Incorrect!')
                time.sleep(2)
    
        # If there is no Admin with this Username.
        else:
            printAnimated('\nAdmin Not Found!')
            time.sleep(2)
            return None

    
    # To Show the Products Present in Inventory.
    def viewProducts(self):
        
        headers = ['ID', 'NAME', 'PRICE in PKR', 'QUANTITY']
        
        data = []
        
        printAnimated("\nAvailable Products:")
        print()
        
        for product in self.products.values():
            temp = [product.product_id, product.name.upper(), product.price, product.quantity]
            data.append(temp)
        
        print(tabulate.tabulate(data, headers, tablefmt='grid', colalign=('center', 'center', 'center', 'center')))
    
    # To keep Track of Inventory Products in File.
    def saveProducts(self):
        
        with open('products.txt', 'w') as file:
            json.dump({pid: prod.toDict() for pid, prod in self.products.items()}, file)

    
    # To load the Products from the File.
    def loadProducts(self):
        
        if os.path.exists('products.txt'):
        
            with open('products.txt', 'r') as file:
                products = json.load(file)
                for pid, data in products.items():
                    self.products[int(pid)] = Product.fromDict(data)


# Class : 7
class Application:
    
    def __init__(self):
        
        self.store = Store()

    
    def run(self):
        
        while True:
            
            clearScreen()
            
            data = [
                [1, 'REGISTER AS A CUSTOMER'],
                [2, 'LOGIN AS A CUSTOMER'],
                [3, 'REGISTER AS AN ADMIN'],
                [4, 'LOGIN AS AN ADMIN'],
                [5, 'EXIT']
            ]

            print()
            print(tabulate.tabulate(data, tablefmt='pretty', colalign=('center', 'left')))
            print()
            
            choice = input("Choose An Option: ")

            # Customer Registration.
            if choice == '1':
                
                try:
                    self.customerRegister()
                
                except WrongInputError as wie:
                    print(f'\nWrongInputError : {wie}')
                    input('\nPress Enter to return to the Main Menu...')
                    continue
            

            # Customer Login.
            elif choice == '2':
                self.customerLogin()
            

            # Admin Register.
            elif choice == '3':
                
                try:
                    self.adminRegister()
                
                except WrongInputError as wie:
                    print(f'\nWrongInputError : {wie}')
                    input('\nPress Enter to return to the Main Menu...')
                    continue
            

            # Admin Login.
            elif choice == '4':
                self.adminLogin()
            

            # Exit The Application.
            elif choice == '5':
                self.store.saveProducts()
                printAnimated("\nExiting The Application. Goodbye!")
                time.sleep(1)
                break
            

            # Invalid Option is Chosen by User.
            else:
                printAnimated("Invalid Choice! Please Try Again...")
                time.sleep(2)

    

    # Customer Registration.
    def customerRegister(self):
    
        clearScreen()
    
        printAnimated("REGISTRATION OF A CUSTOMER :")
        print()

        first_name = input('Enter First Name : ')
        
        if first_name.isdigit():
            raise WrongInputError('Name can\'t be a Number!')
            
        last_name = input('Enter Last Name : ')
        
        if last_name.isdigit():
            raise WrongInputError('Name can\'t be a Number!')
            
        gender = input('Enter Gender : ')
        
        if gender.isdigit():
            raise WrongInputError('Gender can\'t contain a Number!')
        
        date_of_birth = input('Enter Date Of Birth : ')
        email = input("Enter E-mail: ")
        username = input("Enter Username: ")
        password = maskpass.askpass("Enter Password: ")
        confirm_password = maskpass.askpass("Confirm Password: ")

        if password != confirm_password:
            printAnimated("Passwords Do Not Match!")
            time.sleep(2)
            return
        
        flag = isStrongPassword(password)
        if not flag[0]:
            printAnimated(flag[1])
            time.sleep(2)
            return

        self.store.registerUser(first_name, last_name, gender, date_of_birth, email, username, password)

    
    # Customer Login.
    def customerLogin(self):
    
        clearScreen()
    
        printAnimated("LOGGING IN AS A CUSTOMER : ")
        print()

        username = input("Enter Username: ")
        password = maskpass.askpass("Enter Password: ")
        user = self.store.authenticateUser(username, password)
    
        if user:
            self.customerMenu(user)

    
    # Admin Registration.
    def adminRegister(self):
    
        clearScreen()
    
        printAnimated("REGISTRATION OF AN ADMIN : ")
        print()
    
        first_name = input('Enter First Name : ')

        if first_name.isdigit():
            raise WrongInputError('Name can\'t be a Number!')
        
        last_name = input('Enter Last Name : ')

        if last_name.isdigit():
            raise WrongInputError('Name can\'t be a Number!')
         
        gender = input('Enter Gender : ')

        if gender.isdigit():
            raise WrongInputError('Gender can\'t be a Number!')
         
        date_of_birth = input('Enter Date Of Birth : ')
        email = input("Enter E-mail : ")
        username = input("Enter Admin Username : ")
        password = maskpass.askpass("Enter Password : ")
        confirm_password = maskpass.askpass("Confirm Password : ")

        if password != confirm_password:
            printAnimated("Passwords Do Not Match!")
            time.sleep(2)
            return
        
        flag = isStrongPassword(password)
        if not flag[0]:
            printAnimated(flag[1])
            time.sleep(2)
            return

        self.store.registerAdmin(first_name, last_name, gender, date_of_birth, email, username, password)

    
    # Admin Login.
    def adminLogin(self):
    
        clearScreen()
    
        printAnimated("LOGGING IN AS AN ADMIN : ")
        print()
    
        username = input("Enter Admin Username : ")
        password = maskpass.askpass("Enter Password : ")
        admin = self.store.authenticateAdmin(username, password)

        if admin:
            self.adminMenu(admin)

    
    # Customer's Menu.
    def customerMenu(self, user):
        
        while True:
        
            clearScreen()

            data = [
                [1, 'VIEW PRODUCTS'],
                [2, 'ADD TO CART'],
                [3, 'VIEW CART'],
                [4, 'REMOVE FROM CART'],
                [5, 'CHECKOUT'],
                [6, 'VIEW PURCHASE HISTORY'],
                [7, 'CHANGE PERSONAL DETAILS'],
                [8, 'CHANGE PASSWORD'],
                [9, 'LOGOUT']
            ]
            print()
            print('       <---CUSTOMER--->')
            print('       <---MAIN MENU--->')
            print(tabulate.tabulate(data, tablefmt='pretty', colalign=('center', 'left')))
            print()
        
            choice = input("Choose An Option : ")

            # To Show the Inventory Products.
            if choice == '1':
                clearScreen()
                self.store.viewProducts()
                input("\nPress Enter to Return to the Main Menu...")
            

            # To add Product in the Cart.
            elif choice == '2':
                self.addToCart(user)
            

            # To Show Products of the Customer's Cart.
            elif choice == '3':
                clearScreen()
                user.cart.viewCart()
                input("\nPress Enter to Return to the Main Menu...")
            

            # To Remove Product From Customer's Cart.
            elif choice == '4':
                if user.cart.viewCart():
                    self.removeFromCart(user)
            

            # To Checkout.
            elif choice == '5':
                clearScreen()
                user.cart.checkout()
                input("\nPress Enter to Return to the Main Menu...")
            

            # To Show the Past Purchase History of Customer.
            elif choice == '6':
                clearScreen()
                user.viewPurchases()
                input("\nPress Enter to Return to the Main Menu...")
            

            
            # To Update Customer's Personal Details on his Demand.
            elif choice == '7':
                user.updatePersonalDetails()
                input('\nPress Enter to Return to the Main Menu...')
            

            # To Change the Customer's Password.
            elif choice == '8':
                self.changePassword(user)

            # Logout.
            elif choice == '9':
                break
            
            # Invalid Option is Chosen by Customer.
            else:
                printAnimated("Invalid Choice! Please Try Again...")
                time.sleep(2)

    
    # Admin's Menu.
    def adminMenu(self, admin):
    
        while True:
    
            clearScreen()
    
            data = [
                [1, 'VIEW PRODUCTS'],
                [2, 'ADD PRODUCT'],
                [3, 'REMOVE PRODUCT'],
                [4, 'UPDATE PERSONAL DETAILS'],
                [5, 'CHANGE PASSWORD'],
                [6, 'LOGOUT']
            ]
            print()
            print('         <---ADMIN--->')
            print('       <---MAIN MENU--->')
            print(tabulate.tabulate(data, tablefmt='pretty', colalign=('center', 'left')))
            print()
    
            choice = input("Choose An Option: ")


            # To Show the Products of Inventory.
            if choice == '1':
                clearScreen()
                self.store.viewProducts()
                input("\nPress Enter to Return to the Main Menu...")
            

            # To Add a Product in the Inventory.
            elif choice == '2':
                self.addProduct(admin)
            

            # To Remove Product From the Inventory.
            elif choice == '3':
                self.removeProduct(admin)
            

            # To Update Admin's Personal Details on his Demand.
            elif choice == '4':
                admin.updatePersonalDetails()
                input('Press Enter to Return to the Main Menu...')
            

            # To Change the Admin's Password.
            elif choice == '5':
                self.changePassword(admin)

            # When Admin Choose to Logout then Save Inventory Products into the File.
            elif choice == '6':
                self.store.saveProducts()
                break
            
            # Invalid Option is Chosen by the Admin.
            else:
                printAnimated("Invalid Choice! Please Try Again...")
                time.sleep(2)

    

    # To Add Product in the Inventory.
    def addProduct(self, admin):
    
        clearScreen()
    
        product_id = int(input("\nEnter the New Product ID: "))
        name = input("Enter the Product Name: ")
        price = float(input("Enter the Product Price: "))
        quantity = int(input("Enter the Product Quantity: "))
        product = Product(product_id, name, price, quantity)

        admin.addProduct(self.store, product, quantity)

   
   # To Remove Product From the Inventory.
    def removeProduct(self, admin):
   
        clearScreen()
   
        product_id = int(input("\nEnter the Product ID to Remove: "))
        quantity = int(input("Enter the Quantity to Remove: "))
        admin.removeProduct(self.store, product_id, quantity)

    
    # To Add Product to the Customer's Cart.
    def addToCart(self, user):
    
        clearScreen()
    
        self.store.viewProducts()
        product_id = int(input("\nEnter the Product ID to Add to the Cart: "))
        quantity = int(input("Enter the Quantity: "))
        product = self.store.getProduct(product_id)

        if product:
            flag = user.cart.addItem(product, quantity)
            if flag:
                printAnimated(f"Product Added to Cart with Quantity {quantity}!")
                time.sleep(2)
        
        else:
            printAnimated("Invalid Product ID!")
            time.sleep(2)

    

    # To Remove Product from the Customer's Cart.
    def removeFromCart(self, user):
    
        clearScreen()
    
        user.cart.viewCart()
        product_id = int(input("\nEnter the product ID to remove from the cart: "))
        quantity = int(input("Enter the quantity to remove: "))
        if user.cart.removeItem(product_id, quantity):
            printAnimated(f"Product removed from cart with quantity {quantity}!")
        time.sleep(2)

    
    # To Change Password.
    def changePassword(self, user):
    
        clearScreen()
    
        # Asking Old Password from User.
        old_password = maskpass.askpass("Enter Old Password: ")
    
        # If Password Matches ( Hash of both Passwords ).
        if hashPassword(old_password) == user.password:
            new_password = maskpass.askpass("Enter New Password: ")
            confirm_new_password = maskpass.askpass("Confirm New Password: ")


            # If New Passwords are not Matching.
            if new_password != confirm_new_password:
                printAnimated("New Passwords Do Not Match!")
                time.sleep(2)
                return
            
            flag = isStrongPassword(new_password)
            if not flag[0]:
                printAnimated(flag[1])
                time.sleep(2)
                return
            
            # If all the Conditions are Satisfied then Finally Change the Password.
            user.changePassword(old_password, new_password)
            
            if type(user) == Admin:
                user.saveAdminToFile()
        
        else:
            printAnimated('Password is Incorrect!')



# If we are Running this File ( Not Importing it from Anywhere Else ).
if __name__ == "__main__":
    app = Application()
    clearScreen()
    app.run()