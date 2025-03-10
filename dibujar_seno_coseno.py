import matplotlib.pyplot as plt
import numpy as np

# Definimos el límite de valores de la gráfica (entre -10 y 10)
x = np.linspace(-10, 10, 400)

# Crear las funciones sen(x) y cos(x)
seno = np.sin(x)
coseno = np.cos(x)

# Definimos el tamaño de la gráfica
plt.figure(figsize = (10, 3))
# Dibujamos el seno (azul) y el coseno (verde)
plt.plot(x, seno, color = "blue", linewidth = 3)  
plt.plot(x, coseno, color = "green", linewidth =3)
# Establecemos el título de la gráfica y de los ejes X e Y 
plt.title("Gráficas del seno y el coseno")
plt.xlabel("x")
plt.ylabel("y")

# Agregamos la leyenda al gráfico (dentro del gráfico, arriba a la derecha)
#plt.legend(["sen(x)", "cos(x)"], loc = "upper right")
# Agregamos la leyenda al gráfico, fuera del gráfico, arriba a la derecha
plt.legend(["sen(x)", "cos(x)"], bbox_to_anchor = (1.1, 1), loc = "upper right",  prop={"size": 7})

# Establecemos el color y grosor de la línea divisora del eje X
plt.axhline(0, color = "gray", lw = 1)
# Establecemos el color y grosor de la línea divisora del eje Y
plt.axvline(0, color = "gray", lw = 1)

# Mostramos las gráficas del seno y el coseno
plt.show()