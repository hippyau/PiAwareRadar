from urllib.request import urlopen
import json
from time import sleep

DUMP1090DATAURL = "http://192.168.1.166:8080/data/aircraft.json"

class FlightData():
    def __init__(self, data_url = DUMP1090DATAURL):

        self.data_url = data_url

        self.refresh()

    def refresh(self):
        #open the data url
        self.req = urlopen(self.data_url)

        #read data from the url
        self.raw_data = self.req.read()

        #encode the data
        encoding = self.req.headers.get_content_charset()

        #load in the json
        self.json_data = json.loads(self.raw_data.decode())

        self.aircraft = AirCraftData.parse_flightdata_json(self.json_data)

    def _refresh(self):

        data_file = open("aircraft.json")
        
        #load in the json
        self.json_data = json.load(data_file)

        self.aircraft = AirCraftData.parse_flightdata_json(self.json_data)

class AirCraftData():
    def __init__(self,
                 dhex,
                 squawk,
                 flight,
                 lat,
                 lon,
                 validposition,
                 altitude,
                 vert_rate,
                 track,
                 validtrack,
                 speed,
                 messages,
                 seen,
                 mlat):
        
        self.hex = dhex
        self.squawk = squawk
        self.flight = flight
        self.lat = lat
        self.lon = lon
        self.validposition = validposition
        self.altitude = altitude
        self.vert_rate = vert_rate
        self.track = track
        self.validtrack = validtrack
        self.speed = speed
        self.messages = messages
        self.seen = seen
        self.mlat = mlat

    @staticmethod
    def parse_flightdata_json(json_data):
        aircraft_list = []
        for aircraft in json_data['aircraft']:

            if not (aircraft.get("hex") is None):
                ahex = aircraft["hex"]
            else:
                ahex = "0000"

            if not (aircraft.get("squawk") is None):
                asquawk = aircraft["squawk"]
            else:
                asquawk = ""

            if not (aircraft.get("flight") is None):
                aflight = aircraft["flight"]
            else:
                if (asquawk != ""):
                    aflight = asquawk
                else:
                    aflight = "???"

            if not (aircraft.get("lat") is None):
                alat = aircraft["lat"]
            else:
                alat = ""

            if not (aircraft.get("lon") is None):
                alon = aircraft["lon"]
            else:
                alon = ""

            if not (aircraft.get("validposition") is None):
                avp = aircraft["validposition"]
            else:
                if ((alat != "") & (alon != "")):
                    avp = 1
                else: avp = 0

            if not (aircraft.get("alt_baro") is None):
                alt = aircraft["alt_baro"]
            else:
                alt = "0"

            if not (aircraft.get("baro_rate") is None):
                altr = aircraft["baro_rate"]
            else:
                altr = "0"

            if not (aircraft.get("track") is None):
                atrack = aircraft["track"]
                atrackv = 1
            else:
                atrack = "0"
                atrackv = 0

            if not (aircraft.get("ias") is None):
                aias = aircraft["ias"]
            else:
                aias = "0"

            if not (aircraft.get("messages") is None):
                amsg = aircraft["messages"]
            else:
                amsg = "0"

            if not (aircraft.get("seen") is None):
                aseen = aircraft["seen"]
            else:
                aseen = "0"

            if not (aircraft.get("mlat") is None):
                amlat = aircraft["mlat"]
            else:
                amlat = "0"

            aircraftdata = AirCraftData(
                ahex,
                asquawk,
                aflight,
                alat,
                alon,
                avp,                
                alt,
                altr,
                atrack,
                atrackv,                
                aias,
                amsg,
                aseen,
                amlat)

            aircraft_list.append(aircraftdata)
        return aircraft_list

    def __hash__(self):
        return hash(self.hex)

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return (self.hex == other.hex)
            
#test    
if __name__ == "__main__":
    
    #create FlightData object
    myflights = FlightData()
    while True:
        #loop through each aircraft found
        for aircraft in myflights.aircraft:
            
            #print the aircraft's data
            print(aircraft.hex)
            print(aircraft.squawk)
            print(aircraft.flight)
            print(aircraft.lat)
            print(aircraft.lon)
            print(aircraft.validposition)
            print(aircraft.altitude)
            print(aircraft.vert_rate)
            print(aircraft.track)
            print(aircraft.validtrack)
            print(aircraft.speed)
            print(aircraft.messages)
            print(aircraft.seen)
            print(aircraft.mlat)

        sleep(1)

        #refresh the flight data
        myflights.refresh()

