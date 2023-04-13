# POS system for Mulago Hospital

# Import necessary libraries

import datetime

import decimal

import requests

# Define currencies

currencies = {

    "USD": "United States Dollar",

    "EUR": "Euro",

    "UGX": "Ugandan Shilling"

}

# Define vulnerable groups

vulnerable_groups = {

    "elderly": 0.5,

    "children": 0.7,

    "disabled": 0.8,

    "students": 0.6,

    "refugees": 0.9

}

# Define health services

health_services = {

    "checkup": "Checkup",

    "x-ray": "X-Ray",

    "ultrasound": "Ultrasound",

    "dentistry": "Dentistry"

}

# Define payment methods

payment_methods = {

    "cash": "Cash",

    "credit": "Credit Card",

    "loan": "Government Loan"

}

# Define user class

class User:

    def __init__(self, name, email, password):

        self.name = name

        self.email = email

        self.password = password

        self.account_created = datetime.datetime.now()

        self.is_ugandan = False

        self.insurance_card_number = None

        self.pin = None

        self.tin = None

        self.wallet = 0

        self.discount = 0

    

    # Function to set Ugandan status

    def set_ugandan(self):

        self.is_ugandan = True

    

    # Function to set insurance card number

    def set_insurance_card_number(self, insurance_card_number):

        self.insurance_card_number = insurance_card_number

    

    # Function to set PIN

    def set_pin(self, pin):

        self.pin = pin

    

    # Function to set TIN

    def set_tin(self, tin):

        self.tin = tin

    

    # Function to set wallet

    def set_wallet(self, wallet):

        self.wallet = wallet

    

    # Function to set discount

    def set_discount(self, discount):

        self.discount = discount

    

    # Function to get user details

    def get_details(self):

        return {

            "name": self.name,

            "email": self.email,

            "is_ugandan": self.is_ugandan,

            "insurance_card_number": self.insurance_card_number,

            "pin": self.pin,

            "tin": self.tin,

            "wallet": self.wallet,

            "discount": self.discount

        }

# Define medicine class

class Medicine:

    def __init__(self, name, price):

        self.name = name

        self.price = price

    

    # Function to get medicine details

    def get_details(self):

        return {

            "name": self.name,

            "price": self.price

        }

# Define appointment class

class Appointment:

    def __init__(self, user, service, date, time, discount):

        self.user = user

        self.service = service

        self.date = date

        self.time = time

        self.discount = discount

    

    # Function to get appointment details

    def get_details(self):

        return {

            "user": self.user,

            "service": self.service,

            "date": self.date,

            "time": self.time,

            "discount": self.discount

        }

# Define payment class

class Payment:

    def __init__(self, user, payment_method, amount, currency):

        self.user = user

        self.payment_method = payment_method

        self.amount = amount

        self.currency = currency

    

    # Function to get payment details

    def get_details(self):

        return {

            "user": self.user,

            "payment_method": self.payment_method,

            "amount": self.amount,

            "currency": self.currency

        }

# Function to create a new user

def create_user(name, email, password):

    user = User(name, email, password)

    return user

# Function to set Ugandan status

def set_ugandan(user):

    user.set_ugandan()

# Function to set insurance card number

def set_insurance_card_number(user, insurance_card_number):

    user.set_insurance_card_number(insurance_card_number)

# Function to set PIN

def set_pin(user, pin):

    user.set_pin(pin)

# Function to set TIN

def set_tin(user, tin):

    user.set_tin(tin)

# Function to set wallet

def set_wallet(user, wallet):

    user.set_wallet(wallet)

# Function to set discount

def set_discount(user, discount):

    user.set_discount(discount)

# Function to buy medicine

def buy_medicine(user, medicine, discount):

    # Calculate total cost

    total_cost = medicine.price - (medicine.price * discount)

    

    # Check if user has enough balance

    if user.wallet >= total_cost: 

        user.wallet -= total_cost

        return True

    else:

        return False

# Function to book an appointment

def book_appointment(user, service, date, time, discount):

    # Create new appointment

    appointment = Appointment(user, service, date, time, discount)

    return appointment

# Function to get exchange rate

def get_exchange_rate(from_currency, to_currency):

    # Make API request

    url = f"https://api.exchangeratesapi.io/latest?base={from_currency}&symbols={to_currency}"

    response = requests.get(url)

    data = response.json()

    

    # Get exchange rate

    exchange_rate = data["rates"][to_currency]

    

    return exchange_rate

# Function to convert currency

def convert_currency(amount, from_currency, to_currency):

    # Get exchange rate

    exchange_rate = get_exchange_rate(from_currency, to_currency)

    

    # Calculate converted amount

    converted_amount = amount * exchange_rate

    

    return converted_amount

# Function to make payment

def make_payment(user, payment_method, amount, currency):

    # Convert amount to UGX if necessary

    if currency != "UGX":

        amount = convert_currency(amount, currency, "UGX")

    

    # Create payment

    payment = Payment(user, payment_method, amount, currency)

    return payment

# Function to manage user

def manage_user(user):

    # Get user details

    user_details = user.get_details()

    

    # Print user details

    print(user_details)

# Function to manage system

def manage_system():

    pass 

#Call necessary functions to make this code functional 

# Create new user

user = create_user("John Doe", "john.doe@example.com", "password123")

# Set Ugandan status

set_ugandan(user)

# Set insurance card number

set_insurance_card_number(user, "123456789")

# Set PIN

set_pin(user, "123456")

# Set TIN

set_tin(user, "987654321")

# Set wallet

set_wallet(user, 10000)

# Set discount

set_discount(user, vulnerable_groups["elderly"])

# Create medicine

medicine = Medicine("Paracetamol", 500)

# Buy medicine

is_purchased = buy_medicine(user, medicine, user.discount)

# Book appointment

appointment = book_appointment(user, health_services["checkup"], "2020-05-21", "09:00", user.discount)

# Make payment

payment = make_payment(user, payment_methods["cash"], 10000, "USD")

# Manage user

manage_user(user)

# Manage system

manage_system()
