#include <stdio.h>
#include <string.h>
#include <unistd.h>  //Used for UART
#include <fcntl.h>   //Used for UART
#include <termios.h> //Used for UART

#include "../crc/crc16.h"

int uart0_filestream = -1;

void init_uart(){
    uart0_filestream = open("/dev/serial0", O_RDWR | O_NOCTTY | O_NDELAY); // Open in non blocking read/write mode
    if (uart0_filestream == -1){
        printf("Erro - Não foi possível iniciar a UART.\n");
    }
    else{
        printf("UART inicializada!\n");
    }
    struct termios options;
    tcgetattr(uart0_filestream, &options);
    options.c_cflag = B9600 | CS8 | CLOCAL | CREAD; //<Set baud rate
    options.c_iflag = IGNPAR;
    options.c_oflag = 0;
    options.c_lflag = 0;
    tcflush(uart0_filestream, TCIFLUSH);
    tcsetattr(uart0_filestream, TCSANOW, &options);
}

void close_uart(){
    printf("UART finalizada!\n");
    close(uart0_filestream);
}

int checkCrc(char conteudoRecebido[]){
    short crc = calcula_CRC(conteudoRecebido, 7);

    if ((crc & 0xFF) == conteudoRecebido[7] && ((crc >> 8) & 0xFF) == conteudoRecebido[8])
        return 1;

    return 0;
}

float requestFloat(char cmd[]){

    unsigned char tx_buffer[20];
    unsigned char *p_tx_buffer;

    p_tx_buffer = &tx_buffer[0];
    *p_tx_buffer++ = cmd[0];
    *p_tx_buffer++ = cmd[1];
    *p_tx_buffer++ = cmd[2];
    *p_tx_buffer++ = cmd[3];
    *p_tx_buffer++ = cmd[4];
    *p_tx_buffer++ = cmd[5];
    *p_tx_buffer++ = cmd[6];

    short crc = calcula_CRC(&tx_buffer[0], (p_tx_buffer - &tx_buffer[0]));
    *p_tx_buffer++ = crc & 0xFF;
    *p_tx_buffer++ = (crc >> 8) & 0xFF;

    //printf("Buffers de memória criados!\n");

    if (uart0_filestream != -1){
        //printf("Escrevendo caracteres na UART ...");
        int count = write(uart0_filestream, &tx_buffer[0], (p_tx_buffer - &tx_buffer[0]));
        if (count < 0){
            return 0;
            printf("UART TX error\n");
        }
    }

    if (uart0_filestream != -1){
        unsigned char rx_buffer[9];
        int rx_length = read(uart0_filestream, &rx_buffer, 9); // Filestream, buffer to store in, number of bytes to read (max)

        int tentativa = 0;

        for (tentativa = 0; tentativa < 5; tentativa++){

            if (checkCrc(rx_buffer)){
                break;
            }
            else{
                requestFloat(cmd);
            }
        }
        printf(".");

        usleep(700000);

        if (tentativa == 5 || rx_length <= 0 ){
            return 0;
        }
        else{
            unsigned char floats[4] = {rx_buffer[3], rx_buffer[4], rx_buffer[5], rx_buffer[6]};
            float f = *((float *)&floats);
            return f;
        }
    }

}
