'''

nest_dict = {
            "key1": [List],
            "key2": {Dict}
            }

'''

capitals = {
    "India": "New Delhi",
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Stuttgart","Berlin"],
}

# Retrieve "Lille" from the above dictionary.
print(travel_log["France"][1])

nested_list = ["A", 'B', ["C", "D"]]

# Print the letter D from the nested list.
print(nested_list[2][1])

travel_log_dict = {
    "France": {
        "total_visits": 12,
        "cities_visited":["Paris","Lille","Dijon"]
    },
    "Germany": {
         "total_visits": 5,
         "cities_visited": ["Berlin","Hamburg","Stuttgart"]
    },
}

# Print "Stuttgart" from the travel_log_dict
print(travel_log_dict["Germany"]["cities_visited"][2])