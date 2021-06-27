#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_SIZE 10

void selectSort(int* pArr)
{
    for (int i = 0; i < NUM_SIZE; i++) {
        int tmp = pArr[i];
		for (int j = 0; j < NUM_SIZE; j++) {
            // 오름차순
            if (tmp < pArr[j])
            {
                pArr[i] = pArr[j];
                pArr[j] = tmp;
                tmp = pArr[i];
            }

            // 내림차순
            /*
            if (tmp > pArr[j])
            {
                pArr[i] = pArr[j];
                pArr[j] = tmp;
                tmp = pArr[i];
            }
            */
        }
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

    selectSort(pArr);


    printf("After : ");
    for (int i = 0; i < NUM_SIZE; i++)
    {
        printf("%d ", pArr[i]);
    }
    printf("\n");

    free(pArr);
    return 0;
}
