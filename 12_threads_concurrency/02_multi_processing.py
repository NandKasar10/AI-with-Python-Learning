from multiprocessing import Process
import time

def brew_chai(name) :
    print(f"Start of {name} chai served ...!!")
    time.sleep(3)
    print(f"End of {name} chai served ...!!")

if __name__ == "__main__" :
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}",))
        for i in range(0,3)
    ]

#STARTS ALL PROCESS

    for p in chai_makers :
        p.start()

#WAIT FOR ALL TO COMPLETE TO COMBINE THE ACTUAL RESULT

    for p in chai_makers :
        p.join()

    print("All chai served ... !!!")