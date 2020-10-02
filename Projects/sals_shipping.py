def cost_of_ground(weight):
  if (weight <= 2):
    cost = 1.50
  elif (weight <= 6 ):
    cost = 3.00
  elif (weight <= 10):
    cost = 4.00
  else:
    cost = 4.75

  return 20 + (cost * weight)

print(cost_of_ground(8.4))

shipping_cost_prem = 125.00

def cost_of_drone(weight):
  if (weight <= 2):
    cost = 4.50
  elif (weight <= 6 ):
    cost = 9.00
  elif (weight <= 10):
    cost = 12.00
  else:
    cost = 14.25

  return cost * weight

print(cost_of_drone(1.5))

def print_cheapest(weight):

  ground = cost_of_ground(weight)
  drone = shipping_cost_prem
  premium = cost_of_drone(weight)

  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone

  print("The cheapest option available is $%.2f with %s shipping"
  % (cost, method)
  )

print_cheapest(4.8)
print_cheapest(41.5)
