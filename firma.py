from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Indica el camino hacia tu chromedriver
service = Service('C:/Users/Usuario/Documents/chromedriver-win64/chromedriver.exe')

# Inicia el navegador con el service
driver = webdriver.Chrome(service=service)

# A partir de aquí puedes continuar con tu código...



# Abrimos la página de inicio de sesión
driver.get('http://10.78.11.218/dominio/')

# Localizamos los campos de usuario y contraseña
usuario_input = driver.find_element(By.NAME, 'username')  # Cambia 'usuario' por el nombre real del input
password_input = driver.find_element(By.NAME, 'current_password')  # Cambia 'password' por el nombre real del input
password2_input = driver.find_element(By.NAME, 'new_password')  # Cambia 'password' por el nombre real del input

# Ingresamos las credenciales
usuario_input.send_keys('molina')
password_input.send_keys('molina_gay ')
password2_input.send_keys('molina_gatooooooo ')

# Opcional: Resolver el CAPTCHA (esto lo manejaremos después)
# driver.find_element(By.NAME, 'captcha').send_keys('texto_del_captcha')

# Hacemos click en el botón de inicio de sesión
login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]') # Cambia 'login' por el nombre real del botón
login_button.click()

# Esperamos un tiempo para que cargue la página
time.sleep(3)

# Una vez autenticado, buscamos el botón de "Firmar Entrada/Salida"
firmar_button = driver.find_element(By.ID, 'boton_firmar')  # Cambia 'boton_firmar' por el id correcto
firmar_button.click()

# Cerramos el navegador
time.sleep(2)
driver.quit()
