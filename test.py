from datetime import datetime

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
    return f"Klient: {customer_name}, Koszt wynajmu: {cost} zł"


wynik = rent_bike("Maciek", "2:50")
print (wynik)
    
