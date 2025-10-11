seat_type = input("Enter the seat type (sleeper/AC/general/luxury) : ").lower()

match seat_type :
    case "sleeper" :
        print("Sleeper seat is confirmed")
    case "ac" :
        print("AC seat is confirmed")
    case "general" :
        print("General seat is confirmed")
    case "luxury" :
        print("Luxury seat is confirmed")
    case _:
        print("Invalid seat type. PLease check the input !")