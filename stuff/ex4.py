# coding: utf-8
# variable  name

# 100 辆车
cars=100
# 每辆车有4.0 space
space_in_a_car=4.0
# 有30个drivers
drivers=30
# 有90个passengers
passengers=90
# 不能被驾驶的汽车=汽车数-驾驶员
cars_not_driven=cars-drivers
# 能被驾驶的汽车=驾驶员
cars_driven=drivers
# 能载的乘客数=汽车数*每辆车空位数
carpool_capacity=cars_driven*space_in_a_car
# 平均每辆车要载客数=乘客数/能被驾驶的汽车
average_passengers_per_car=passengers/cars_driven

print("Ther are",cars,"cars availabe.")
print("There are only",drivers,"drivers availabel.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")