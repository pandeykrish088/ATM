class Atm():
    def __init__(self, Card_Number, Pin_Number):
        self.Card_Number = Card_Number
        self.Pin_Number = Pin_Number

    def card(self):
        cardNumber = input("")
        print("Enter your Card Number: " + cardNumber)

    def pin(self):
        pinNumber = input("")
        print("Enter your Pin Number: " + pinNumber)