#include<stdio.h>
#include<stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;

/* printing in order allows that one check the correctness of the BST itself, since it literally prints in order */
/* level order traversal will help check the balance in an AVL tree*/

struct queue{
	int val;
	struct queue *next;
	};
typedef struct queue queue;

/*int emptyQ(queue *root){
	if(root==NULL){return 1;}
	else {
	return 0;
	}
}

queue* createQ(){
	return (queue*)malloc(sizeof(queue));
}

int add_to_head(queue **root, int val){
	queue *old_root;
	if (root == NULL){ return -1; }
	old_root = *root;
	*root = ( queue *) malloc(sizeof(queue));
	(*root) -> val = val;
	(*root) -> next = old_root;

return 0;

int take_and_del_from_tail(queue **root,int **rval)
	{
	struct queue *temp = NULL;
	if (root == NULL)
		{
		return -1;
		}
	if ((*root)->next == NULL)
	{	
		temp = *ppList;
		*ppList = NULL;
		*rval = (temp)->val;
		free(temp);
		return 0;
	}
	else
		{
		return ll_del_from_tail(&((*ppList)->next));
		}
}*/	

int printLevelOrder(bstNode *root){
	int height = levelheight(root);
	int i = 0;
	for (i=0;i<=height;i=i+1){
		printLevelNumber(root,i);
	}
}
	
int levelheight(bstNode *root) {
	if(root == NULL){
		return 0;
	}
	else{
		int hleft = levelheight(root->l);
		int hright = levelheight(root->r);
		if (hleft>hright){
			return (hleft+1);
		}
		else {
			return (hright+1);
		}
	}
}


int printLevelNumber(bstNode *root, int l){
	if(root==NULL){
		return 0;
	}
	if(l==1){
		printf("%d ",(root->val));
	}
	else if(l>1){
		printLevelNumber(root->l,l-1);
		printLevelNumber(root->r,l-1);
	}
}


int printTreeInOrder(bstNode *root){
	if(root == NULL){
		return -1;
	}
	printTreeInOrder((root->l));
	
	printf("%d\n",(root->val));
	
	printTreeInOrder((root->r));
	
	return 0;
}


int add_bst(bstNode **root,int val) {
   if (root == NULL) { return -1; }
   if (*root == NULL) {
       	*root = (bstNode *)malloc(sizeof(bstNode)*1);
	((*root)->val)=val;
	((*root)->l)=NULL;	
	((*root)->r)=NULL;
   } else {

      	if(((*root)->val)<val){
		add_bst(&((*root)->r),val);
		}
	else{
		add_bst(&((*root)->l),val);
   }
	return 0;
}
}	



int main(void) {
  	bstNode *root=NULL;
	int value = 0;
	while(scanf("%d",&value)!=EOF){
		add_bst(&root,value);
		}
	printTreeInOrder(root);
   

  /* bstNode *root=NULL;
   add_bst(&root,5);
   add_bst(&root,3);
   add_bst(&root,1);
   add_bst(&root,4);
   add_bst(&root,7);
   add_bst(&root,6);
   add_bst(&root,8);
   printTreeInOrder(root);
   printLevelOrder(root);
   return 0;*/
}

	
