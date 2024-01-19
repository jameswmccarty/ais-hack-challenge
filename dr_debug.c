/* 
gcc dr_debug.c -L. -l:command-transmitter.so
patchelf --remove-needed command-transmitter.so a.out
patchelf --add-needed ./command-transmitter.so a.out

./a.out <string_to_scramble>

*/


#include<stdio.h>
#include<stdlib.h>

char * command_transmitter(char *param_1);

int main(int argc, char **argv) {
	printf(command_transmitter(argv[1]));
	fputc('\n',stdout);
	return 0;
}
