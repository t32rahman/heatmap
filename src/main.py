import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Initial Setup
radiation = pd.read_json("input.json")

plt.ion()

ax = plt.gca()
ax.ticklabel_format(useOffset=False)

title = plt.title("Rover Radiation Graph")

plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.scatter("lat", "long", c='b', data=radiation)
plt.colorbar()
plt.draw()
plt.pause(0.5)


while True:
    radiation = pd.read_json("input.json")
    ax = plt.gca()
    ax.ticklabel_format(useOffset=False)
    title = plt.title("Rover Radiation Graph")

    plt.xlabel("Latitude")
    plt.ylabel("Longitude")

    plt.scatter("lat", "long", c='b', data=radiation)
    plt.draw()
    plt.pause(0.5)
    

print("Ok")
# plt.draw()

