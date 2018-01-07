#include <stdio.h>
#include "NN_func.h"

int main()
{
	float P = 10.0f;
	float result = heavyside(P);
	printf("%f   \n",result);
	return 0;
}

