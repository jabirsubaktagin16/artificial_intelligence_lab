def seriessum(number,interval,first):
    if(number==0):
        return 0
    elif (number>=1):
        return seriessum(number-1, interval, first)+first+(number-1)*interval

#Main
number=int(input('Enter number of terms: '))
interval=int(input('Enter the interval: '))
first=int(input('Enter the first element: '))
result=seriessum(number,interval,first)
print('The sum of the series is: ',result)
