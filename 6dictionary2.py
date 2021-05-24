weather = {"city": "Москва", 
"temperature": "20"}
print("country" in weather)
print(weather.get('country', 'Россия'))
weather["date"] = "27.05.2019"
print (len(weather))