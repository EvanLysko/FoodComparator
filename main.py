import googlemaps
import json

#TODO the googlemaps library is causing issues when requesting with next_page_token but the links generated work. So fuck the libary and just use your own requests

gmaps = googlemaps.Client(key = "AIzaSyD6XC9bqblOB1b0UdXo88jGUX0qT2Jwd4Q")

page_count = 0
next_page_token = None
location = "pittsburgh, pa"
places = []

while page_count < 5:
    if next_page_token:
        results = gmaps.places(query = "grocery stores " + location, page_token = next_page_token)
    else:
        results = gmaps.places(query = "grocery stores " + location)

        

    #check status
    if results["status"] != "OK":
        print("PLACES REQUEST ERROR")
        continue
    
    next_page_token = results["next_page_token"]
    
    results = results["results"]
    places = places+ results
    page_count += 1
    print(next_page_token)
    

# each place has:
# business_status
# formatted_address
# geometry
# icon
# icon_background_color
# icon_mask_base_uri
# name
# opening_hours
# photos
# place_id
# plus_code
# price_level
# rating
# reference
# types
# user_ratings_total

#we want
# name
# formatted_address
# opening_hours --- this just has if they are open now or not
# photos -- maybe
# price_level - needs error handling, some don't have a price level listed
# rating - 0.0 - 5.0
# user_ratings_total
# types


#get rid of:
# geometry
# business_status
# icon
# icon_background_color
# icon_mask_base_uri
# photos
# place_id
# plus_code
# reference

print(len(places))

def _shouldKeepInList(place):
    """checks if place["business_status"] is OPERATIONAL
    """
    return place["business_status"] == "OPERATIONAL"

#get rid of all non-operational places
places[:] = [tup for tup in places if _shouldKeepInList(tup)]


for place in places:
    try:
        del place["geometry"]
    except:
        pass
    
    try:
        del place["business_status"]
    except:
        pass
    
    try:
        del place["icon"]
    except:
        pass
    
    try:
        del place["icon_background_color"]
    except:
        pass
    
    try:
        del place["icon_mask_base_uri"]
    except:
        pass
    
    try:
        del place["photos"]
    except:
        pass
    
    try:
        del place["plus_code"]
    except:
        pass
    
    try:
        del place["reference"]
    except:
        pass
        


# print(len(places))

# for place in places:
#     for key in place:
#         print(key)
#     break;
    
    
# for place in places["results"]:
    # print(place["name"])
    