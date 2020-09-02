import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Initial Setup ------------------------------------------
PAUSE = 0.5 # Pause inbetween refreshes (Seconds)
radiation = pd.read_json("input.json")

plt.ion() #Interactive on

# Absolute axis
ax = plt.gca()
ax.ticklabel_format(useOffset=False)

# Labels
title = plt.title("Rover Radiation Graph")
plt.xlabel("Latitude")
plt.ylabel("Longitude")

# Create Plot
plt.scatter("lat", "long", c='b', data=radiation)
plt.colorbar()
plt.draw()
plt.pause(PAUSE)

# Main Loop ----------------------------------------------
while True:
    # Pretty much Same as initial setup
    # Except this loop doesn't add color bar
    radiation = pd.read_json("input.json")

    ax = plt.gca()
    ax.ticklabel_format(useOffset=False)

    title = plt.title("Rover Radiation Graph")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")

    plt.scatter("lat", "long", c='b', data=radiation)
    plt.draw()
    plt.pause(PAUSE)
    

print("Ok")


