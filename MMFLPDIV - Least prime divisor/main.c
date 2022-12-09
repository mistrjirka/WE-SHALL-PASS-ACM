#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#define MAX_PRIME 99999989

int* makePrimeArray(size_t *len){
    static int arrayOfNums[MAX_PRIME];
    for(int i = 0; i <= MAX_PRIME - 2; i++){
        arrayOfNums[i] = i + 2;
    }
    for(int i = 0; i * i <= MAX_PRIME - 2; i++){
        if(arrayOfNums[i] != 0){
            for(int j = 2; j <= MAX_PRIME - 2; j++){
                if(arrayOfNums[i] * j <= MAX_PRIME){
                    arrayOfNums[arrayOfNums[i] * j - 2] = 0;
                } else{
                    break;
                }
            }
        }
    }
    int counter = 0;
    static int arrayOfPrimes[MAX_PRIME];
    for(int i = 0; i <= MAX_PRIME - 2; i++){
        if(arrayOfNums[i] != 0){
            arrayOfPrimes[counter] = arrayOfNums[i];
            counter++;
        }
    }
    *len = counter;
    return arrayOfPrimes;
}

int least_prime_divisor(int num)
{
    int least_prime[num+1];
}

int main(){
    int input_number = 0;
    int returnval = scanf("%d", &input_number);
    size_t length = 0;
    
    int *array_of_primes = makePrimeArray(&length);
    printf("%zu", length);
    while(input_number != 0 && returnval == 1){
        for(int i = 0; i < length; i++){
            if(input_number%array_of_primes[i]==0){
                printf("%d\n", array_of_primes[i]);
                break;
            }            
        }
        returnval = scanf("%d", &input_number);
    }
    return 0;
}

