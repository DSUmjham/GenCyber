// gcc -g environment_variable.c -o environment_variable.out

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main (void)
{
	char buffer[20]; // create a 20 byte buffer to hold the contents of HOME
	strcpy(buffer, getenv("HOME")); // get the HOME environment variable
	printf("HOME = %s\n", buffer); // print out the value
}