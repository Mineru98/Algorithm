#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_SIZE 10

void insertSort(int* pArr)
{
    int i, j;
    int key;

    for (i = 1; i < NUM_SIZE; i++)
    {
        key = pArr[i];
        for (j = i - 1; j >= 0; j--){
            if (pArr[j] > key)
            {
                pArr[j + 1] = pArr[j];
            }
            else
            {
                break;
            }
        }
        pArr[j + 1] = key;
    }
}

int* randomPlace()
{
	int random = 0;
    int* pArr;
    pArr = (int *)malloc(sizeof(int) * NUM_SIZE);

    if (pArr == NULL)
    {
        return NULL;
    }

    // 랜덤으로 리스트 배치
    srand(time(0));
	for (int i = 0; i < NUM_SIZE; i++) {
		random = rand()%9;
		pArr[i] = random;
	}

    return pArr;
}

int main()
{
    int* pArr = randomPlace();

    if (pArr == NULL)
    {
        printf("malloc error");
        return -1;
    }

    printf("Before : ");
    for (int i = 0; i < NUM_SIZE; i++)
    {
        printf("%d ", pArr[i]);
    }
    printf("\n");

    insertSort(pArr);


    printf("After : ");
    for (int i = 0; i < NUM_SIZE; i++)
    {
        printf("%d ", pArr[i]);
    }
    printf("\n");

    free(pArr);
    return 0;
}
