from datetime import datetime
import json

def rent_bike(customer_name, rental_duration):
    "A function that takes the customer's name and rental time"
    def calculate_cost(rental_duration):
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
        path = "rentals.json"
        while not os.path.exists(path):
            with open(path, 'w') as file:
                json.dump(rental, file)
        else:
            with open(path, 'a') as file:
                for rental_entry in rental:
                    file.write(json.dumps(rental_entry) + "\n")
    save_rental(rental)





wynik = rent_bike("Maciek", "2:50")
print (wynik)




    
