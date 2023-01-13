#ifndef _UART_
#define _UART_

void init_uart();
void close_uart();

float requestFloat(char cmd[]);

#endif