#include <stdio.h>

int main() {
	int i =0;
	int input = 0;
	int _stack = 0;
	int stack_ = 0;
	for(i = 1; i<9;i++){
		if(i==8) scanf("%d",&input);
		else scanf("%d ",&input);
		if(input==i) _stack++;
		if(input==(9-i)) stack_++;
	}
	
	if(_stack==8) printf("ascending\n");
	else if(stack_==8) printf("descending\n");
	else printf("mixed\n");
	return 0;
}