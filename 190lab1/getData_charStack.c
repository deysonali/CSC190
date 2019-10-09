
#include <stdio.h>
#include <stdlib.h>

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

int llnode_print_from_head(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
}

int llnode_print_from_tail(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      if (x->next == NULL) {
         printf("%c\n",x->value);
	 return 0;
      } else {
         llnode_print_from_tail(x->next);
         printf("%c\n",x->value);
	 return 0;
      }
   }
}

int main(void) {
   int n=0;
   int value=0;
   int rvalue=0;
   int stuff = 0;
   char return_value;
   llnode *input_list=NULL;

   while (scanf("%c",&value) != EOF) {
      n=n+1;
      push(&input_list,value);
   }
   pop(&input_list,&return_value);
   pop(&input_list,&return_value);
   printf("Popped: %c\n", return_value);
   printf("INFO: you entered %d items\n",n);
   rvalue=llnode_print_from_head(input_list);
   pop(&input_list,&return_value);
   printf("Popped: %c\n", return_value);
   printf("INFO: you entered %d items\n",n);
   rvalue=llnode_print_from_head(input_list);
    pop(&input_list,&return_value);
   printf("Popped: %c\n", return_value);
   printf("INFO: you entered %d items\n",n);
   rvalue=llnode_print_from_head(input_list);
 pop(&input_list,&return_value);
   printf("Popped: %c\n", return_value);
   printf("INFO: you entered %d items\n",n);
   rvalue=llnode_print_from_head(input_list);
 pop(&input_list,&return_value);
   printf("Popped: %c\n", return_value);
   printf("INFO: you entered %d items\n",n);
   rvalue=llnode_print_from_head(input_list);
   pop(&input_list,&return_value);
   printf("Popped: %c\n", return_value);
   printf("INFO: you entered %d items\n",n);
   rvalue=llnode_print_from_head(input_list);
   pop(&input_list,&return_value);
   printf("Popped: %c\n", return_value);
   printf("INFO: you entered %d items\n",n);
   rvalue=llnode_print_from_head(input_list);


   if ( !(rvalue==0) ) { printf("ERR: llnode_print returned an error\n"); }

   return 0;
}
