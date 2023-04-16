import phonenumbers
from phonenumbers import geocoder, carrier

my_number = "+998995437671"

ch_number= phonenumbers.parse(my_number,"CH")
print(geocoder.description_for_number(ch_number, "en"))
car_number= phonenumbers.parse(my_number, "RO")
print(carrier.name_for_number(car_number,"en"))