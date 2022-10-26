import os
from ssl import ALERT_DESCRIPTION_INSUFFICIENT_SECURITY
from dotenv import load_dotenv
from arcgis.gis import GIS

class Config(object):
    load_dotenv()

    PORTAL_URL = os.environ.get('PORTAL_URL')
    PORTAL_USER = os.environ.get("PORTAL_USER")
    PORTAL_PASSWORD = os.environ.get("PORTAL_PASSWORD")
    
    HUB_URL = os.environ.get('HUB_URL')
    AGO_URL = os.environ.get('AGO_URL')
    AGO_USER = os.environ.get("AGO_USER")
    AGO_PASSWORD = os.environ.get("AGO_PASSWORD")
    
    SERVER_URL = os.environ.get('SERVER_URL')

    ARCGIS_ID = os.environ.get("ARCGIS_ID")
    ARCGIS_SECRET = os.environ.get("ARCGIS_SECRET")

def get_token():
    # Get the ip address of my computer
    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname) 

    url = Config.PORTAL_URL + '/sharing/rest/generateToken'
    payload = {'username': Config.PORTAL_USER, 'password': Config.PORTAL_PASSWORD,
           'client':'ip', 'ip':ip_address, 'f': 'json'}
#    payload = {'username': Config.PORTAL_USER, 'password': Config.PORTAL_PASSWORD,
#           'client':'referer', 'referer":refererurl, 'f': 'json'}
    # default lifespan is 60 minutes
    r = requests.post(url, payload)
    j=json.loads(r.text)
    return j['token']


def get_pro_token():
    import arcpy
    portalUrl = arcpy.GetActivePortalURL()
    j = arcpy.GetSigninToken()
    return j['token']


if __name__ == "__main__":
    import requests
    import json

    assert(Config.PORTAL_URL)
    assert(Config.PORTAL_USER)
    assert(Config.PORTAL_PASSWORD)

    assert(Config.HUB_URL)

    assert(Config.AGO_URL)
    assert(Config.AGO_USER)
    assert(Config.AGO_PASSWORD)

    assert(Config.SERVER_URL)

    # Test connection to ArcGIS Online
    gis = GIS(Config.AGO_URL, Config.AGO_USER, Config.AGO_PASSWORD)
    print("Logged in as", gis.properties["user"]["fullName"], 'to', gis.properties['name'])

    # Test connection to ArcGIS Hub, whatever that is. This fails
    #hub = GIS(Config.HUB_URL, Config.AGO_USER, Config.AGO_PASSWORD)
    #print("Logged in as", gis.properties["user"]["fullName"], 'to', gis.properties['name'])

    # Test a connection via normal auth
    #gis = GIS(Config.PORTAL_URL, Config.PORTAL_USER, Config.PORTAL_PASSWORD)
    #print(gis)

    # Test a connection via a Pro token
    token = get_pro_token()
    gis = GIS(Config.AGO_URL, api_key=token, verify_cert=False)
    print("Logged in as", gis.properties["user"]["fullName"])

    # Test a connection via a token
# Whelp, this is wrong
#    token = get_token()
#    gis = GIS(token=token, referer=Config.PORTAL_URL, verify_cert=False)
#    print(gis.properties)

    q = '*'
    list_of_maps = gis.content.search(
        q, item_type='web map', outside_org=False, max_items=5000)
    print("Maps found %d" % len(list_of_maps))

#    d = os.environ
#    for k in d:
#        print("%s : %s" % (k, d[k]))
#    print("PYTHONPATH=", os.environ.get("PYTHONPATH"))
