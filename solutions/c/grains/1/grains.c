#include "grains.h"
uint64_t square(uint8_t index){
    if (index<1 || index>64){
        return 0;
    }
    uint64_t out=1;
    return out << (index-1);
   
}
uint64_t total(void){
    uint64_t sum=0;
    uint64_t one=1;
    for (uint8_t i=0; i<64;i++ ){
        sum+=one<<i;
    }
    return sum;
} 





#ifndef GRAINS_H
#define GRAINS_H

#include <stdint.h>

uint64_t square(uint8_t index);
uint64_t total(void);

#endif