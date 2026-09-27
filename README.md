# collatz-structural-model
Modelo de Dinámica Estructural y Propagación de Acarreos por Renato Lima # Modelo de Dinámica Estructural y Propagación de Acarreos en la Conjetura de Collatz

**Autor:** Renato Lima Lepretti  
**Marco Teórico:** Dinámica $2$-ádica, Espondilolistesis de Bits y Pozos de Atracción de Masa  

---

## Resumen Ejecutivo

Este repositorio presenta un modelo analítico y geométrico desarrollado por **Renato Lima Lepretti** para estudiar la dinámica de la conjetura de Collatz ($3n+1$) mediante la transformación de masa en representación binaria y la propagación de acarreos (*carries*).

El modelo reinterpreta la operación de Collatz a través de una analogía de mecánica estructural (fricción entre bloques y espondilolistesis binaria), demostrando cómo el crecimiento de la masa $M(n) = \log_2(n)$ fuerza al sistema hacia un pozo de atracción gravitacional.

---

## Principios del Modelo

### 1. Métrica de Masa ($M(n)$)
Para cualquier entero positivo $n$, la masa o complejidad del estado se define en el espacio de información como:
$$M(n) = \log_2(n)$$

### 2. Mecanismo de Acarreo y Espondilolistesis Binaria
La transformación sobre impares $3n + 1$ equivale a $(2n + n) + 1$, representada como la superposición de un vector de bits desplazado sobre sí mismo. 

El modelo de **Renato Lima Lepretti** establece que la estabilidad de la trayectoria depende del grado de contacto entre bloques de bits adyacentes (`11`):
* **Umbral Crítico ($\rho_c = 33.3\%$):** Basado en la periodicidad $2$-ádica límite de $1/3 = 0.010101\dots_2$.
* **Mecanismo de Colapso:** Cuando la densidad de contacto supera el $33.3\%$, se generan acarreos en cadena que incrementan la valoración $2$-ádica $v_2(3n+1) \ge 2$, forzando una contracción neta de la masa ($\Delta M < 0$).

---

## Caso de Estudio: $n = 27$

El script adjunto `collatz_structural_analysis.py` analiza la trayectoria del número $27$, el cual requiere exactamente **111 pasos** para alcanzar el atractor $1$, alcanzando un pico de masa de $M(9232) \approx 13.17$ bits antes de desplomarse por el pozo de atracción.

---

## Uso del Código

```bash
python collatz_structural_analysis.py

