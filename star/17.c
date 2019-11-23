#include <stdio.h>

int main() {
	int N = 0;
	int i = 0, j = 0;
	scanf("%d", &N);
	for(i=0;i<N;i++) {
		if(i==0) {
			for(j=0;j<N-1;j++) {
				printf(" ");
			}
			printf("*");
		} else if(i==N-1) {
			for(j=0;j<2*N-1;j++) {
				printf("*");
			}
		} else {
			for(j=1;j<2*N-(N-1-i);j++) {
				if(j==N-i||j==N+i)
					printf("*");
				else
					printf(" ");
			}
		}
		printf("\n");
	}
	return 0;
}
