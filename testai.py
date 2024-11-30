from datetime import datetime

# Pobranie godziny i minuty od użytkownika w formacie HH:MM
wejscie = input("Podaj czas w formacie godzina:minuta (HH:MM): ")

try:
    # Konwersja wprowadzonego czasu na obiekt datetime.time
    czas = datetime.strptime(wejscie, "%H:%M").time()
    print(f"Wprowadzony czas: {czas}")
except ValueError:
    print("Niepoprawny format. Użyj formatu HH:MM (np. 14:30).")