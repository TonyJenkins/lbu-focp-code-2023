if __name__ == "__main__":
    time = 8
    time2 = "am"
    temperatures = []
    for x in range(6):
        temp = str(input(f"Enter {time}{time2} temp: "))
        if len(temp) == 0:
            print("Enter a temperature")
        else:
            if time == 12:
                time = 0
                time2 = "pm"
            time += 2
            if "C" in temp:
                temperatures.append(int(temp[:-1]))
            else:
                temperatures.append(int(temp))

    print(f"Highest Temp: {max(temperatures)}C")
    print(f"Lowest Temp: {min(temperatures)}C")
    print(f"Average Temp: {round(sum(temperatures) / len(temperatures), 2)}C")


#COMMENT
#missing the reference to which version of python (line 1)
#includes an if check to see if 'C' is present on the inputted string
