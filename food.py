RESTAURANTS = [
    ("Mango Rice", 4.2, 25),
    ("Pad Thai House", 4.8, 40),
    ("Chicken Rice", 4.6, 15),
    ("Som Tam Corner", 4.6, 25),
    ("Boat Noodles", 4.8, 30),
]


def by_rating(restaurant):
    return (-restaurant[1], restaurant[2])


def by_time(restaurant):
    return (restaurant[2], -restaurant[1])

choice = input("Sort by (rating/time): ").strip().lower()

if choice == "rating":
    sorted_restaurants = sorted(RESTAURANTS, key=by_rating)
elif choice == "time":
    sorted_restaurants = sorted(RESTAURANTS, key=by_time)
else:
    print("Unknown option")
    sorted_restaurants = []

for number, restaurant in enumerate(sorted_restaurants, start=1):
    name, rating, minutes = restaurant
    print(f"{number}. {name}, {rating} stars, {minutes} min")
