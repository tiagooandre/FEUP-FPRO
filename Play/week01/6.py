import math
angle = int(input("Angle: "))*math.pi/180  # convert to radians
cos_angle = math.cos(angle)*18
sin_angle = math.sin(angle)*18

alcance = ((cos_angle*2*sin_angle)/(-10))
alcance = round(alcance)

print(alcance)