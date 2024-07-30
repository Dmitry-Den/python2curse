import requests
import pandas as pd
import json

category = input("Введите категорию заведения для поиска рядом: ")

url = "https://api.foursquare.com/v3/places/search"

client_id = "0BWRGL1TKZ5AC3VFPHIIE02P2RZ53SDBMYNXUQAUF02SR4VD"
client_secret = "ROBLHLNMLTWWSGEGLUG2IUCCCZXQBJRMRK34HP2G1300MUL4"
headers = {"accept": "application/json", "Authorization": "fsq3u1wI+pxkQIwJKTPol9LIxmjCPQPFOt+BqeeAW8J5sOU=", }
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "query": category,

}
response = requests.get(url, params=params, headers=headers)
print(response.text)

if response.status_code == 200:
    print("Успешный запрос")
    data = response.json()  # Directly use .json() method
    venues = data["results"]

    venues_data = []
    for venue in venues:
        name = venue["name"]
        region = venue.get("location", {}).get("region", "Регион не указан")
        locality = venue.get("location", {}).get("locality", "Город не указан")
        address = venue.get("location", {}).get("address", "Адрес не указан")
        rating = venue.get("rating", "-")
        venues_data.append({"Название": name, "Адрес": f'{region}, {locality}, {address}', 'Рейтинг': rating})
    df = pd.DataFrame(venues_data)
    print(df.head)
else:
    print("Запрос не удался", response.status_code)