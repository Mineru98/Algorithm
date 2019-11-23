#include <stdio.h>
#include <string.h>

int main() {
	int n1, n2, idx=0, p=0, num1, num2, ans[10001];
	char c1[10001], c2[10001];

	scanf("%s %s", c1, c2);
	
	num1 = strlen(c1);
	num2 = strlen(c2);
	
	while (num1||num2||p) {
		if (num1)	n1 = c1[(num1--) - 1]-'0';
		if (num2)	n2 = c2[(num2--) - 1]-'0'; 
		ans[idx++] = (n1 + n2 + p) % 10;
		p = n1 + n2 + p > 9 ? 1 : 0;
		n1 = n2 = 0;
	}
	for (int i = idx-1; i >= 0; i--)printf("%d", ans[i]);
	printf("\n");
	return 0;
}
/*
#include<stdio.h>

int main() {
	int num1[10001], num2[10001], sum[10001];
	char num1[10001], num2[10001];
	int l1, l2;

	scanf("%s %s", num1, num2);

	for (l1 = 0; num1[l1] != '\0'; l1++)
		num1[l1] = num1[l1] - '0';

	for (l2 = 0; num2[l2] != '\0'; l2++)
		num2[l2] = num2[l2] - '0';

	int carry = 0;
	int k = 0;
	int i = l1 - 1;
	int j = l2 - 1;
	for (; i >= 0 && j >= 0; i--, j--, k++) {
		sum[k] = (num1[i] + num2[j] + carry) % 10;
		carry = (num1[i] + num2[j] + carry) / 10;
	}
	if (l1 > l2) {

	while (i >= 0) {
		sum[k++] = (num1[i] + carry) % 10;
		carry = (num1[i--] + carry) / 10;
	}

	} else if (l1 < l2) {
		while (j >= 0) {
			sum[k++] = (num2[j] + carry) % 10;
			carry = (num2[j--] + carry) / 10;
		}
	} else {
		if (carry > 0)
			sum[k++] = carry;
	}


	
	for (k--; k >= 0; k--)
	printf("%d", sum[k]);
	printf("\n");
	return 0;
}
*/