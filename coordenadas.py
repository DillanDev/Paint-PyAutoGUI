import pyautogui
import time
path = "C:/Users/Root/Desktop/coordenadas.txt"

cordxy = ""
lista = ["1"]
        
while True:
    time.sleep(0.5)
    cord_x, cord_y = pyautogui.position()
    cordxy = str(cord_x)+","+str(cord_y)
    file = open(path,'r+')
    file.write("\n")
    file.write("pyautogui.click()")
    file.write("\n")
    file.write("pyautogui.moveTo(")
    file.write(cordxy)
    file.write(")")
    lista = file.readlines()
    print(lista[len(lista)-1])
    

        
        
        
    
        
        
    
    
        
    
