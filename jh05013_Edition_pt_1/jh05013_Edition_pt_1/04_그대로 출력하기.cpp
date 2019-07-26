#include <stdio.h>
char str[105];
int main(void) {
	while (scanf("%[^\n]\n", str) == 1) {
		printf("%s\n", str);
	}
	return 0;
}