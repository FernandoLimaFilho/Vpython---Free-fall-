from vpython import * # Importação do vpython
from time import sleep # Importando o método time.sleep() para trabalhar com o tempo entre mensagens
"""
Criação de uma função para calcular o tempo de queda livre a partir de informações 
fornecidas pelo usuário;
"""
def Tempo_de_queda(y0, v0, t0):
    """
    1º) Criação do solo na forma de uma caixa
    """
    solo = box(pos = vector(0, 0, 0), size = vector (30, 1.5, 30))
    """
    2º) Criação de uma pequena esfera
    sphere(posicão inicial, raio da esfera, cor da esfera)
    Segundo o problema; posição incial = (0 uc, 19.64 uc, 0 uc)
    """
    bola = sphere(pos = vector(0, y0, 0), radius = 1.0, color = color.green)
    """
    3º) Condições iniciais e definições
    """
    g = vector(0, -9.82, 0) # Definição da gravidade
    bola.v = vector(0, v0, 0) # Velcidade inicial da bola
    t = t0 # tempo inicial
    """
    # dt é o intervalo de tempo de registro de informações sobre o movimento do objeto pelo vpython.
    """
    dt = 0.001
    """
    4º) Definindo as equações de movimento...
    """ 
    while bola.pos.y >= 0:
        rate(900) # Velocidade da animação 
        bola.v = bola.v + g*dt # Equação da velocidade da bola
        bola.pos = bola.pos + bola.v*dt # Equação de posição da bola
        t = t + dt # Autalização do tempo
    return(t)   
"""
Informações fornecidas pelo usuário
"""
y0 = float(input("Posição inicial: "))
while y0<0: # Sistema para evitar erros fornecidos pelo usuário
    print("\n\033[1;41mErro: A posição inicial deve ser positiva!\033[m") # \033[1;31m é o código pra fonte vermelha
    sleep(2) # Depois de 2 segundos, faça o que vem abaixo
    y0 = float(input("Posição inicial: "))    
v0 = float(input("Velocidade inicial: "))
while v0<0: # Sistema para evitar erros fornecidos pelo usuário
    print("\n\033[1;41mErro: Velocidade inicial deve ser positiva!\033[m")
    sleep(2) # Depois de 2 segundos, faça o que vem abaixo
    v0 = float(input("Velocidade inicial: "))    
t0 = float(input("Tempo inicial: "))
while t0<0: # Sistema para evitar erros fornecidos pelo usuário
    print("\n\033[1;41mErro: Forneça um tempo inicial positivo!\033[m")
    sleep(2) # Depois de 2 segundos, faça o que vem abaixo
    t0 = float(input("Tempo inicial: "))
"""
Resultado
"""    
sleep(1)
print(f"\n\033[1;33mTempo de queda livre = {Tempo_de_queda(y0, v0, t0)}\033[m")



    

