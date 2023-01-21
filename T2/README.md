# Fse_Trabalho_2 - Forno de Solda

## Aluno
|Matrícula | Aluno |
| -- | -- |
| 18/0103431  |  João Victor Valadão de Brito |

## Objetivo

Este trabalho tem por objetivo a implementação de um sistema (que simula) o controle de um forno para soldagem de placas de circuito impresso (PCBs). No trabalho, o aluno deverá desenvolver o software que efetua o controle de temperatura do forno utilizando dois atuadores para este controle: um resistor de potência de 15 Watts utilizado para aumentar temperatura e; uma ventoinha que puxa o ar externo (temperatura ambiente) para reduzir a temperatura do sistema.

## Componentes do Sistema
O sistema é composto por:

- Ambiente fechado controlado com o resistor de potência e ventoinha;
- 01 Sensor DS18B20 (1-Wire) para a medição da temperatura interna (TI) do sistema;
- 01 Sensor BME280 (I2C) para a medição da temperatura externa (TE);
- 01 Conversor lógico bidirecional (3.3V / 5V);
- 01 Driver de potência para acionamento de duas cargas (L297);
- 01 ESP32;
- 01 Raspberry Pi 4;

**Linguagem**: 
- C<br>

**Bibliotecas**: 

- stdio.h
- stdlib.h
- string.h
- unistd.h
- softPwm.h
- time.h
- wiringPi.h
- fcntl.h  
- termios.h

## Arquitetura do sistema
O projeto em si está dentro da pasta T2 nesse repositório e lá estão os arquivos que são utilizados para a execução do programa que será explicado no tópico seguinte. A arquitetura do projeto foi dividida em pastas para facilitar a compreensão do sistema de modo geral, assim temos as seguintes pastas:

### crc
 - Apresenta os arquivos disponibilizados pelo professor para podermos calcular o CRC, que são importados para dentro da **main.c**.

### PID
 - Apresenta os arquivos disponibilizados pelo professor para podermos utilizar o algoritmo de PID para nos retornar a porcentagem que a ventoinha e o resistor devem ser acionados, que são importados para dentro da **main.c**.

### UART
 - Apresenta as configurações para que possa ser executada a configuração da UART para realizar a comunicação com a ESP32, que são importados para dentro da **main.c**.

### main.c
 - Este é o arquivo central que define o fluxo do sistema e também as configurações da GPIO.

### Makefile
 -  Este é um arquivo que auxília na compilação do código.

## Uso

**Para executar o programa é necessário seguir a ordem das informações a seguir**

Siga as instruções a seguir :

1) Clonar o repositório:
```sh 
git clone https://github.com/joaovaladao/Fse_Trabalhos.git
```

2) Acessar a pasta da aplicação:
```sh
cd .\T2\
```

3) Copie a pasta para a placa rasp inserindo seu user no lugar de <user_>, seu caminho ao inves de <caminho/> e o IP ao inves de <000.00.00.00>:
```
scp -P 13508 -r T2 <user_>@<000.00.00.00>:/home/<user_>
```
exemplo:
```
scp -P 13508 -r T2 joaobrito@164.41.98.16:~
```

4) Acessar via ssh a placa rasp inserindo seu user no lugar de <user_> e o IP ao inves de <000.00.00.00>:
```
ssh <user_>@<000.00.00.00> -p 13508
```
exemplo:
```
ssh joaobrito@164.41.98.16 -p 13508
```

6) Acessar a pasta da aplicação no ssh:
```sh
cd .\T2\
```

7) Compile e Execute:
```sh
make
```

8) Para terminar a execução pressione **CONTROL+C**

## Observações 
Não consegui implementar o I2C para recuperar a temperatura ambiente **ainda...**
