if __name__ == '__main__':
    temperatures = []
    times = ["8am", "10am", "12am", "2pm", "4pm", "6pm"]
    total = 0

    for s in range(len(times)):
        current_temp = input(f"Enter {times[s]} temp: ")
        current_temp = int(current_temp[:-1])
        total += current_temp
        temperatures.append(current_temp)

    # For Testing print(temperatures)
    num_of_temperatures = len(temperatures)

    highest_temp = max(temperatures)
    lowest_temp = min(temperatures)
    average_temp = total / num_of_temperatures

    print(f"Highest Temp: {highest_temp}C")
    print(f"Lowest Temp: {lowest_temp}C")
    print(f"Average Temp: {average_temp}C")

#COMMENT
#the for loop - this could directly traverse the list 'times', for s in times
