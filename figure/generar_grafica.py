import os
import matplotlib.pyplot as plt

# 1. Crear la carpeta 'figuras' si no existe
os.makedirs('figuras', exist_ok=True)

# 2. Datos experimentales de PE-U4 (Commit 3711eda, N=4 ejecutores)
transformaciones = [
    'T1\n(Filtrado - Foco)', 
    'T2\n(Agregación)', 
    'T3\n(Join)', 
    'T4\n(Derivada)', 
    'T5\n(Top-N)'
]
speedups = [5.93, 5.30, 4.90, 5.64, 4.56]

# 3. Asignación de colores: T1 en rojo (#d62728) y el resto en azul (#1f77b4)
colores = ['#d62728', '#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4']

# 4. Construcción del gráfico
plt.figure(figsize=(8, 5))
barras = plt.bar(transformaciones, speedups, color=colores, edgecolor='black', linewidth=1.2)

# Línea de aceleración lineal teórica (N=4)
plt.axhline(y=4.0, color='gray', linestyle='--', linewidth=1.5, label='Aceleración Lineal Ideal (N=4)')

# Etiquetas y títulos
plt.ylabel('Speedup experimental ($S = T_{pandas} / T_{spark}$)', fontsize=11, fontweight='bold')
plt.xlabel('Transformación Evaluada', fontsize=11, fontweight='bold')
plt.title('Aceleración Experimental por Transformación ($N=4$ ejecutores)\nFoco Individual: T1 - Filtrado y Selección', fontsize=12, fontweight='bold', pad=15)
plt.ylim(0, 7)
plt.grid(axis='y', linestyle=':', alpha=0.7)

# Anotación de valores exactos encima de cada barra
for barra in barras:
    y = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width() / 2.0, 
        y + 0.15, 
        f'{y:.2f}x', 
        ha='center', 
        va='bottom', 
        fontweight='bold', 
        fontsize=10
    )

plt.legend(loc='upper right', frameon=True)
plt.tight_layout()

# 5. Guardar la imagen a 300 DPI en la carpeta figuras/
ruta_salida = os.path.join('figuras', 'fig_speedup.png')
plt.savefig(ruta_salida, dpi=300, bbox_inches='tight')
plt.close()

print(f"¡Gráfica de T1 generada exitosamente a 300 DPI en: {ruta_salida}!")