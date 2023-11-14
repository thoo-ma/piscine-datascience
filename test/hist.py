import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = np.random.normal(0, 1, 1000)

# Create histogram
plt.hist(data, bins=range(-4, 5, 1))  # bins from -4 to 4 with step size 1
plt.xticks(range(-4, 5, 1))  # x-axis ticks from -4 to 4 with step size 1

# Set labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')

# Show plot
plt.show()