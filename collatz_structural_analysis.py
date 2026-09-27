import math
import matplotlib.pyplot as plt

def analizar_collatz_renato(n_inicial):
    """
    Modelo de Dinámica Estructural de Collatz
    Autor/Conceptualización: Renato Lima Lepretti
    """
    n = n_inicial
    pasos = 0
    
    historial_n = [n]
    historial_masa = [math.log2(n)]
    historial_contacto = []
    historial_v2 = []

    print(f"=== INICIO DE ANÁLISIS ESTRUCTURAL PARA n = {n_inicial} ===")
    
    while n > 1:
        # Representación binaria del entero impar actual
        bin_str = bin(n)[2:]
        longitud_bits = len(bin_str)
        
        # Conteo del patrón de contacto de empuje '11'
        pares_11 = sum(1 for i in range(longitud_bits - 1) if bin_str[i:i+2] == '11')
        densidad_contacto = pares_11 / longitud_bits if longitud_bits > 1 else 0.0
        historial_contacto.append(densidad_contacto)

        if n % 2 == 0:
            n = n // 2
            v2 = 1
        else:
            siguiente_val = 3 * n + 1
            # Cálculo de la valoración 2-ádica v2(3n+1)
            v2 = 0
            temp = siguiente_val
            while temp % 2 == 0:
                v2 += 1
                temp //= 2
            
            n = siguiente_val // (2**v2)
            
        pasos += 1
        historial_v2.append(v2)
        historial_n.append(n)
        historial_masa.append(math.log2(n) if n > 0 else 0)

    print(f"Análisis completado en {pasos} pasos.")
    print(f"Masa máxima alcanzada: {max(historial_masa):.2f} (n = {max(historial_n)})")
    
    return historial_n, historial_masa, historial_contacto, historial_v2

# Ejecución del caso de estudio: Renato Lima Lepretti - Caso n = 27
if __name__ == "__main__":
    n_estudio = 27
    hist_n, hist_masa, hist_contacto, hist_v2 = analizar_collatz_renato(n_estudio)

    # Generación de la gráfica del modelo
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(hist_masa, color='blue', linewidth=1.5, label='Masa $M(n) = \log_2(n)$')
    ax1.axhline(y=math.log2(27), color='gray', linestyle='--', alpha=0.7, label='Masa Inicial (n=27)')
    ax1.set_ylabel('Masa (Bits)')
    ax1.set_title('Modelo de Dinámica Estructural de Collatz — Renato Lima Lepretti\nCaso de Estudio: n = 27 (111 pasos)')
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    ax2.plot(hist_contacto, color='red', alpha=0.6, label='Densidad de Contacto (Patrón 11)')
    ax2.axhline(y=1/3, color='black', linestyle=':', label='Umbral Crítico (33.3%)')
    ax2.set_xlabel('Pasos de la Órbita')
    ax2.set_ylabel('Densidad de Contacto')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    plt.savefig('collatz_renato_lima_27.png')
    plt.show()
