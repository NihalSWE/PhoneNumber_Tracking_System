
#Phone Number tracking project

import phonenumbers
from phonenumbers import timezone,carrier,geocoder
number=(input("Enter Your Phone Number: "))
phone=phonenumbers.parse(number,"CH")
time=timezone.time_zones_for_number(phone)
sim_details=carrier.name_for_number(phone,"en")
location= geocoder.description_for_number(phone,'en')


print(f"Your Number:{number}\n{phone}\nTime zone:{time}\nSim Details:{sim_details}\nLocation: {location}")
print(f"Your Number:{number} ")
print(f"{phone}")
print(f"Time zone:{time}")
print(f"Sim Details:{sim_details}")
print(f"Location: {location}")