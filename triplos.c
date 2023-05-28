/*
    Autor: Nico Pauer
    Mail: nicolaspauer20@gmail.com
    Fecha: 28/05/2023

    Almacena los 10 primeros numeros de 3 a 30 y multiplos de 3 en un arreglo.
*/
#include <stdio.h>

/* Declaro las variables */
int num, contador;
/* Declaro el arreglo de enteros */
int lista[10];

void main()
{
  /* Inicializo las variables */
    num = 1;
    contador = 0;
  /* Inicializo elementos del arreglo desde la posicion 0 hasta la posicion 9 */
    while (contador < 10)
    {
      /* Para que sea multiplo de 3 */
        num *= 3;
      /* Inicializo elemento correspondiente en el arreglo */
        lista[contador] = num;
      /* Muestro que fue agregado e incremento en uno el contador para
         evitar bucle infinito */
        printf("%d agregado a posicion %d.\n", num, contador);
        contador += 1;
    }
}
