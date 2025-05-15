import pyautogui
import pyperclip
import webbrowser
import time 

import yfinance

yfinance.Ticker("AAPL").history("6mo")

data = yfinance.Ticker("AAPL").history("6mo")
cierre = data.Close
cierre.plot()

maxima = round(cierre.max(), 2)
minimo = round(cierre.min(), 2)
medio = round(cierre.mean(), 2)

destinatario = input("Diga el correo al que se quiere enviar:")
asunto = "Correo de prueba"
mensaje = f"""
   Hola, estimado, le invito a realizar un chequeo sistemático de lo existente.
   Estoy probando mi sistema automático para envío de correos, me parece increíble.
   
   La cotización máxima de la página de apple en yahoo finance es :USD {maxima}
   La cotización mínima de la página de apple en yahoo finance es :USD {minimo}
   La cotización media de la página de apple en yahoo finance es :USD {medio}
   
    Si te parece bien, hagámoslo bien.
"""
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
time.sleep(3)

pyautogui.click(94,208)
time.sleep(5)

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("tab")
pyperclip.copy(asunto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("tab")
pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=1218, y=959)

pyautogui.hotkey("ctrl", "w")
time.sleep(1)
pyautogui.click(x=1079, y=263)