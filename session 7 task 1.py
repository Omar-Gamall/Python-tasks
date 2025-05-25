import matplotlib.pyplot as plt


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [15, 17, 16, 18, 20, 19, 22]


plt.plot(days, temperatures)

# Add labels and title
plt.xlabel("Day of the Week")
plt.ylabel("Temperature in celsius")
plt.title("Weekly Temperature Variation")

plt.show()
