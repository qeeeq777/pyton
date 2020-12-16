from scipy.special import spherical_jn as jn
from scipy.special import spherical_yn as yn 
import matplotlib.pyplot as plt
import urllib.request as url #используется для открытия URL
from numpy import pi 
from re import split #расщепление
import numpy as np
import os
# для ЭПР
def hn(l, z):
 return jn(l, z) + 1j * yn(l, z)
def an(l, z):
 return jn(l, z) / hn(l, z)
def bn(l, z):
 return (z * jn(l - 1, z) - l * jn(l, z)) \
 / (z * hn(l - 1, z) - l * hn(l, z))
# вывод исходных данных
URL = 'https://jenyay.net/uploads/Student/Modelling/task_02.txt'
file = url.urlopen(URL)
list = file.readlines()
my_string = list[12].decode("utf-8") # счёт идёт от 0
values = split("[=\r;]", my_string) # вывод нужных значений
D = float(values[1])
fmin = float(values[3])
fmax = float(values[5])
Z = 1000 # кол-во точек 
r = 0.5 * D
f = np.linspace(fmin, fmax, Z) # исходные данные для дальнейшего расчёта
L = 3e8 / f
k = 2 * pi / L
Sum_arr = [((-1) ** n) * (n + 0.5) * (an(n, k * r) - bn(n, k * r)) \
 for n in range(1, 50)]
Sum = np.sum(Sum_arr, axis=0) # суммирование элементов
Sig = (L ** 2) / pi * (np.abs(Sum) ** 2) # ЭПР
plt.plot(f/0.01e11, Sig) #график
plt.xlabel('$f, ГГц$')
plt.ylabel('$\sigma, м^2$')
plt.grid()
plt.show()
#создаём путь
try:
 os.mkdir('results')
except OSError:
 pass
complete_file = os.path.join('results', 'task_02_307B_Kuptsov_13.txt')
# преобразуем nparray в list, для вывода в файл
ftl = f.tolist() 
Stl = Sig.tolist()
f = open(complete_file, 'w')
f.write('    f         Sigma\n')
#расчёт значений
for i in range(Z):
 f.write(str("%.3f" % ftl[i])+' '+str("%.9f" % Stl[i])+"\n")
f.close()

