#include <stdio.h>

int main() {
	
	int N = 0;
	int i = 0;
	int result = 0;
	int mul = 0;
	scanf("%d",&N);
	
	char str[N];
	for(i=0;i<N;i++){
		scanf("%c",&str[i]);
		if(str[i]=='*') mul++;
	}
	
	for(i=0;i<(N/2);i++) {
		
		// 곱셈 연산 부분
		for(i=0;i<mul;i++){
			if(str[i]=='*') {
				result = str[i-1]*str[i+1];
				str[i]=0;
			}
		}
		
		for(i=0;i<(N/2)-mul;i++){
			if(str[i]=='+'){
				result = str[i-1]+str[i+1];
				str[i]=0;
			}else if(str[i]=='-'){
				result = str[i-1]-str[i+1];
				str[i]=0;
			}
		}
	}
	
	return 0;
}