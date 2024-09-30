import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definição das condições básicas
bmax = 1  # Normalize bmax em 1
freq = 60  # 60 Hz
w = 2 * np.pi * freq  # Velocidade angular (rad/s)

# Inicialmente, determine os três campos magnéticos componentes
t = np.linspace(0, 1/freq, 600)  # Um ciclo completo com resolução de 600 pontos
Baa = np.sin(w * t) * (np.cos(0) + np.sin(0) * 1j)
Bbb = np.sin(w * t - 2 * np.pi / 3) * (np.cos(2 * np.pi / 3) + np.sin(2 * np.pi / 3) * 1j)
Bcc = np.sin(w * t + 2 * np.pi / 3) * (np.cos(-2 * np.pi / 3) + np.sin(-2 * np.pi / 3) * 1j)

# Cálculo de B líquida (Bnet)
Bnet = Baa + Bbb + Bcc

# Cálculo de um círculo que representa o valor máximo esperado de B líquida (Bnet)
circle = 1.5 * (np.cos(w * t) + np.sin(w * t) * 1j)

# Criando a figura
fig, ax = plt.subplots(figsize=(8, 6), dpi=80)
ax.plot(circle.real, circle.imag, color="purple", label="Circulo", linewidth=2.0)

# Configurações do gráfico
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# Desenhando o vetor girante (inicialmente parado no primeiro frame)
quiver = ax.quiver(0, 0, Bnet.real[0], Bnet.imag[0], units='xy', angles='xy', scale=1)

# Função de animação que atualiza o vetor girante
def update(frame):
    quiver.set_UVC(Bnet.real[frame], Bnet.imag[frame])  # Atualizando o vetor
    return quiver,

# Criando a animação
anim = FuncAnimation(fig, update, frames=len(t), interval=30, blit=True)

# Mostrando o gráfico animado
plt.title("Gráfico Campo Girante", fontsize=17)
plt.xlabel("Eixo X", fontsize=15)
plt.ylabel("Eixo Y", fontsize=15)
plt.legend(loc="upper left")
plt.show()