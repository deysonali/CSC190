#include<stdlib.h>
#include<stdio.h>
#include<getData_charHead.c>
#include<getData_charStack.c>

int main (void) {

char value="\0";
char popped_value='\0';
int n=0;
llnode *input_list=NULL;


while (scanf("%c",&value) != EOF){

	if((value=="(")||(value=="{")||(value=="[")){
		push(&input_list,value);
	}
	if((value==")")||(value=="}")||(value=="]")){
		if((*input_list)==NULL){
			printf("FAIL: %d",n);
			return -1;
			}
		pop(&input_list,&popped_value);
		if(((value==")")&&(popped_value!="("))||((value=="}")&&(popped_value!="{"))||((value=="]")&&(popped_value!="["))){
			printf("FAIL: %d",n);
			return -1;
		}
	}

	n=n+1;
}

if (*input_list==NULL){
	printf("PASS");
	return 0;
}
else{
	printf("FAIL: %d",n);
	return -1;
}

}	
