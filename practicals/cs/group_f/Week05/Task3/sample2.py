# Get temperature every two hours from 8am to 6pm
Temperatures = []
Time_of_day = 8

while (Time_of_day - 2) != 18:
    User_input_temperature = int(input(f"Enter temperature at {Time_of_day}:00 : "))
    Temperatures.append(User_input_temperature)
    Time_of_day += 2

#calculate highest lowest and average

lowest_temp = min(Temperatures)
highest_temp = max(Temperatures)
Average_temp = sum(Temperatures) / len(Temperatures)


print(f"Lowest temperature: {lowest_temp} \nHighest temperature: {highest_temp} \nAverage temperature: {Average_temp}")


#COMMENT
#Please follow guidelines on well written code and include
#!/usr/bin/env python3
#if __name__ == '__main__':
#This works - but shows as a 24hr clock. It's again a different why a loop can be writtem
