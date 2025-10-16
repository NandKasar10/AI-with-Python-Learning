#daemon threads are threads which are bg_thread when automatically shuts down when main program exit

import threading
import time

def monitor_tea_temp():
    while True : 
        print(f"Monitoring tea temperature ..!!")
        time.sleep(2)

threading.Thread(target=monitor_tea_temp, daemon=True).start()

print("Main program done ...!!!")
