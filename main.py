
---

## 📄 **main.py** (código principal)

```python
# Simulação de Hub, Switch e Roteador em Python

# Lista de dispositivos conectados à rede
dispositivos = ["PC1", "PC2", "PC3", "PC4"]

# -------------------------------
# HUB: envia para todos os dispositivos
# -------------------------------
def hub(origem, destino, mensagem):
    print(f"\n📡 HUB recebeu de {origem}: '{mensagem}'")
    for d in dispositivos:
        if d != origem:
            print(f"➡️ Enviando para {d} (mesmo sem saber quem é o destino)")


# -------------------------------
# SWITCH: envia apenas para o destino correto
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
# Testes de simulação
# -------------------------------
if __name__ == "__main__":
    hub("PC1", "PC3", "Olá, tudo bem?")
    switch("PC1", "PC3", "Olá, tudo bem?")
    roteador("PC1", "Internet", "Acessando um site")

---------------------------------------------------------------------------------------
# Saída esperada:
Java

📡 HUB recebeu de PC1: 'Olá, tudo bem?'
➡️ Enviando para PC2 (mesmo sem saber quem é o destino)
➡️ Enviando para PC3 (mesmo sem saber quem é o destino)
➡️ Enviando para PC4 (mesmo sem saber quem é o destino)

🔀 SWITCH recebeu de PC1: 'Olá, tudo bem?'
➡️ Enviando apenas para PC3

🌐 ROTEADOR recebeu de PC1: 'Acessando um site'
➡️ Encaminhando para a rede Internet (escolhendo a melhor rota)
---------------------------------------------------------------------------------------------------------
🎯 Objetivo do projeto

Este projeto foi criado para:

Fixar conceitos básicos de redes.

Demonstrar a diferença entre Hub, Switch e Roteador.

Colocar em prática um aprendizado teórico usando Python.
