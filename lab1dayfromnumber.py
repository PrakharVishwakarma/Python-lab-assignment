num = int(input("Enter the number to print the name of day : "))  
 
if 0 < num < 8:
        days = {1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
                }
        print("The name of the day is",days[num],".")
else:
    print(("Invalid Input"))
