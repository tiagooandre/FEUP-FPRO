def trip_cost(distance, litres_100km, price):
    #distance = float(input("Distance: "))
    #litres_100km = float(input("L/100km: "))
    #price = float(input("Price/L: "))

    travel = (litres_100km * price * distance) / 100

    return round(travel, 2)

print(trip_cost(235, 7, 1.46))