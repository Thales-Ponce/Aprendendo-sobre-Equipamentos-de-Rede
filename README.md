# Aprendendo-sobre-Equipamentos-de-Rede
Nos meus estudos em redes de computadores, estou entendendo a importância de três dispositivos fundamentais:
# 🖧 Simulação de Hub, Switch e Roteador em Python

Este projeto foi desenvolvido como forma de estudo prático em **Redes de Computadores**.  
O objetivo é demonstrar, de maneira simples, como funcionam três dispositivos fundamentais em uma rede: **Hub, Switch e Roteador**.

---

## 🔹 Conceitos abordados

### 📡 Hub
- Dispositivo mais simples.  
- Ao receber uma mensagem, **envia para todos os dispositivos** conectados, sem verificar quem é o destinatário.  
- Isso gera **tráfego desnecessário** e pode deixar a rede lenta.  

### 🔀 Switch
- Dispositivo mais inteligente que o hub.  
- Analisa os **endereços MAC** para descobrir quem deve receber os dados.  
- Envia a mensagem **somente para o destino correto**.  
- Isso torna a rede **mais rápida e segura**.  

### 🌐 Roteador
- Responsável por **conectar redes diferentes** (exemplo: sua rede local com a internet).  
- Trabalha com **endereços IP** para escolher o **melhor caminho (rota)** para os pacotes de dados.  
- Pode oferecer funções de segurança, como **firewall e NAT**.  

---

## 🚀 Como funciona a simulação

Neste projeto, cada dispositivo foi representado em funções Python:  

- `hub()` → envia mensagens para todos.  
- `switch()` → envia somente para o destino correto.  
- `roteador()` → conecta a rede local a uma rede externa (exemplo: Internet).  

### 📌 Exemplo de execução
```bash
python main.py
