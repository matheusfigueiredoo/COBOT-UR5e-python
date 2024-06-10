# Colaborative Robot (COBOT) ur5e

Este repostiório apresenta um tutorial de como controlar o robô colaborativo ur5e da Universal Robots na linguagem de programação Python. 

O desenvolvimento dos códigos foi feito com base nos exemplos mostrados no site: https://sdurobotics.gitlab.io/ur_rtde/index.html e no sitema operacional Windows 10 Pro x64.

## Setup

Primeiramente, são necessárias algumas configurações na máquina utilizada para executar os comandos de controle do robô.

### 1. Instalação da biblioteca

O robô é controlado com base nas funções da biblioteca _Real-Time Data Exchange (RTDE)_. Dessa forma, esta biblioteca funciona apenas nas versões 3.9 e 3.10 do Python. Então, caso a versão do Python de sua máquina seja diferente destas, será necessário mudar para as versões citadas.

Para instalar a biblioteca, execute o seguinte comando no prompt de comando:

**pip install ur_rtde**

Após a instalação, verificar a versão usando o comando:

**pip show ur_rtde**

### 2. Conexão do robô com a máquina

O robô é controlado remotamente por uma máquina com transporte de comunicação TCP/IP. É fundamental garantir que tanto o robô quanto a máquina estejam conectados na mesma rede.

Após ligar o robô, configure-o pelo PolyScope para controle remoto. Depois, na aba de configurações, certifique-se de que esteja no modo **DHCP** e anote o **endereço de IP** mostrado na tela. Este endereço de ip é necessário para que o script desenvolvido em Python consiga controlar o robô, posteriormente.


## ur_rtde

A biblioteca _ur_rtde_ consiste em três imports fundamentais para controle do braço:

### 1. RTDE Control interface
Usado para mover o robô e funções utilitárias.

### 2. RTDE Receive interface
Usado para receber dados do robô.

### 3. RTDE IO interface
Usado para configurar I/O digitais/analógicas e ajustar o controle deslizante de velocidade do robô.


## Divisão do repositório

