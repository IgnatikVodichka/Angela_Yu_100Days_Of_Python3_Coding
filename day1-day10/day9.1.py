capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France":
    {"cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12, },

    "Germany":
    {"cities_visited": ["Berlin", "Hmaburg", "Stuttgart"],
     "total_visits": 11, },
}


'''
Nesting dictionaries inside a list:
'''

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
