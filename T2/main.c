#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <softPwm.h>
#include <time.h>

#include "UART/uart.h"
#include "PID/pid.h"

unsigned char solicitaTempInterna[7] = {0x01, 0x23, 0xC1, 3, 4, 3, 1};
unsigned char solicitaTempRef[7] = {0x01, 0x23, 0xC2, 3, 4, 3, 1};
double referencia = 0.0;

const int init_gpio(){

    const int PWMpinRes = 4; // WiringPI GPIO 23
    const int PWMpinVet = 5; // WiringPI GPIO 24

    return PWMpinRes, PWMpinVet;
}


// void init_estado(){
//     pid_configura_constantes(30.0, 0.2, 400.0);
// }

void loop(){
    float TempInterna = requestFloat(solicitaTempInterna);
    printf("Temperatura Interna: %f\n", TempInterna);

    float TempReferencia = requestFloat(solicitaTempRef);
    printf("Temperatura Referencia: %f\n", TempReferencia);
}

int main(){
    printf("-------- Estruturando o programa --------\n");
    const int PWMpinRes, PWMpinVet = init_gpio();

    init_uart();
    //init_i2c();
    //init_estado();

    while(1){
        loop();
    }

    close_uart();
    }