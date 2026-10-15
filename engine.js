// Auger Math engine - hypothetical arithmetic on labeled norms only.
// No verdicts about what any auger can bite through: soil, roots and rock
// are the rental counter's and the manual's call. Always have utilities
// located before any dig.

function plural(n, one, many) { return n === 1 ? one : many; }

function aAn(n) {
  const s = String(n);
  return (n === 11 || n === 18 || s.startsWith("8")) ? "An" : "A";
}

function fixed1(x) { return (Math.floor(x * 10 + 0.5) / 10).toFixed(1); }

function holeMinutes(holes, seconds) {
  if (!(holes > 0)) throw new Error("the hole count must be above zero");
  if (!(seconds > 0)) throw new Error("the claimed seconds must be above zero");
  return holes * seconds / 60;
}

function holeTruth(holes, seconds) {
  const minutes = holeMinutes(holes, seconds);
  let verdict;
  if (minutes <= 10) verdict = "done before the concrete sets";
  else if (minutes <= 30) verdict = "a working hour";
  else if (minutes <= 90) verdict = "an honest afternoon";
  else verdict = "a two-day rental honestly";
  return `The auger claims ${seconds} seconds a hole; ${holes} ${plural(holes, "hole", "holes")} is ${fixed1(minutes)} minutes of drilling - ${verdict}.`;
}

function buriedFeet(post, above) {
  if (!(post > 0)) throw new Error("the post length must be above zero");
  if (!(above > 0)) throw new Error("the above-ground height must be above zero");
  if (!(above < post)) throw new Error("the above-ground height must be less than the post length");
  return post - above;
}

function depthTruth(post, above) {
  const buried = buriedFeet(post, above);
  const fraction = buried / post;
  let verdict;
  if (fraction >= 1/3) verdict = "the one-third rule holds";
  else if (fraction >= 1/4) verdict = "a quarter buried honestly";
  else verdict = "shallow - check the local frost line";
  return `${aAn(post)} ${post}-foot post standing ${above} ${plural(above, "foot", "feet")} above ground buries ${fixed1(buried)} ${plural(buried === 1 ? 1 : 0, "foot", "feet")} - ${verdict}.`;
}

function holeCubicFeet(diameter, depth) {
  if (!(diameter > 0)) throw new Error("the hole diameter must be above zero");
  if (!(depth > 0)) throw new Error("the depth must be above zero");
  return Math.PI * (diameter / 2) * (diameter / 2) * depth / 1728;
}

function mixTruth(holes, diameter, depth, yield_) {
  if (!(holes > 0)) throw new Error("the hole count must be above zero");
  if (!(yield_ > 0)) throw new Error("the bag yield must be above zero");
  const each = holeCubicFeet(diameter, depth);
  const total = holes * each;
  const bags = Math.ceil(total / yield_);
  let verdict;
  if (bags <= 4) verdict = "a few bags at the truck";
  else if (bags <= 12) verdict = "a cart of bags honestly";
  else if (bags <= 30) verdict = "a stack of bags honestly";
  else verdict = "a pallet honestly";
  return `${holes} ${plural(holes, "hole", "holes")} ${diameter} ${plural(diameter, "inch", "inches")} wide and ${depth} ${plural(depth, "inch", "inches")} deep ${holes === 1 ? "takes" : "take"} about ${fixed1(total)} cubic feet of concrete - about ${bags} ${plural(bags, "bag", "bags")} of ${yield_} cubic feet each, ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { holeMinutes, holeTruth, buriedFeet, depthTruth, holeCubicFeet, mixTruth };
}
