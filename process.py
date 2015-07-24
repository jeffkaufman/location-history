import json
import pprint

def start(fname):
  happening = []
  with open(fname) as inf:
    d = json.loads(inf.read())
    for location in d["locations"]:
      lat = location["latitudeE7"] / 10000000.0
      lng = location["longitudeE7"] / 10000000.0

      if "activitys" in location:
        for activity in location['activitys']:
          ts = int(activity["timestampMs"]) / 1000.0
          for possibility in activity["activities"]:
            happening.append((ts, lat, lng, possibility["confidence"], possibility["type"]))
  with open("out.csv", 'w') as outf:
    for record in happening:
      outf.write("%.3f, %.6f, %.6f, %d, %s\n" % record)

if __name__ == "__main__":
  #start("sample.json")
  start("LocationHistory.json")
