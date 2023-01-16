#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <softPwm.h>
#include <time.h>
#include <wiringPi.h>

#include "UART/uart.h"
#include "PID/pid.h"

unsigned char solicitaTempInterna[7] = {0x01, 0x23, 0xC1, 3, 4, 3, 1};
unsigned char solicitaTempRef[7] = {0x01, 0x23, 0xC2, 3, 4, 3, 1};
unsigned char comandoUsuario[7] = {0x01, 0x23, 0xC3, 3, 4, 3, 1};
unsigned char enviaInt[7] = {0x01, 0x16, 0xD1, 3, 4, 3, 1};

unsigned char ligarSistema[8] = {0x01, 0x16, 0xD3, 3, 4, 3, 1, 1};
unsigned char desligarSistema[8] = {0x01, 0x16, 0xD3, 3, 4, 3, 1, 0};
unsigned char algoritmoFuncion[8] = {0x01, 0x16, 0xD5, 3, 4, 3, 1, 1};
unsigned char algoritmoParado[8] = {0x01, 0x16, 0xD5, 3, 4, 3, 1, 0};

double pidRes = 0.0;

const int init_gpio(){

    const int PWMpinRes = 4; // WiringPI GPIO 23
    const int PWMpinVet = 5; // WiringPI GPIO 24

    if (wiringPiSetup() == -1)
        exit(1);

    if (softPwmCreate(PWMpinRes, 0, 100) == 0){
        printf("PWM do resistor criado!\n");
    }
    if (softPwmCreate(PWMpinVet, 0, 100) == 0){
        printf("PWM da ventoinha criado!\n");
    }

    return PWMpinRes, PWMpinVet;
}


void init_estado(){
    pid_configura_constantes(30.0, 0.2, 400.0);
    sendSignal(desligarSistema, 0);
    sendSignal(algoritmoParado, 0);
}

void delay(unsigned milliseconds)
{
    clock_t pause;
    clock_t start;

    pause = milliseconds * (CLOCKS_PER_SEC / 1000);
    start = clock();
    while( (clock() - start) < pause );
}

void loop(const int PWMpinRes, const int PWMpinVet){
    float TempReferencia = requestFloat(solicitaTempRef);
    printf("Temperatura Referencia: %f\n", TempReferencia);
    pid_atualiza_referencia(TempReferencia);

    float TempInterna = requestFloat(solicitaTempInterna);
    printf("Temperatura Interna: %f\n", TempInterna);
    pidRes = pid_controle(TempInterna);

    int usuario = requestInt(comandoUsuario);
    printf("Comando do Usuario: %d\n", usuario);

    if (usuario == 161){
        printf("Ligar Sistema\n");
        sendSignal(ligarSistema, 1);
    }
    else if (usuario == 162){
        printf("Desligar Sistema\n");
        sendSignal(desligarSistema, 0);
    }

    else if (usuario == 163){
        printf("Algoritmo Iniciado\n");
        sendSignal(algoritmoFuncion, 1);
    }

    else if (usuario == 164){
        printf("Algoritmo Parado\n");
        sendSignal(algoritmoParado, 0);
    }

    if(pidRes > -40 && pidRes < 0){
        pidRes = -40; 
    }

    printf("PID: %f\n", pidRes);
    sendInt(enviaInt, pidRes);

    if (pidRes < 0){
            softPwmWrite(PWMpinRes, 0);
            delay(0.7);
            softPwmWrite(PWMpinVet, pidRes * -1);
            delay(0.7);
    }

    else if (pidRes > 0){
            softPwmWrite(PWMpinVet, 0);
            delay(0.7);
            softPwmWrite(PWMpinRes, pidRes);
            delay(0.7);
        }
    
}

int main(){
    printf("-------- Estruturando o programa --------\n");
    //const int PWMpinRes, PWMpinVet = init_gpio();

    const int PWMpinRes = 4; // WiringPI GPIO 23
    const int PWMpinVet = 5; // WiringPI GPIO 24

    if (wiringPiSetup() == -1)
        exit(1);

    if (softPwmCreate(PWMpinRes, 0, 100) == 0){
        printf("PWM do resistor criado!\n");
    }
    if (softPwmCreate(PWMpinVet, 0, 100) == 0){
        printf("PWM da ventoinha criado!\n");
    }

    init_uart();
    //init_i2c();
    init_estado();

    while(1){
        loop(PWMpinRes, PWMpinVet);
    }

    close_uart();
    }