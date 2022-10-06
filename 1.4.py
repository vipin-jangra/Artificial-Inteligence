import matplotlib.pyplot as plt
#1
x = [1,2,3,4,5,6,7,8]
y= [60,62,61,58,56,57,46,63]
plt.xlabel("Days")
plt.ylabel("Speed")
plt.plot(x,y)
plt.show()

#2 
plt.plot(x,y,color='green', linestyle='dashed', marker='+', markerfacecolor='blue', markersize=12)

#3 
days=[1,2,3,4,5,6,7,8]
max_speed=[80,91,92,88,77,79,76,75]
min_speed=[42,43,40,42,33,36,34,35]
avg_speed=[46,58,57,56,40,42,41,36]
plt.xlabel("Days")
plt.ylabel("Speeds")
plt.plot(days,max_speed,label="max_speed")
plt.plot(days,min_speed,label="min_speed")
plt.plot(days,avg_speed,label="avg_speed")
plt.grid(color='r', linestyle='-', linewidth=1)
plt.legend()
plt.title("title")
plt.show()