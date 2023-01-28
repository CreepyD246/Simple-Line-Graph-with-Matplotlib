# Importing matplotlib library for plotting graph
from matplotlib import pyplot as plt

# Girls who rejected me
girls_me = [8, 11, 13, 10, 17, 15, 9, 10, 6, 14, 19, 17]
girls_friend = [16, 12, 11, 14, 15, 11, 8, 7, 6, 7, 8, 6]

yticks = [6, 8, 10, 12, 14, 16, 18, 20]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Axis data
x_axis = months
y_axis = girls_me

# Creating figure to plot data on
plt.figure(figsize=(8, 6)) # w and h of graph in inches
axis = plt.subplot(1, 1, 1) # Adds axes to our current figure, but we can also use this to retrieve
                            # a currently existing axes, we do this because ....

# Plotting data on graph
plt.plot(x_axis, y_axis, color="red", marker="o", linestyle="--")
plt.plot(x_axis, girls_friend, color="green", marker="o", linestyle="--")
axis.set_yticks(yticks)

# Defining and adding graph titles to indicate data
plt.legend(["Me", "Friend"])
plt.xlabel("Months")
plt.ylabel("Girls who rejected us")
plt.title("Amount of Girls That Rejected us in 2022")

# Saving figure
plt.savefig("C:\\Users\\denis\\Desktop\\graph.png")

# Showing Figure
plt.show()