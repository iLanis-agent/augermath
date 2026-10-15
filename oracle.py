import math, json

def plural(n, one, many):
    return one if n == 1 else many

def a_an(n):
    s = str(n)
    return "An" if (n == 11 or n == 18 or s.startswith("8")) else "A"

def fixed1(x):
    return f"{math.floor(x * 10 + 0.5) / 10:.1f}"

def hole_minutes(holes, seconds):
    if not (holes > 0):
        raise ValueError("the hole count must be above zero")
    if not (seconds > 0):
        raise ValueError("the claimed seconds must be above zero")
    return holes * seconds / 60

def hole_truth(holes, seconds):
    minutes = hole_minutes(holes, seconds)
    if minutes <= 10:
        verdict = "done before the concrete sets"
    elif minutes <= 30:
        verdict = "a working hour"
    elif minutes <= 90:
        verdict = "an honest afternoon"
    else:
        verdict = "a two-day rental honestly"
    return f"The auger claims {seconds} seconds a hole; {holes} {plural(holes, 'hole', 'holes')} is {fixed1(minutes)} minutes of drilling - {verdict}."

def buried_feet(post, above):
    if not (post > 0):
        raise ValueError("the post length must be above zero")
    if not (above > 0):
        raise ValueError("the above-ground height must be above zero")
    if not (above < post):
        raise ValueError("the above-ground height must be less than the post length")
    return post - above

def depth_truth(post, above):
    buried = buried_feet(post, above)
    fraction = buried / post
    if fraction >= 1/3:
        verdict = "the one-third rule holds"
    elif fraction >= 1/4:
        verdict = "a quarter buried honestly"
    else:
        verdict = "shallow - check the local frost line"
    return f"{a_an(post)} {post}-foot post standing {above} {plural(above, 'foot', 'feet')} above ground buries {fixed1(buried)} {plural(1 if buried == 1 else 0, 'foot', 'feet')} - {verdict}."

def hole_cubic_feet(diameter, depth):
    if not (diameter > 0):
        raise ValueError("the hole diameter must be above zero")
    if not (depth > 0):
        raise ValueError("the depth must be above zero")
    return math.pi * (diameter / 2) * (diameter / 2) * depth / 1728

def mix_truth(holes, diameter, depth, bag_yield):
    if not (holes > 0):
        raise ValueError("the hole count must be above zero")
    if not (bag_yield > 0):
        raise ValueError("the bag yield must be above zero")
    each = hole_cubic_feet(diameter, depth)
    total = holes * each
    bags = math.ceil(total / bag_yield)
    if bags <= 4:
        verdict = "a few bags at the truck"
    elif bags <= 12:
        verdict = "a cart of bags honestly"
    elif bags <= 30:
        verdict = "a stack of bags honestly"
    else:
        verdict = "a pallet honestly"
    return f"{holes} {plural(holes, 'hole', 'holes')} {diameter} {plural(diameter, 'inch', 'inches')} wide and {depth} {plural(depth, 'inch', 'inches')} deep {'takes' if holes == 1 else 'take'} about {fixed1(total)} cubic feet of concrete - about {bags} {plural(bags, 'bag', 'bags')} of {bag_yield} cubic feet each, {verdict}."

FNS = {"holeTruth": hole_truth, "depthTruth": depth_truth, "mixTruth": mix_truth}

cases = [
 {"fn":"holeTruth","args":[12,30]},
 {"fn":"holeTruth","args":[1,45]},
 {"fn":"holeTruth","args":[20,60]},
 {"fn":"holeTruth","args":[40,90]},
 {"fn":"holeTruth","args":[80,90]},
 {"fn":"holeTruth","args":[10,59]},
 {"fn":"holeTruth","args":[0,30]},
 {"fn":"holeTruth","args":[12,0]},
 {"fn":"depthTruth","args":[8,4]},
 {"fn":"depthTruth","args":[6,4]},
 {"fn":"depthTruth","args":[10,7]},
 {"fn":"depthTruth","args":[8,5]},
 {"fn":"depthTruth","args":[4,3]},
 {"fn":"depthTruth","args":[0,4]},
 {"fn":"depthTruth","args":[8,0]},
 {"fn":"depthTruth","args":[8,8]},
 {"fn":"depthTruth","args":[8,9]},
 {"fn":"mixTruth","args":[12,10,36,0.6]},
 {"fn":"mixTruth","args":[1,8,24,0.6]},
 {"fn":"mixTruth","args":[6,10,36,0.6]},
 {"fn":"mixTruth","args":[15,10,36,0.6]},
 {"fn":"mixTruth","args":[40,12,36,0.6]},
 {"fn":"mixTruth","args":[12,10,36,0.45]},
 {"fn":"mixTruth","args":[3,6,18,0.6]},
 {"fn":"mixTruth","args":[0,10,36,0.6]},
 {"fn":"mixTruth","args":[12,0,36,0.6]},
 {"fn":"mixTruth","args":[12,10,0,0.6]},
 {"fn":"mixTruth","args":[12,10,36,0]}
]

out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
