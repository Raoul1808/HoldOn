import json
import codecs


def make_hold_dict(tile: int, duration: int = 0, distance_multiplier: int = 100, landing_animation: bool = False):
    return {
        "floor": tile,
        "eventType": "Hold",
        "duration": duration,
        "distanceMultiplier": distance_multiplier,
        "landingAnimation": ("Enabled" if landing_animation else "Disabled")
    }


chart = json.load(codecs.open('main.adofai', 'r', 'utf-8-sig'))

chart_length = len(chart['pathData'])

print(chart_length)

for i in range(chart_length):
    chart["actions"].append(make_hold_dict(i+1))

file = codecs.open('out.adofai', 'w', 'utf-8-sig')
json.dump(chart, file, ensure_ascii=False, indent=4)

print('All Done!')
