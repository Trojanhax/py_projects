import requests
import json
city = str(input(' enter your city:--'))
url = f"http://api.weatherapi.com/v1/current.json?key=b8432efc443f4f09a7a171832231810&q={city}"
r = requests.get(url)
wd = json.loads(r.text)
print("name:               ", wd["location"] ["name"])
print("region:             ", wd["location"] ["region"])
print("lat:                ", wd["location"] ["lat"])
print("lon:                ", wd["location"] ["lon"])
print("lon:                ", wd["location"] ["lon"])
print("tz_id:              ", wd["location"] ["tz_id"])
print("localtime_epoch:    ", wd["location"] ["localtime_epoch"])
# print("localtime:          ", wd["location"] ["localtime])

print('last_updated_epoch: ', wd["current"] ["last_updated_epoch"])
print("last_updated:       " ,wd["current"] ["last_updated"])
print("temp_c:             " ,wd["current"] ["temp_c"])
print("temp_f:             ", wd["current"] ["temp_f"])
print("is_day:             ", wd["current"] ["is_day"])
