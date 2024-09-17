#ask the user for the velocity of the object in miles per hour
velocity_Start = int(input('What is your objects starting velocity in mph? '))
velocity_End = int(input('What is your objects final velocity in mph? '))

#ask the user for the amount of time in seconds the object was in motion and put it into hours
time_sec = int(input('What is the time in seconds that the object moved? '))
time_hr= time_sec / 3600

#calculate the displacement using an equation derived from one of the basic kinematic equations
#STORE THE NEW VARIABLE AS total displacement
total_Displacement = (time_hr * (velocity_Start + velocity_End)) / 2

#print the total displacement
print("your total displacement is",total_Displacement,'miles')