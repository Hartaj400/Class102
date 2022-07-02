import pyautogui
import charge


start_time = charge.time()


def main():
    while(True):
        if((charge.time() - start_time) >= 60*60):  
            print(start_time)
            pyautogui.alert("Charge Your Laptop")

main()    