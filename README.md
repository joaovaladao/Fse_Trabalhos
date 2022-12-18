# Fse_Trabalho_1 - Automated Room

# Gerenciador de Cruzamentos


## Aluno
|Matrícula | Aluno |
| -- | -- |
| 18/0103431  |  João Victor Valadão de Brito |

## Sobre 
Este trabalho tem por objetivo a criação de um sistema distribuído de automação predial para monitoramento e acionamento de sensores e dispositivos de um prédio com múltiplas salas. O sistema deve ser desenvolvido para funcionar em um conjunto de placas Raspberry Pi com um servidor central responsável pelo controle e interface com o usuário e servidores distribuídos para leitura e acionamento dos dispositivos. Dentre os dispositivos envolvidos estão o monitoramento de temperatura e umidade, sensores de presença, sensores de fumaça, sensores de contagem de pessoas, sensores de abertura e fechamento de portas e janelas, acionamento de lâmpadas, aparelhos de ar-condicionado, alarme e aspersores de água em caso de incêndio.

## Componentes do Sistema
Para simplificar a implementação e logística de testes do trabalho, a quantidade de salas do prédio e o número de sensores foi reduzido a um mínimo representativo. Estarão disponíveis para teste 4 placas Raspberry Pi para executar os Servidores Distribuídos e o Servidor Central. A configuração do sistema está detalhada abaixo:
O sistema do Servidor Central será composto por:

- 01 placa Raspberry Pi 4;

O sistema do Servidor Distribuído será composto por:

- 01 Placa Raspberry Pi 4;
- 01 Sensore de Temperatura (DHT22)
- 01 Circuito de potência com 5 relés para acionametno de Lâmpadas / Aparelhos de Ar-Condicionado, etc.;
- 02 Sensores de fechamento de portas/janelas;
- 01 Sensore de presença;
- 01 Sensore de fumaça;
- 02 Sensores de Contagem de Pessoas (Cada pessoa que passa aciona o sinal do sensor por aprox. 200 ms, são 2 sensores por sala);
- 01 Alarme (Buzzer).

**Linguagem**: 
- python (versão 3)<br>

**Bibliotecas**: 
- socket
- RPi.GPIO
- threading
- time <br>

## Arquitetura do sistema
O projeto em si está dentro da pasta Automated_room nesse repositório e lá estão os arquivos que são utilizados para a execução do programa que será explicado no tópico seguinte. A arquitetura do projeto segue o padrão de um sistema TCP/IP, ou seja, voltada a conexão de um servidor central aos seus servidores distribuídos. Assim, conseguimos relacionar os scripts quanto a suas funcionalidades no código

### Servidor Central
**server_test.py**: Esse arquivo é o responsável por inicializar o servidor e fazer todas as requisições aos sistemas distribuídos que o usuário selecionar.

**data_receiver.py**: Esse arquivo é o responsável por formatar os dados que foram disponibilizados pelos servidores distribuídos.

### Servidores Distribuídos
**sala.py**: Esse arquivo é uma classe, onde armazena os atributos presentes em uma sala, como os pinos dos leds e endereços de sensores, assim como uma variável para armazenar o estado desses objetos. Além de pequenas funções para controle dos leds.

**sensores.py**: Esse arquivo armazena as funções que são chamadas pelos callbacks, ou seja, quais atividades devem acontecer quando um sensor é ativado. Também é o responsável pelo calculo da temperatura e umidade da sala a cada 2 segundos.

**client_test.py**: Esse arquivo é o responsável por formatar as mensagens antes de serem enviadas ao servidor central, alem das funções para criar o socket e realizar o envio propriamente.

**listen_server.py**: Esse arquivo é o responsável por verificar quais são as requisições do servidor, e desse modo fazer as manipulações para realizar as tarefas requisitadas.

**menu.py**: Esse arquivo vai apresentar as funcionalidades do menu para cada sistema distribuído no terminal.

### Outros
**global_variables**: Esse arquivo serve apenas para mapear os pinos para a configuração das salas em cada placa Raspberry

## Uso 
**Para executar o programa é necessário seguir a ordem das informações a seguir**

Siga as instruções a seguir :

1) Clonar o repositório:
```sh 
git clone https://github.com/joaovaladao/Fse_Trabalhos.git
```

2) Acessar a pasta da aplicação:
```sh
cd .\T1\Automated_room\
```

3) Copie a pasta para a primeira placa rasp inserindo seu user no lugar de <user_> e o IP ao inves de <000.00.00.00>:
```
scp -P 13508 -r Automated_room <user_>@<000.00.00.00>:~
```
exemplo:
```
scp -P 13508 -r Automated_room joaobrito@164.41.98.16:~
```

4) Copie a pasta para a segunda placa rasp inserindo seu user no lugar de <user_> e o IP ao inves de <000.00.00.00>:
```
scp -P 13508 -r Automated_room <user_>@<000.00.00.00>:~
```
exemplo:
```
scp -P 13508 -r Automated_room joaobrito@164.41.98.26:~
```

5) Abrir **3 terminais** e neles acessar via ssh a primeira placa rasp inserindo seu user no lugar de <user_> e o IP ao inves de <000.00.00.00>, onde 2 terminais podem dividir o ip da mesma placa Raspberry:
```
ssh <user_>@<000.00.00.00> -p 13508
```
exemplo:
 - Terminal 1
```
ssh joaobrito@164.41.98.16 -p 13508
```
 - Terminal 2
```
ssh joaobrito@164.41.98.16 -p 13508
```
 - Terminal 3
```
ssh joaobrito@164.41.98.26 -p 13508
```

6) Subir o servidor em um dos terminais duplicados:<br>

    ```
    cd Automated_room/
    ```
    - Para subir o servidor, então utilizaremos o python e passaremos o IP da placa em que o servidor se encontra

    ```
    python server_test.py 164.41.98.16
    ```

7) Subir as duas salas para comunicarem com o servidor:

    - Para subir a primeira sala vamos passar o ip do servidor e uma flag para identificarmos se a configuração representa os pinos da sala 1 ou da sala 2, ou seja:

    ```
    cd Automated_room/
    ```

    ```
    python main.py <ip_do_server> <config_da_sala>
    ```
    - Exemplo:

    ```
    python main.py 164.41.98.16 1
    ```

    - Para subir a segunda sala repetimos o processo anterior, passando o mesmo ip do servidor e alterando apenas o número da sala:

    ```
    cd Automated_room/
    ```

    ```
    python main.py <ip_do_server> <config_da_sala>
    ```
    - Exemplo:

    ```
    python main.py 164.41.98.16 2
    ```


9) Para terminar a execução pressione **CONTROL+C** duas vezes em cada terminal depois de finalizar conexão com o servidor

## Observações 
Não implentado o log (em arquivo CSV) dos comandos acionados, outro problema no código é que os alarmes só disparam localmente na sala em que o sensor identificou alguma irregularidade.

