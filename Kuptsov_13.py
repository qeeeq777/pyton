import numpy as np
import matplotlib.pyplot as plt
import os
n = 1000 
A = 10
x = np.linspace(-5.12, 5.12, 1000) # создание "отрезка"
fx =((np.sin(A*np.pi*x))/(2*x))+((x-1)**(4))
# построение графика функции
fig, ax = plt.subplots()
ax.plot(x, fx)
ax.set_xlim(-5.12, 5.12);
ax.set_ylim(-10, 80);
ax.grid(linewidth = 2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x, fx, color = 'blue')
plt.show()
# создание файла
try:
 os.mkdir('results')
except OSError:
 pass
complete_file = os.path.join('results', 'task_01_307B_Kuptsov_13.txt')
f = open(complete_file, 'w')
# текстовый файл с таблицей
f.write('   x    f(x)\n')
for i in range(n):
 f.write(str("%.4f" % x[i])+' '+str("%.4f" % fx[i])+"\n")
f.close()
