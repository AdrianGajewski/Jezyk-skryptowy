import datetime

data = input("Podaj datę w formacie rrrr-mm-dd \n")
data = data.split('-')
a = datetime.date(int(data[0]), int(data[1]), int(data[2]))
print(datetime.date.today() - a)