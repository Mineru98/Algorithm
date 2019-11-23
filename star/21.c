#include <stdio.h>

int main() {
	int N = 0;
	int i = 0, j = 0;
	scanf("%d", &N);
	for(i=0;i<N*2;i++) {
		if(N==1) {
			for(j=0;j<N-1;j++) {
				printf(" ");
			}
			printf("*\n");
			break;
		} else {
			for(j=0;j<N;j++){
				if(i%2==1){
					if(j%2==0)
						printf(" ");
					else
						printf("*");
				} else {
					if(j%2==0)
						printf("*");
					else
						printf(" ");
				}
			}
		}
		printf("\n");
	}
	return 0;
}
