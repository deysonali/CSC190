#include<stdlib.h>
#include<stdio.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;

int llnode_add_to_tail(llnode **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}

int llnode_add_to_head(llnode **x,char value) {
   llnode *p = *x;
   *x = (llnode *) malloc(sizeof(llnode));
   (*x)->value = value;
   (*x)->next = p;
   return 0;
   }


int push(llnode **x, char value) {
   llnode_add_to_head(x,value);
   }

int pop(llnode **x, char *return_value){
   if (x==NULL) { return -1;}
   if (*x==NULL) { return -1;}
   else {
        llnode *temp=NULL;

        (*return_value) = (*x)->value;
        temp = *x;
        (*x)= (temp->next);
        free(temp);
        return 0;
        }
}

int main (void) {

char value;
char popped_value;
int n=0;
llnode *input_list=NULL;
int rval=0;

while (scanf("%c",&value) != EOF){

	if((value=='(')||(value=='{')||(value=='[')){
		rval = push(&input_list,value);
	}
	if((value==')')||(value=='}')||(value==']')){
		rval = pop(&input_list,&popped_value);
		if(rval == -1){
			printf("FAIL, %d\n",n);
                        return -1;
                        }

		if(((value==')')&&(popped_value!='('))||((value=='}')&&(popped_value!='{'))||((value==']')&&(popped_value!='['))){
			printf("FAIL, %d\n",n);
			return -1;
		}
	}

	n=n+1;

}

rval = pop(&input_list,&popped_value);
if (rval == -1){
	printf("PASS\n");
	return 0;
}
else{
	printf("FAIL, %d\n",n-2);
	return -1;
}

}	
