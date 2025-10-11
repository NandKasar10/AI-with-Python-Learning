device_status = input("State the status of the device (active/unactive) : ").lower()
temp = int(input("State the Temperature in Celsius : "))

if device_status == "active" :

    if temp > 35 :
        print(f"High temperature alert! : {temp}")

    else : 
        print(f"Temperature is normal : {temp}")

elif device_status == "unactive" :
    print("Device is offline. Please activate the device to check temperature !")

else :
    print("Please state whether the system is active or not !")

