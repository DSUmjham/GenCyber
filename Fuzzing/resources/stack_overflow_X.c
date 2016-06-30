/*
	Compile instructions (x32):
	gcc -g -fno-stack-protector -z execstack stack_overflow_X.c -o stack_overflow_X.out

	Compile instructions (x64):
	gcc -g -m32 -fno-stack-protector -z execstack stack_overflow_X.c -o stack_overflow_X.out

	Run instructions:
	./stack_overflow_X.out

	Debug instructions:
	gdb ./stack_overflow_X.out
*/

#include <stdio.h>
#include <stdlib.h>

void echo(void) 
{
	printf("Enter some text:\n");
	char buffer[64]; // 64 byte buffer stored on the stack
	gets(buffer); //retrieve user input and store in the buffer
	printf("%s\n", buffer); //print out the user input as a string
	return;
}


void main(void)
{
	echo();
	exit(0);
}