# taking this concept to its limit, you can nest a dictionary inside another dictionary
# for example if you have several users for a website, you can add their username as the keys
# then store info about the user in a dictionary associated with this username

users = {
    "mwooley": {
       "first": "martin",
       "last": "wooley",
       "location": "sheffield"
    },
    "dtucker":{
        "first": "daruis",
        "last": "tucker",
        "location": "hull"
    }
}

for username, user_info in users.items():
    print("\n" + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())