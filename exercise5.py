import matplotlib.pyplot as plt
from exercise1and2 import read_nominees

nominees = read_nominees()

years = []
role_len = []
for n in nominees:
    years.append(int(n.year))
    role_len.append(len(n.role))

plt.plot(years,role_len, 'ro')
plt.show()

