#include <stdio.h>
char str;
int main(void) {
	while ((str = getchar()) && str != EOF)
		printf("%c", str);
	return 0;
}