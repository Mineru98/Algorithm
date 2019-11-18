// 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 
// input : 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)

#include <stdio.h>

int main() {
	int A = 0;
	int B = 0;
	int C = 0;
	
	scanf("%d %d %d", &A, &B, &C);
	
	if(A > B) {
		if (A > C) {
			if (B > C) {
				printf("%d\n", B);
			} else {
				printf("%d\n", C);
			}
		} else {
			printf("%d\n", A);
		}
	} else {
		if(B > C) {
			if(A > C) {
				printf("%d\n", A);
			} else {
				printf("%d\n", C);
			}
		} else {
			printf("%d\n", B);
		}
	}
	
	return 0;
}
