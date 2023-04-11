import json
import time
import googleMapsPlacesRequests as gPlaces
import googleMapsGeocodingRequests as gGeocode

# print(places)
    

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


def _shouldKeepInList(place):
    """checks if place["business_status"] is OPERATIONAL
    """
    return place["business_status"] == "OPERATIONAL"


def _getOnlyOperational(places):
    places[:] = [tup for tup in places if _shouldKeepInList(tup)]
    return places


def _getWithoutUselessInfo(places):
    
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
    return places      


def _getWithoutDuplicateNames(places):
    names = []
    res = []
    for place in places:
        if place["name"] not in names:
            names.append(place["name"])
            res.append(place)
        
    return res

def _getLocalGroceryStores():
    zip_code = "15226"
    page_count = 0
    next_page_token = None
    location = "pittsburgh pa"
    radius = "50000";
    places = []

    geocode_results = gGeocode.get(zip_code)

    if geocode_results["status"] != "OK":
        print("GEOCODE REQUEST ERROR: " + geocode_results["status"])
            
            
    latlng = str(geocode_results["results"][0]["geometry"]["location"]["lat"]) + "," + str(geocode_results["results"][0]["geometry"]["location"]["lng"])
    print(latlng)


    while page_count < 2:
        if next_page_token is None:
            results = gPlaces.get("query=" + "grocery stores" + "&location=" + latlng +"&radius=" + radius)
        else:
            results = gPlaces.get("pagetoken=" + next_page_token)

        #check status
        if results["status"] != "OK":
            print("PLACES REQUEST ERROR: " + results["status"])
            break
        
        try:
            next_page_token = results["next_page_token"]
        except:
            next_page_token = None
            
        if next_page_token is None or next_page_token == "":
            page_count = 10000
        
        results = results["results"]
        places = places + results
        page_count += 1
        print(len(places))
        time.sleep(5)

    places = _getWithoutDuplicateNames(places)
    places = _getOnlyOperational(places)
    places = _getWithoutUselessInfo(places)


    for place in places:
        print(place["name"])
        
def _getPopularGroceryStores():
    zip_code = "15226"
    page_count = 0
    next_page_token = None
    radius = "50000";
    places = []

    geocode_results = gGeocode.get(zip_code)

    if geocode_results["status"] != "OK":
        print("GEOCODE REQUEST ERROR: " + geocode_results["status"])
            
            
    latlng = str(geocode_results["results"][0]["geometry"]["location"]["lat"]) + "," + str(geocode_results["results"][0]["geometry"]["location"]["lng"])
    print(latlng)


    

    places = _getWithoutDuplicateNames(places)
    places = _getOnlyOperational(places)
    places = _getWithoutUselessInfo(places)


    for place in places:
        print(place["name"])

_getLocalGroceryStores()

