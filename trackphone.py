import phonenumbers
from phonenumbers import geocoder, carrier, timezone

num = phonenumbers.parse("+919889225514")

print("Location:", geocoder.description_for_number(num, "en"))  # Region
print("Carrier:", carrier.name_for_number(num, "en"))  # Airtel, Jio etc.
print("Time Zone:", timezone.time_zones_for_number(num))


#output syntax        /home/khushiii/Workspace/.venv/bin/python /home/khushiii/Workspace/Python/trackphone.py
# to undo this        rm -rf ~/Workspace/.venv
