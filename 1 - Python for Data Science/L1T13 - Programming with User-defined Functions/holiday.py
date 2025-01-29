def hotel_cost(num_nights):
    # Assuming that the hotel cost is R800 per night
    return num_nights * 800

def plane_cost(city_flight):
    if city_flight == 1:
        return 750
    elif city_flight == 2:
        return 850
    elif city_flight == 3:
        return 600
    else:
        print('You have selected an invalid city code.')
        return 0

def car_rental(rental_days):
    # Assume the car rental cost is R450 per day
    return rental_days * 450

def holiday_cost(num_nights, city_flight, rental_days):
    hotel_cost_total = hotel_cost(num_nights)
    plane_cost_total = plane_cost(city_flight)
    car_rental_total = car_rental(rental_days)
    return hotel_cost_total + plane_cost_total + car_rental_total

if __name__ == "__main__":
    city_options = {
        1: "O.R. Tambo International",
        2: "Capetown International",
        3: "King Shaka International"
    }

    print("Welcome to the Holiday Cost Calculator!\n")

    city_flight = int(input("Enter the city code for your destination:\n1. O.R. Tambo International\n2. Capetown International\n3. King Shaka International\n"))

    num_nights = int(input("\nHow many nights will you be staying? "))
    rental_days = int(input("How many days will you need a car for? "))

    total_cost = holiday_cost(num_nights, city_flight, rental_days)

    if total_cost > 0:
        print("\nHere are the details of your holiday:")
        print(f"Destination: {city_options.get(city_flight)}")
        print(f"Number of Nights: {num_nights}")
        print(f"Number of Rental Days: {rental_days}")
        print(f"Hotel Cost: R{hotel_cost(num_nights)}")
        print(f"Plane Cost: R{plane_cost(city_flight)}")
        print(f"Car Rental Cost: R{car_rental(rental_days)}")
        print(f"Total Holiday Cost: R{total_cost}")
