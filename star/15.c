#include <stdio.h>

int main() {
	int N = 0;
	int i = 0, j = 0;
	scanf("%d", &N);
	for(i=0;i<N;i++) { // 줄 수
		if(i==0) {
			for(j=0;j<N-1;j++) { // 열 수
				printf(" ");
			}
			printf("*");
		} else {
			for(j=1;j<2*N-(3-i);j++) {
				if(j==N-i||j==N+i)
					printf("*");
				else if(j==2*N-(4-i)&&i==N-1){
					// printf("");
				} else
					printf(" ");
			}
		}
		printf("\n");
	}
	return 0;
}