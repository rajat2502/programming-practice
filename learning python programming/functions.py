#physics force mass project

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

def get_force(mass, acceleration):
  return mass*acceleration

def get_energy(mass, c = 3*10**8):
  return mass*c*c

def get_work(mass, acceleration, distance):
  f = get_force(mass, acceleration)
  return distance*f

f100_in_celsius = f_to_c(1000)
c0_in_fahrenheit = c_to_f(0)
train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

bomb_energy = get_energy(1, 3*10**8)

print("A 1kg bomb supplies " + str(bomb_energy) +" Joules.")

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) +" Joules of work over " + str(train_distance) +" meters.")

#multiple return statements
def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit,high_limit
low, high = get_boundaries(100, 20)
