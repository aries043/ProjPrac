import googlemaps

def getloc(addr):
    gmaps = googlemaps.Client(key='') #Please Enter your googlemaps key.
    geocode_result = gmaps.geocode(addr)
    n_lat = geocode_result[0]['geometry']['location']['lat']
    n_lng = geocode_result[0]['geometry']['location']['lng']
    return n_lat, n_lng
