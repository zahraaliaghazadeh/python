# Note date now is 9/21/2021 , and the location Seattle WA
# is used to answer the questions

# What is the difference between the highest and the lowest temperature values
#  predicted for the 10 day forecast?

highest = 73
lowest = 55
print("The difference of highest and lowest temp predicted for the 10 day forecast is {}"
.format(highest-lowest))


print("-"*50)
# What is the average temperature at noon predicted for the 10 day
#  forecast?

data1 = [61, 63, 62, 61, 59, 60, 64, 65, 65, 63]
average = sum(data1)/10
print("Average temoerature at noon predicted for the 10 day forecast is: {} F"
.format(average))

print()
print("-"*50)
# What is the highest temperature predicted for the 10 day forecast,
#  converted from Fahrenheit to Celsius?

data2 = [69, 64, 62, 63, 62, 68, 70, 73, 72, 77]
high = max(data2)
high_celcius = (high - 32) * (5/9)
print("The highest temperature predicted for the next 10 days forecast is: {}"
.format(high_celcius))
