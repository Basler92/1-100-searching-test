from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Ścieżka do chromedriver.exe - dostosuj do swojego systemu
driver_path = 'ścieżka/do/chromedriver.exe'

# Inicjalizacja przeglądarki
driver = webdriver.Chrome(executable_path=driver_path)

# Otwarcie strony internetowej
driver.get('https://www.example.com')  # Zastąp URL odpowiednią stroną

# Znajdź pole tekstowe (np. za pomocą XPath) - dostosuj do strony, którą używasz
input_field = driver.find_element("xpath", "//input[@id='nazwa_pola']")  

# Wprowadź liczby od 1 do 100
for number in range(1, 101):
    input_field.send_keys(str(number))
    input_field.send_keys(Keys.RETURN)  # Wciśnij Enter
    time.sleep(1)  # Poczekaj sekundę (opcjonalnie)

# Zamknij przeglądarkę po zakończeniu działania
driver.quit()
