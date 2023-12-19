from geopy.geocoders import Nominatim
from geopy.distance import geodesic

locator = Nominatim(user_agent="GetLo")

location = locator.geocode("Kaikankuppam Valasaravakkam Chennai Tamil Nadu")

print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

Poddatur = (17.3632333,78.9597908)
con = ['Kakinada', 'Chennai', 'Miraj', 'Madurai', 'Coimbatore','Mumbai']

def find_nearest(user, consumers):
    dist=[]
    locator = Nominatim(user_agent="GetLo")
    for i in consumers:
        loca = locator.geocode(i)
        loc=(loca.latitude, loca.longitude)
        dist.append(geodesic(user, loc).km)
    
    nearest = list(zip(consumers, dist))
    nearest.sort(key=lambda x: x[1])
    nearest = nearest[:5]
    return nearest

# print(find_nearest(Poddatur,con))


# Kakinada = (17.1213126,82.18422479792069)
# Jagtial = (18.82135895,78.91506632525903)
# Miraj = (16.85851605,74.71089474233874)


# #the API output has multiple other details as a json like altitude, lattitude, longitude, correct raw addres, etc.
# #printing all the informaton
# # print(location.raw,'\nPoint = ',location.point,'\nLongitude = ',location.longitude,'\nLatitude = ',location.latitude,'\nAltitude = ',location.altitude,'\nAddress = ',location.address)
# print(geodesic(Poddatur, Kakinada).km)
# print(geodesic(Poddatur, Jagtial).km)
# print(geodesic(Poddatur, Miraj).km)
# print(geodesic(Kakinada, Jagtial).km)
# print(geodesic(Kakinada, Miraj).km)
# print(geodesic(Jagtial, Miraj).km)

# consumers = ['A', 'B', 'C', 'D', 'E', 'F']
# dist = [343.95165701372946, 161.45693708451796, 455.6065096785789, 394.07762045758176, 796.3284483016829, 495.7408271557955]
