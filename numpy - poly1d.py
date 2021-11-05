import numpy as np

# the following constructs the polynomial x² + 2x + 3
p = np.poly1d([1,2,3])
print(np.poly1d(p))

print(p(.5))