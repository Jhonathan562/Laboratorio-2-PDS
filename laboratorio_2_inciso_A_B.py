import numpy as np
import matplotlib.pyplot as plt

#Inciso o punto 8 (a)
# Datos de Jhonathan
# Se define h[n] y x[n] 
h = np.array([5,6,0,0,7,4,7]) # codigo estudiantil Jhonathan
x = np.array([1,0,1,3,1,0,5,4,6,1]) # cedula ciudadana Jhonathan

# Graficar h[n] Jhonathan
t = np.arange(len(h)) 
plt.figure(figsize=(8, 4))
plt.stem(t, h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('h[n] Jhonathan')
plt.grid()
plt.show()

# Graficar x[n] Jhonathan
t = np.arange(len(x))
plt.figure(figsize=(8, 4))
plt.stem(t, x)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[n] Jhonathan')
plt.grid()
plt.show()

y = np.convolve(x, h, mode='full') #Calcular la convolucion entre h[n] y x[n]
print("Señal de la convolucion entre h[n] y x[n] osea y[n] de Jhonathan:", y) #Imprimir el resultado de la convolucion

# Graficar la convolución o y[n] Jhonathan
t = np.arange(len(y))
plt.figure(figsize=(8, 4))
plt.stem(t, y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Convolución de h[n] y x[n] Jhonathan')
plt.grid()
plt.show()


# Datos de Jose
# Se define h[n] y x[n] 
h = np.array([5,6,0,0,6,8,3]) # codigo estudiantil Jose
x = np.array([1,0,2,7,1,5,0,7,2,5]) # cedula ciudadana Jose

# Graficar h[n] Jose
t = np.arange(len(h)) 
plt.figure(figsize=(8, 4))
plt.stem(t, h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('h[n] Jose')
plt.grid()
plt.show()

# Graficar x[n] Jose
t = np.arange(len(x))
plt.figure(figsize=(8, 4))
plt.stem(t, x)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[n] Jose')
plt.grid()
plt.show()

y = np.convolve(x, h, mode='full') #Calcular la convolucion entre h[n] y x[n]
print("Señal de la convolucion entre h[n] y x[n] osea y[n] de Jose:", y) #Imprimir el resultado de la convolucion

# Graficar la convolución o y[n] Jose
t = np.arange(len(y))
plt.figure(figsize=(8, 4))
plt.stem(t, y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Convolución de h[n] y x[n] Jose')
plt.grid()
plt.show()



# Inciso o punto 8(b)
Ts = 1.25e-3  #𝑇𝑠 = 1.25𝑚s
n = np.arange(9) # 𝑝𝑎𝑟𝑎 0 ≤ 𝑛 < 9 
f = 100  # 100𝑛𝑇s
x1 = np.cos(2 * np.pi * f * n * Ts) #𝑥1[𝑛𝑇𝑠] = cos(2𝜋100𝑛𝑇𝑠)
x2 = np.sin(2 * np.pi * f * n * Ts) #𝑥2[𝑛𝑇𝑠] = sin(2𝜋100𝑛𝑇𝑠)
correlacion = np.correlate(x1, x2, mode='full') # Correlacione entre ambas señales
print("Correlación cruzada osea el vector o resultado", correlacion)

# Graficar Correlacion entre ambas señales
t_corr = np.arange(-len(n) + 1, len(n))
plt.figure(figsize=(8, 4))
plt.stem(t_corr, correlacion)
plt.xlabel('Desplazamiento')
plt.ylabel('Correlación')
plt.title('Correlación cruzada entre x1[n] y x2[n]')
plt.grid()
plt.show()



