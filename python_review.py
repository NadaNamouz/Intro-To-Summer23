import random

#2
temperatures = []
for i in range(7):
    x = random.randint(26, 41)  
    temperatures.append(x)

#3
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#4
good_days_count = 0
for j in range(len(days_of_the_week)):
    t = temperatures[j]
    if t % 2 == 0:
        good_days_count += 1
        #print(days_of_the_week[j]) 

#5
highest_temp = 0
lowest_temp = 41
highest_temp_day = ""
lowest_temp_day = ""

for k in range(len(temperatures)):
    temp = temperatures[k]  
    if temp > highest_temp:
        highest_temp = temp
        highest_temp_day = days_of_the_week[k]  
    if temp < lowest_temp:
        lowest_temp = temp
        lowest_temp_day = days_of_the_week[k]  

#6
sum=0
for i in range(len(temperatures)):
	sum += temperatures[i]
average = sum/7

#7
above_avg = []
for i in range(len(temperatures)):
    if temperatures[i] > average:
        day = days_of_the_week[i]
        above_avg.append(day)

print("Report")
print("Temperatures of the week")
for i in range(7):
    print(days_of_the_week[i], ":", temperatures[i]) 
print("******************")
print("Shelly had", good_days_count, "days with even temperatures")
print("******************")
print("The hottest temperature was:", highest_temp, "on", highest_temp_day)
print("The lowest temperature was:", lowest_temp, "on", lowest_temp_day)
print("******************")
print("The average temperature was:", average)
print("Days with temperatures above average were:", above_avg)


#bonus
sorted_days = []
sorted_days.append(lowest_temp)
temperatures.remove(lowest_temp)
temperatures.remove(highest_temp)


for i in range(len(temperatures)):
    for j in range(len(temperatures)):
        L = 41
        if temperatures[j]<L:
            L = temperatures[j]
            sorted_days.append(L)
            temperatures.remove(L)
sorted_days.append(highest_temp)
print(sorted_days)

