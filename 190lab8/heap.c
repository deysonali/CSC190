#include<stdlib.h>
#include<stdio.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;

int initHeap(HeapType *pHeap, int size) {
	if(pHeap == NULL) {
		return -1;
	}
	(pHeap->store)=(int*)malloc(sizeof(int)*size);
	(pHeap->size)=size;
	(pHeap->end)=0;
	return 0;
}


int inOrderMaker(HeapType *pHeap, int *output, int n, int *index){

	if(*index>((pHeap)->end)-1){
		return 0;
	}
	else {
		inOrderMaker(pHeap, output, 2*n+1, index);
		output[*index] = (pHeap->store[n]);
		inOrderMaker(pHeap, output, 2*n+2, index);
		*index = (*index) +1;
	}
}

int inOrder (HeapType *pHeap, int **output, int *o_size){
	int index;
	int n;
	int end;
	if (pHeap == NULL){
		return -1;
	}
	index = 0;
	n = 0;
	end = (pHeap)->end;
	*output = (int*)malloc(sizeof(int)*(pHeap->end));
	inOrderMaker(pHeap,*output,n,&index);
	*o_size = index+1;		
        return 0;
}

int preOrderMaker(HeapType *pHeap, int *output, int n, int *index){

        if(*index>((pHeap)->end)-1){
                return 0;
        }
        else {	
		output[*index] = (pHeap->store[n]);
                preOrderMaker(pHeap, output, 2*n+1, index);
                preOrderMaker(pHeap, output, 2*n+2, index);
                *index = (*index) +1;
        }

}
int preOrder (HeapType *pHeap, int **output, int *o_size){
       	int index;
        int n;
        int end;
	
	if (pHeap == NULL){
                return -1;
        }
        index = 0;
        n = 0;
        end = (pHeap)->end;
        *output = (int*)malloc(sizeof(int)*(pHeap->end));
        preOrderMaker(pHeap,*output,n,&index);
        *o_size = index+1;
        return 0;
}

int postOrderMaker(HeapType *pHeap, int *output, int n, int *index){

        if(*index>((pHeap)->end)-1){
                return 0;
        }
        else {
                postOrderMaker(pHeap, output, 2*n+1, index);
                postOrderMaker(pHeap, output, 2*n+2, index);
                output[*index] = (pHeap->store[n]);
		*index = (*index) +1;
        }
}

int postOrder (HeapType *pHeap, int **output, int *o_size){
       	int index;
        int n;
        int end;
	
	if (pHeap == NULL){
                return -1;
        }
        index = 0;
        n = 0;
        end = (pHeap)->end;
        *output = (int*)malloc(sizeof(int)*(pHeap->end));
        postOrderMaker(pHeap,*output,n,&index);
        *o_size = index+1;
        return 0;
}
	

int addHeap(HeapType *pHeap, int key){	
	unsigned int end;
	int parentval;
	int parentind;
	int index;
	int temp;

	if (pHeap == NULL) {
		return -1;
	}
	end = ((pHeap)->end);
	parentval = 0;
	parentind = 0;
	index = 0;
	temp = 0;
	((pHeap)->store[end])=key;
	index = end;
	((pHeap)->end) = end + 1;
	
	while(1){
		if (index<=0){
			break;
		}
		if((index)%2!=0){
			parentind = index/2;
			parentval=((pHeap)->store[parentind]);
		}
		else {	
			parentind = (index-2)/2;
			parentval=((pHeap)->store[parentind]);
		}
		if(((pHeap)->store[index])>parentval){
			temp = (pHeap)->store[index];
			((pHeap)->store[index]) = (pHeap->store[parentind]);
			((pHeap)->store[parentind]) = temp;
			index = parentind;				
		}
		else {
			break;
		}
	}	
}

int findHeap(HeapType *pHeap, int key){
	int i = 0;
	if(pHeap == NULL) {
		return -1;
	}
	for (i = 0; i < (pHeap->end); i=i+1){
		if(((pHeap)->store[i])==key){
			return 1;
		}
	}
	return 0;
}

int delHeap(HeapType *pHeap, int *key){
	int rval;
	int node;
	int nodeval;
	int temp;
	int end;
	if(pHeap==NULL){
		return -1;
	}
	rval=0;
        node = 0;
        nodeval = ((pHeap)->store[node]);
        temp = 0;
        end= (pHeap)->end;

	if(((pHeap)->end)==0){
		return -1;
	}
	else {
		rval = (pHeap)->store[0];
		(pHeap)->end = ((pHeap)->end)-1;
		if(((pHeap)->end) >1){
			((pHeap)->store[0])=((pHeap)->store[end-1]);
			node = 0;
			while(1){
				if((nodeval>((pHeap)->store[2*node+1])) && (nodeval>((pHeap)->store[2*node+2]))){
					break;
				}
				if(((pHeap)->store[2*node+1])>=((pHeap)->store[2*node+2])){
					int temp = (pHeap)->store[2*node+1];
					(pHeap)->store[2*node+1] = (pHeap)->store[0];
					(pHeap)->store[0] = temp;
					node = 2*node+1;
				        nodeval = ((pHeap)->store[node]);
				}

				if(((pHeap)->store[2*node+1])<((pHeap)->store[2*node+2])){
                                        int temp = (pHeap)->store[2*node+2];
                                        (pHeap)->store[2*node+2] = (pHeap)->store[0];
                                        (pHeap)->store[0] = temp;
                                        node = 2*node+2;
                                        nodeval = ((pHeap)->store[node]);
                                }
			}
		}
	}
return rval;
}
	
				
			
		
		


	

