/*
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
*/

/* core
① A ^ B % C = (A % C) * (B % C) % C
② Divide-and-Conquer
https://m.blog.naver.com/kks227/220583413569
*/

#include <stdio.h>

int C = 0;

int power(int n, int k){
	if(k == 0) return 1;
	
	int temp = power(n, k/2);
	int result = 1LL * temp * temp % C;
	if(k%2) result = 1LL * result * n % C;
	
	return result;
}

int main() {
	int A = 0;
	int B = 0;
	
	scanf("%d %d %d", &A, &B, &C);
	printf("%d\n", power(A,B));
	return 0;
}