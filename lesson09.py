import datetime

current_time = datetime.datetime.now()

day = int(input("Ingrese el día: "))
month = int(input("Ingrese el mes: "))
year = int(input("Ingrese el año: "))

custom_date = datetime.date(year, month, day)
print(custom_date)
print(custom_date.year)
print(custom_date.month)
print(custom_date.day)

weekday = custom_date.weekday()

days = ["Lunes", "Martes"]
days = {
    1: "Lunes",
    2: "Martes",
}
print(days[weekday])
if(weekday == 0):
    print("Lunes")
elif(weekday == 1):
    print("Martes")
print(current_time.strftime("%d/%m/%Y %H:%M:%S"))