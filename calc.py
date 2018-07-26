start_bar = int(input("Start pressure?: "))
end_bar = int(input("End pressure?: "))
bar = start_bar-end_bar
bottom_time = int(input("Bottom time (in min)?: "))

msw = float(input("Average depth?: "))

pressure = (msw*0.099376) + 1

sac = bar/bottom_time/pressure

print("SAC: " + str(sac) + " units/min")

service_pressure = int(input("Tank service pressure?: "))
tank_capacity = int(input("Tank capacity?: "))
rmv = (tank_capacity/service_pressure)*sac

print("RMV: " + str(rmv) + " units/min")
