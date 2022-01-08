

travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12,
     },

    {"country": "Germany",
     "cities_visited": ["Berlin", "Hmaburg", "Stuttgart"],
     "total_visits": 11,
     }
]


def add_new_country(country, total_visits, cities):
    travel_log.append(
        {"country": country,
         "cities_visited": cities,
         "total_visits": total_visits})


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)


'''
Another method
'''


def add_new_country(country, total_visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = cities
    new_country["total_visits"] = total_visits
    travel_log.append(new_country)


print(travel_log)
