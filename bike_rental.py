import json
from datetime import datetime
import smtplib
import os
import re

PATH = "rentals.json"

def rent_bike(customer_name, rental_duration):
    "A function that takes the customer's name and rental time"
    cost = calculate_cost(rental_duration)
    rental = {
            "Imie:": customer_name,
            "Czas:": rental_duration, 
            "Koszt:": cost
            }
    save_rental(rental)
    return rental

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

def save_rental(rental):
    "Saves new record to rentals.json"
    if not os.path.exists(PATH):
        rentals = []
    else:
        with open(PATH, "r") as file:
            rentals = json.load(file)

    rentals.append(rental)

    with open(PATH, "w") as file:
        json.dump(rentals, file, indent=4)

def load_rentals():
    "Loads current rental list"
    if not os.path.exists(PATH):
        print("Brak aktywnych wynajmów.")
        return []
    with open(PATH, "r") as file:
        return json.load(file)

def main():
    print ("""
           1. Wynajem roweru
           2. Obliczanie kosztu wynajmu
           3. Wyświetlanie listy wynajmów
           4. Usuwanie wynajmu z listy
    """)
    choice = int(input())
    while not 1 <= choice <= 4:
        print ("Wybierz opcje od 1 do 4")
        choice = int(input())
    if choice == 1:
        name = str(input("Podaj imie klienta: "))
        while re.search(r'[^a-zA-Z]', name):
            print ("Imie nie może zawierać znaków specjalnych, liczb, oraz spacji")
            name = str(input("Podaj imie klienta: "))
        print (f"Imie klienta: {name}")
        while True:
            time_input = input("Wprowadź godzinę i minutę (format HH:MM): ")
    
            try:
                # Próba sparsowania w formacie godzina:minuta
                parsed_time = datetime.strptime(time_input, "%H:%M")
        
                # Sprawdzanie poprawności godziny i minut
                hours = parsed_time.hour
                minutes = parsed_time.minute
        
                # Sprawdzanie czy godzina i minuta mieszczą się w poprawnym zakresie
                if 0 <= hours < 24 and 0 <= minutes < 60:
                    print(f"Podany czas: {hours:02d}:{minutes:02d}.")
                    break  # Jeśli format jest poprawny, przerywamy pętlę
                else:
                    print("Godzina lub minuta poza zakresem. Spróbuj ponownie.")
    
            except ValueError:
                print("Niepoprawny format. Użyj formatu HH:MM. Spróbuj ponownie.")
        mail = str(input("Podaj adres email (przykład: jankowalski@gmail.com): "))
        rental = rent_bike(name, time_input)
        print (rental)

    if choice == 2:
        while True:
            timetocalculate = input("Wprowadź godzinę i minuty (format HH:MM): ")
    
            try:
                # Próba sparsowania w formacie godzina:minuta
                parsed_time = datetime.strptime(timetocalculate, "%H:%M")
        
                # Sprawdzanie poprawności godziny i minut
                hours = parsed_time.hour
                minutes = parsed_time.minute
        
                # Sprawdzanie czy godzina i minuta mieszczą się w poprawnym zakresie
                if 0 <= hours < 24 and 0 <= minutes < 60:
                    print(f"Podany czas: {hours:02d}:{minutes:02d}.")
                    break  # Jeśli format jest poprawny, przerywamy pętlę
                else:
                    print("Godzina lub minuty poza zakresem. Spróbuj ponownie.")
    
            except ValueError:
                print("Niepoprawny format. Użyj formatu HH:MM. Spróbuj ponownie.")
        calculatedtime = calculate_cost(timetocalculate)
        print (f"Kwota wynajmu za czas {timetocalculate} wynosi: {calculatedtime} zł")

        


main()
        

    