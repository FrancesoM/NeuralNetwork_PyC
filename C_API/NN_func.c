//
//  main.c
//  Neural_Functions
//
//  Created by Francesco Maio on 06/01/18.
//  Copyright © 2018 Francesco Maio. All rights reserved.
//
#include "NN_func.h"

float heavyside(float P)
{
    if(P >= 0)
    {
        return 1.0f;
    }
    else
    {
        return 0.0f;
    }
}

float logistic(float P)
{
    float temp = exp(-P);
    return 1.0f/(1.0f + temp);
}
