height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

base = len(height) - 1
if height[0] < height[-1]: altura = height[0]
else: altura = height[-1] 

benchmark = base * altura
print("base: ", base)
print ("altura :", altura)
print ("superficie: ", benchmark)


lateral_izq = max(height[0], height[1])
lateral_dcho = max(height[-2], height[-1])

# if height[1] > height[0]: lateral_izq = height[1]
# else: lateral_izq = height[0]

print (lateral_izq)

# if height[-2] > height[-1]: lateral_dcho = height[-2]
# else: lateral_dcho = height[-1]
print (lateral_dcho)