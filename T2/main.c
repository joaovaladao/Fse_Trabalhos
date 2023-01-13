#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <softPwm.h>
#include <time.h>

#include "UART/uart.h"
#include "PID/pid.h"

unsigned char solicitaTempInterna[7] = {0x01, 0x23, 0xC1, 3, 4, 3, 1};

//void init_gpio(void){

    const int PWMpinRes = 4; // WiringPI GPIO 23
    const int PWMpinVet = 5; // WiringPI GPIO 24

//}


// void init_estado(){
//     pid_configura_constantes(30.0, 0.2, 400.0);
// }

int main(){
    printf("-------- Estruturando o programa --------\n");

    //init_gpio();
    init_uart();
    //init_i2c();
    //init_estado();

    requestFloat(solicitaTempInterna);
    sleep(1);

    close_uart();
    }