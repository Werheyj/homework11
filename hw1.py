import numpy as np
import matplotlib.pyplot as plt


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

z = np.zeros(3)
print(z)

b = a.reshape(1, 9)
print(b)
b = a.reshape(9, 1)
print(b)


fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(a[0], label='1')
ax.plot(a[1], label='2')
ax.plot(a[2], label='3')
ax.set_xlabel('ось х')
ax.set_ylabel('ось у')
ax.set_title('Пример')
ax.legend()
plt.show()
