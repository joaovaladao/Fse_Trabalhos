#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wiringPiI2C.h>
#include <wiringPi.h>
#include <softPwm.h>
#include <time.h>

#include "UART/uart.h"

//void init_gpio(void){

    const int PWMpinRes = 4; // WiringPI GPIO 23
    const int PWMpinVet = 5; // WiringPI GPIO 24

//}

int main(){
    printf("-------- Estruturando o programa --------\n");

    //init_gpio();
    init_uart();
    //init_i2c();
    //init_estado();

    close_uart();
    }