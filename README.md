# Modelo exploratorio de dinámica binaria en la conjetura de Collatz

**Autor:** Renato Lima Lepretti

Este repositorio contiene un programa para visualizar y explorar trayectorias de la conjetura de Collatz mediante cantidades derivadas de la representación binaria de los enteros. Es un análisis experimental; no presenta una demostración de la conjetura.

## Descripción

Para un entero positivo $n$, definimos la medida logarítmica

$$
M(n)=\log_2(n),
$$

que refleja la magnitud de $n$ en escala de bits. En los estados impares, la transformación de Collatz puede escribirse como

$$
3n+1=2n+n+1.
$$

Esta forma permite observar la suma binaria y los acarreos que produce. El programa también calcula la valoración 2-ádica $v_2(3n+1)$, es decir, el exponente de la mayor potencia de 2 que divide a $3n+1$.

Como descriptor exploratorio, el script cuenta los pares de bits consecutivos 11 en la representación binaria de cada estado y calcula su frecuencia respecto de la longitud binaria. Esta frecuencia se grafica junto con $M(n)$ para facilitar la inspección de una órbita.

## Caso de estudio: $n=27$

Con la regla estándar de Collatz, la trayectoria que comienza en 27 llega a 1 tras 111 pasos y alcanza el máximo 9232. El script reproduce y grafica esta órbita particular. Este ejemplo ilustra el comportamiento de una trayectoria, pero no permite concluir por sí solo que todas las trayectorias convergen.

## Alcance y limitaciones

La frecuencia de pares 11 se incluye como una cantidad que puede estudiarse y compararse entre trayectorias. En esta versión no se demuestra que exista un umbral universal para esa frecuencia, ni que dicho valor determine $v_2(3n+1)$ o garantice una disminución de $M(n)$.

De hecho, para $n=3$, la representación binaria es 11, por lo que la frecuencia de pares 11 es $1/2$, mayor que $1/3$. Sin embargo, $3n+1=10$ y $v_2(10)=1$. Este caso muestra que la frecuencia, tal como está definida aquí, no implica por sí sola que $v_2(3n+1)\ge 2$.

Cualquier relación general entre patrones binarios, acarreos, contracción de la medida y convergencia debe formularse con definiciones y condiciones precisas, y demostrarse por separado. La conjetura de Collatz continúa siendo un problema abierto.

## Requisitos y uso

El script requiere Python y Matplotlib. Desde la carpeta del repositorio, ejecútalo con:

    python collatz_structural_analysis.py

El programa genera una gráfica para el caso $n=27$ y la guarda como collatz_renato_lima_27.png.

## Próximos pasos de investigación

- Comparar la frecuencia de pares 11 y los valores de $v_2(3n+1)$ en un conjunto amplio de estados impares.
- Especificar si la medida de frecuencia debe calcularse sobre todos los estados o solo sobre los impares.
- Formular y probar (o refutar) afirmaciones cuantitativas que relacionen los descriptores binarios con la variación de $M(n)$.
- Separar claramente los resultados experimentales de las proposiciones demostradas.
