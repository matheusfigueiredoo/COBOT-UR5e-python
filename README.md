# Colaborative Robot (COBOT) ur5e

Este repostiório apresenta um tutorial de como controlar o robô colaborativo ur5e da Universal Robots na linguagem de programação Python. 

O desenvolvimento dos códigos foi feito com base nos exemplos mostrados no site: https://sdurobotics.gitlab.io/ur_rtde/index.html


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

Após ligar o robô, configure 
