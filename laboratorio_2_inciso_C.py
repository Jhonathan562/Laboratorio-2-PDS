import wfdb
import matplotlib.pyplot as plt
import numpy as np


EMG = "Datos_EMG/emg_neuropathy"

lecturasignal = wfdb.rdrecord(EMG)
signal = lecturasignal.p_signal[:,0]  
fs = lecturasignal.fs  
numero_datos = len(signal) 
muestreo=int(5*fs)
time = [i / fs for i in range(numero_datos)]  
signal = signal[:muestreo]
time = time[:muestreo]

plt.figure(figsize=(12,4))
plt.plot(time, signal, color="red")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mv)")
plt.title("Señal EMG neuropatia")
plt.legend()
plt.grid()
plt.show()

suma=0
for i in range(len(signal)):
    suma += signal[i]
media = suma/ len(signal)
print(f"Media de la señal: {media:.4f}")

longitud_vector = 0
for _ in signal:
    longitud_vector +=1
print(f"Longitud del vector: {longitud_vector}")

desviacion = 0
for i in range(len(signal)):
    desviacion += (signal[i] - media) ** 2
desviacion_estandar = (desviacion/len(signal)) ** 0.5
print(f"Desviación estándar: {desviacion_estandar:.4f}")

coeficiente_de_variacion = desviacion_estandar/ media if media != 0 else float ('nan')
print(f"Coeficiente de variación: {coeficiente_de_variacion:.4f}")

def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 1:
        mediana = datos_ordenados[n // 2]  
    else:
        mediana = (datos_ordenados[n // 2 - 1] + datos_ordenados[n // 2]) / 2  # Promedio de los dos centrales
    return mediana

mediana = calcular_mediana(signal)
print(f"La mediana es : {mediana:.4f}")

mediana_librerias = np.median(signal)
media_librerias = np.mean(signal)
longitud_vector_librerias = len(signal)
desviacion_librerias = np.std(signal)
coeficiente_variacion_librerias = desviacion_librerias / media_librerias if media_librerias != 0 else np.nan

print(f"Media de la señal con librerias: {media_librerias:.4f}")
print(f"Longitud del vector con librerias: {longitud_vector_librerias}")
print(f"Desviación estándar con librerias: {desviacion_librerias:.4f}")
print(f"Coeficiente de variación con librerias: {coeficiente_variacion_librerias:.4f}")
print(f"La mediana con librerias es: {mediana_librerias:.4f}")


t = np.linspace(0, 1, fs, endpoint=False) 
N = len(t)

frequencies = np.fft.fftfreq(N, 1/fs)
spectrum = np.fft.fft(signal) / N
magnitude = 2 * np.abs(spectrum[:N//2]) 


plt.figure(figsize=(12,4))
plt.plot(frequencies[:N//2], magnitude, 'orange')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Espectro de la señal normalizado')
plt.grid()
plt.show()

psd = (magnitude ** 2) / N

plt.figure(figsize=(12,4))
plt.plot(frequencies[:N//2], psd, 'violet')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad Espectral')
plt.title('Espectro de la señal de Densidad Espectral')
plt.grid()
plt.show()



suma=0
for i in range(len(magnitude)):
    suma += magnitude[i]
media = suma/ len(magnitude)
print(f"Media de la señal en cuanto a la frecuencia: {media:.4f}")

desviacion = 0
for i in range(len(magnitude)):
    desviacion += (magnitude[i] - media) ** 2
desviacion_estandar = (desviacion/len(signal)) ** 0.5
print(f"Desviación estándar en cuanto a la frecuencia: {desviacion_estandar:.4f}")

mediana = calcular_mediana(magnitude)
print(f"La mediana en cuanto a la frecuencia: {mediana:.4f}")


mediana_librerias = np.median(magnitude)
media_librerias = np.mean(magnitude)
desviacion_librerias = np.std(magnitude)

print(f"Media de la señal con librerias en cuanto a la frecuencia: {media_librerias:.4f}")
print(f"Desviación estándar con librerias en cuanto a la frecuencia: {desviacion_librerias:.4f}")
print(f"La mediana en cuanto a la frecuencia : {mediana_librerias:.4f}")

plt.figure(figsize=(8, 4))
plt.hist(magnitude, bins=50, color='orange', alpha=0.7, edgecolor='black', density=True)
plt.xlabel("Magnitud")
plt.ylabel("Frecuencia (Hz)")
plt.title("Histograma de la Frecuencia (5s)")
plt.grid()
plt.show()


plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(signal, label="Signal Biomedical EMG neuropathy", color="red")
plt.title("Signal Biomedical EMG neuropath")
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(magnitude[:muestreo//2], label="Signal at transformation a Fourier", color="orange")
plt.title("Signal at transformation a Fourier")
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(psd[:muestreo//2], label="Signal Density Espectral a Potencial", color="violet")
plt.title("Signal Density Espectral a Potencial")
plt.legend()

plt.tight_layout()
plt.show()


