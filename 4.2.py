print("witch fanction you want a or b or c")
x = input()
if x == "a":

    print("Insert a word or sentence to chack if it \"Filndrom\"")
    word = input()
    if word[0] == word[-1]:
        print("YES it is a \"Filndrom\"")
    else:
        print("no it is not a \"Filndrom\"")

elif x == 'b':

    print("Insert the temperature you would like to convert:")
    degree = input()
    if degree[-1::] == 'c' and 'C' and 'f' and 'F':

        if degree[-1::] == 'c' and 'C':
            degree = float(degree[: -1:]) * 1.8 + 32
            print(str(degree) + 'F')
        elif degree[-1::] == 'f' and 'F':
            degree = (float(degree[: -1:]) - 32) / 1.79
            print(str(degree) + 'C')
    else:
        print("You need to put a degree with the letter c or f")

elif x == 'c':
    print("Insert the date in clander and we see what day is it")
    print("weekday(year, month, day)")
    year = int(input('year'))
    month = int(input('month'))
    day = int(input('day'))
    wday = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    import calendar
    dayx = calendar.weekday(year, month, day)
    print(wday[dayx])
else: "enter a or b or c"