import json
from collections import defaultdict

resolution = 10.0**3  # decimals to keep

def start(fname):
  # { (lat, lng) -> { activity -> count } }
  activities = defaultdict(lambda : defaultdict(int))

  with open(fname) as inf:
    for line in inf:
      ts, lat, lng, confidence, activity = line.strip().split(", ")

      lat = int(float(lat) * resolution) / resolution
      lng = int(float(lng) * resolution) / resolution

      activities[lat, lng][activity] += int(confidence)

  cleaned = []
  for (lat, lng), activity_counts in activities.iteritems():
    a = [(count, activity) for (activity, count) in activity_counts.items()]
    a.sort()
    most_common_count, most_common_activity = a[-1]
    cleaned.append([lat, lng, most_common_activity])

  with open("out2.json", "w") as outf:
    outf.write(json.dumps(cleaned))

if __name__ == "__main__":
  start("out.csv")
