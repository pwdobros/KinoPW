import json
from datetime import datetime
import smtplib
import os

PATH = "rentals.json"

def rent_bike(customer_name, rental_duration):
    "A function that takes the customer's name and rental time"
    def calculate_cost(rental_duration):
        "Calculates cost of rental"
        rental_duration = datetime.strptime(rental_duration, "%H:%M").time()
        hours = rental_duration.hour
        minutes = rental_duration.minute
        firsthour = 10
        if hours < 1:
            cost = 10
        else:
            if minutes == 0:
                cost = firsthour+(hours-1)*5
            else:
                cost = firsthour+(hours)*5
        return cost
    cost = calculate_cost(rental_duration)
    rental = [{"Imie:": customer_name, "Czas:": rental_duration, "Koszt:": cost}]
    def save_rental(rental):
        "Saves new record to rentals.json"
        if not os.path.exists(PATH):
            with open(PATH, 'w') as file:
                json.dump(rental, file, indent=4)
        else:
            with open(PATH, 'r+') as file:
                for rental_entry in rental:
                    file.write(json.dumps(rental_entry, indent=4) + "\n")
    save_rental(rental)

rent_bike("Kuba", "1:00")

def load_rentals():
    "Shows up records from rentals.json"
    with open(PATH, 'r') as file:
        rentals = json.load(file)
        print (rentals)

test = int(input())
if test == 1:
    load_rentals()
        

    