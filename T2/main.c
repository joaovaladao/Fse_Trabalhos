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

unsigned char ativacurva[8] = {0x01, 0x16, 0xD4, 3, 4, 3, 1, 1};
unsigned char desativacurva[8] = {0x01, 0x16, 0xD4, 3, 4, 3, 1, 0};

unsigned char enviaReferencia[7] = {0x01, 0x16, 0xD2, 3, 4, 3, 1};

// double pidRes = 0.0;
int curva, algoritmoIniciado, sistemaLigado, count;
float TempReferencia = 0.0;

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
    sendSignal(desativacurva, 0);
    curva = 0;
    sistemaLigado = 0;
    algoritmoIniciado = 0;
    count = 1;
}

void delay(unsigned milliseconds)
{
    clock_t pause;
    clock_t start;

    pause = milliseconds * (CLOCKS_PER_SEC / 1000);
    start = clock();
    while( (clock() - start) < pause );
}

void pid_activation(double pidRes, const int PWMpinRes, const int PWMpinVet){

    if(pidRes > -40 && pidRes < 0){
        pidRes = -40; 
    }

    printf("PID: %f\n", pidRes);
    sendInt(enviaInt, pidRes);

    if (pidRes < 0){
            softPwmWrite(PWMpinRes, 0);
            delay(0.5);
            softPwmWrite(PWMpinVet, pidRes * -1);
            delay(0.5);
    }

    else if (pidRes > 0){
            softPwmWrite(PWMpinVet, 0);
            delay(0.5);
            softPwmWrite(PWMpinRes, pidRes);
            delay(0.5);
        }   
}

void loop(const int PWMpinRes, const int PWMpinVet){

    time_t t = time(NULL);   
    struct tm tm = *localtime(&t);

    int usuario = requestInt(comandoUsuario);
    printf("Comando do Usuario: %d\n", usuario);

    if (usuario == 161){
        printf("Ligar Sistema\n");
        sendSignal(ligarSistema, 1);
        sistemaLigado = 1;
    }
    else if (usuario == 162){
        printf("Desligar Sistema\n");
        sendSignal(desligarSistema, 0);
        sistemaLigado = 0;
    }

    else if (usuario == 163){
        printf("Algoritmo Iniciado\n");
        sendSignal(algoritmoFuncion, 1);
        algoritmoIniciado = 1;
    }

    else if (usuario == 164){
        printf("Algoritmo Parado\n");
        sendSignal(algoritmoParado, 0);
        algoritmoIniciado = 0;
    }

    if(sistemaLigado == 0){
        printf("Sistema desligado, por favor ligue o sistema\n");
        sleep(2);
        return;
    }

    if(algoritmoIniciado == 0){
        printf("Algoritmo desligado, por favor inicie o software\n");
        sleep(2);
        return;
    }

    if(curva == 0){
        TempReferencia = requestFloat(solicitaTempRef);
        printf("Temperatura Referencia: %f\n", TempReferencia);
        pid_atualiza_referencia(TempReferencia);
    }

    else if(curva == 1){
        printf("Curva ativada\n");
        if (count > 0 && count < 30)
            TempReferencia = 25.0;
        else if (count >= 30 && count < 60)
            TempReferencia = 38.0;
        else if (count >= 60 && count < 120)
            TempReferencia = 46.0;
        else if (count >= 120 && count < 130)
            TempReferencia = 57.0;
        else if (count >= 130 && count < 150)
            TempReferencia = 61.0;
        else if (count >= 150 && count < 180)
            TempReferencia = 63.0;
        else if (count >= 180 && count < 210)
            TempReferencia = 54.0;
        else if (count >= 210 && count < 240)
            TempReferencia = 33.0;
        else if (count >= 240 && count < 300)
            TempReferencia = 25.0;
        else{
            curva = 0;
            count = 0;
            sendSignal(desativacurva, 0);
        }

        printf("Nova Temperatura Referencia (Curva): %f         ", TempReferencia);
        printf("Segundos: %d\n", count);
        pid_atualiza_referencia(TempReferencia);
        sendFloat(enviaReferencia, TempReferencia);
        count++;
    }

    float TempInterna = requestFloat(solicitaTempInterna);
    printf("Temperatura Interna: %f\n", TempInterna);
    double pidRes = pid_controle(TempInterna);

    if (usuario == 165){
        if(curva == 0){
            curva = 1;
            sendSignal(ativacurva, 1);
            float newref = 25.0;
            pid_atualiza_referencia(newref);
            sendFloat(enviaReferencia, newref);
        }
        else if(curva == 1){
            curva = 0;
            sendSignal(desativacurva, 0);
        }
        printf("Modo Curva Ativado/Desativado\n");
    }

    pid_activation(pidRes, PWMpinRes, PWMpinVet);

    FILE *fpt;
    fpt = fopen("log.csv", "a+");
    fprintf(fpt, "%02d/%02d/%d;%02d:%02d:%02d;%0.2lf;%0.2lf;%0.2lf\n", tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec, TempInterna, TempReferencia, pidRes);
    fclose(fpt);
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