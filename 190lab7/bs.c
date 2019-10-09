#include<stdio.h>
#include<stdlib.h>
int bs(int *x,int size,int (*compare)(int x,int y)) {
	if(x==NULL){
	return -1;
	}
	int i = 0;
	int j = 0;
	int swapped = 1;
	int temp = 0;
	while(swapped == 1){	
		swapped = 0;
		for (i = 0; i <= size-1; i++){      
			for (j = 0; j < size-i-1; j++){ 
				if (compare(x[j],x[j+1]) == 0){	
					temp = x[j];
					x[j] = x[j+1];
					x[j+1] = temp;
					swapped = 1;
				}
			}
		}
	}
return 0;
}
int lt(int x,int y) {
	if (x<y){
		return 1;
	}
	else {
		return 0;
	}
}
int gt(int x,int y) {
	if (x>y) {
		 return 1;
        }
        else {
                return 0;
	}
}
    


 
