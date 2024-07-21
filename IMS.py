''' Please make sure you have matplotlib installed before running the code below'''

import numpy as np
import matplotlib.pyplot as plt

# Define the number of neurons in each region
n_neurons_prefrontal = 100
n_neurons_anterior_cingulate = 100
n_neurons_orbitofrontal = 100

# Define the neural activity as random values initially
activity_prefrontal = np.random.rand(n_neurons_prefrontal)
activity_anterior_cingulate = np.random.rand(n_neurons_anterior_cingulate)
activity_orbitofrontal = np.random.rand(n_neurons_orbitofrontal)

# Define a function to simulate the effect of an emotion on neural activity
def simulate_emotion(emotion):
    global activity_prefrontal, activity_anterior_cingulate, activity_orbitofrontal
    
    if emotion == "happiness":
        activity_prefrontal *= np.random.uniform(1.1, 1.5, n_neurons_prefrontal)
        activity_anterior_cingulate *= np.random.uniform(1.1, 1.5, n_neurons_anterior_cingulate)
        activity_orbitofrontal *= np.random.uniform(1.1, 1.5, n_neurons_orbitofrontal)
    elif emotion == "sadness":
        activity_prefrontal *= np.random.uniform(0.5, 0.9, n_neurons_prefrontal)
        activity_anterior_cingulate *= np.random.uniform(0.5, 0.9, n_neurons_anterior_cingulate)
        activity_orbitofrontal *= np.random.uniform(0.5, 0.9, n_neurons_orbitofrontal)
    elif emotion == "anger":
        activity_prefrontal *= np.random.uniform(0.8, 1.2, n_neurons_prefrontal)
        activity_anterior_cingulate *= np.random.uniform(1.3, 1.7, n_neurons_anterior_cingulate)
        activity_orbitofrontal *= np.random.uniform(1.1, 1.5, n_neurons_orbitofrontal)
    else:
        print("Unknown emotion")
    
    # Clip the activity values to be within [0, 1]
    activity_prefrontal = np.clip(activity_prefrontal, 0, 1)
    activity_anterior_cingulate = np.clip(activity_anterior_cingulate, 0, 1)
    activity_orbitofrontal = np.clip(activity_orbitofrontal, 0, 1)

# Simulate the effect of sadness
simulate_emotion("sadness")

# Plot the neural activity
plt.figure(figsize=(15, 5))

# Plot for Prefrontal Cortex Activity
plt.subplot(1, 3, 1)
plt.title("Prefrontal Cortex Activity")
plt.plot(activity_prefrontal, 'o')
plt.ylim(0, 1)

# Plot for Anterior Cingulate Cortex Activity
plt.subplot(1, 3, 2)
plt.title("Anterior Cingulate Cortex Activity")
plt.plot(activity_anterior_cingulate, 'o')
plt.ylim(0, 1)

# Plot for Orbitofrontal Cortex Activity
plt.subplot(1, 3, 3)
plt.title("Orbitofrontal Cortex Activity")
plt.plot(activity_orbitofrontal, 'o')
plt.ylim(0, 1)

# Show the plots
plt.show()