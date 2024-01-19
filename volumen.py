 # cilinder volume
import math
from datetime import datetime
dia = datetime.now().strftime("%y-%m-%d")
l = float(input("l? "))
r = float(input("r? "))
v = math.pi * r**2 * l
with open("v.txt", "at") as file:
  file.write(f"day {dia},large {l}, radius {r},volume {v:.2f}\n")
  print(f"el volumen es {v:.2f}")