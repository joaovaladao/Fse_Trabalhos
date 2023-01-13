#include <stdio.h>
#include <softPwm.h>
#include <wiringPiI2C.h>
#include <wiringPi.h>

#include "UART/uart.h"

void init_gpio(void){

    const int PWMpinRes = 4; // WiringPI GPIO 23
    const int PWMpinVet = 5; // WiringPI GPIO 24

}

int main(){
    printf("Estruturando o programa");

    init_gpio();
    init_uart();
    init_i2c();
    init_estado();

    desligaForno();
    }