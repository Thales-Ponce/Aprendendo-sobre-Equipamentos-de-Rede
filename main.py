simulacao_rede

---------------------
# main.py
# Simulação de Hub, Switch e Roteador
# Autor: Thales Ponce
# Objetivo: Demonstrar o funcionamento básico de dispositivos de rede

# Lista de dispositivos conectados à rede
dispositivos = ["PC1", "PC2", "PC3", "PC4"]

# -------------------------------
# HUB: envia mensagens para todos os dispositivos
# -------------------------------
def hub(origem, mensagem):
    print(f"\n📡 HUB recebeu de {origem}: '{mensagem}'")
    for d in dispositivos:
        if d != origem:
            print(f"➡️ Enviando para {d} (mesmo sem saber quem é o destino)")

# -------------------------------
# SWITCH: envia mensagens apenas para o dispositivo correto
# -------------------------------
def switch(origem, destino, mensagem):
    print(f"\n🔀 SWITCH recebeu de {origem}: '{mensagem}'")
    if destino in dispositivos:
        print(f"➡️ Enviando apenas para {destino}")
    else:
        print("⚠️ Dispositivo de destino não encontrado na rede")

# -------------------------------
# ROTEADOR: conecta redes diferentes
# -------------------------------
def roteador(origem, destino_rede, mensagem):
    print(f"\n🌐 ROTEADOR recebeu de {origem}: '{mensagem}'")
    print(f"➡️ Encaminhando para a rede {destino_rede} (escolhendo a melhor rota)")

# -------------------------------
# Execução da simulação
# -------------------------------
if __name__ == "__main__":
    print("===== SIMULAÇÃO DE REDE =====")
    
    # Testando Hub
    hub("PC1", "Olá, tudo bem?")
    
    # Testando Switch
    switch("PC1", "PC3", "Olá, tudo bem?")
    
    # Testando Roteador
    roteador("PC1", "Internet", "Acessando um site")
    ---------------------------------------------------------------
    ✅ O que esse código faz:

Hub: envia a mensagem para todos os dispositivos conectados, sem distinguir o destino.

Switch: envia a mensagem apenas para o destino correto, simulando inteligência de rede.

Roteador: encaminha a mensagem de uma rede local para outra (simulado como “Internet”).



