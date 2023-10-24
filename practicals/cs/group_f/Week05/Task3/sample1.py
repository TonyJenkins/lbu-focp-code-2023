if __name__ == '__main__':

    print("Disclaimer, when entering temps ensure it is like this: 11C")

    time = 8

    am_pm = "am"

    temps = []

    for x in range(6):

        if time == 12:
            am_pm = "pm"

        if time > 12:
            time = 2

        temp = input(f"Enter {time}{am_pm} temp: ")

        temps.append(int(temp[:-1]))

        time += 2

    print(f"Highest Temp: {max(temps)}C")
    print(f"Lowest Temp: {min(temps)}C")
    print(f"Average Temp: {round(sum(temps) / len(temps),1)}C")


#COMMENTS
#This works :-)
#Shows loops and how you iterate through values can be done in several ways. This is a little more complicated than needed to be
