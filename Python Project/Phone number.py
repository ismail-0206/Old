import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number=input("Enter Your Number:\n")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")



print(number)
print(phone)
print(time)
print(car)
print(reg)