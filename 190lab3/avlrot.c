#include<stdio.h>
#include<stdlib.h>
struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

struct qNode {
   avlNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;

int printLevelOrder(avlNode *root){
        int height = levelheight(root);
        int i = 0;
        for (i=0;i<=height;i=i+1){
                printLevelNumber(root,i);
        }
	printf("\n");
}

int levelheight(avlNode *root) {
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


int printLevelNumber(avlNode *root, int l){
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
int printTreeInOrder(avlNode *root){
        if(root == NULL){
                return -1;
        }
        printTreeInOrder((root->l));

        printf("%d\n",(root->val));

        printTreeInOrder((root->r));

        return 0;
}	


int isAVL(avlNode *root){
	int right = 0;
	int left = 0;
	int diff=0;

	if(root==NULL){return 0;}
	left=depth(root->l);
	right=depth(root->r);
	/*printf("Node with val %d has left depth %d\n",(root)->val,left);
	printf("Node with val %d has right depth %d\n",(root)->val,right);*/


	if((left-right)>0){
		diff=left-right;
		
	}
	else if((left-right)<0){
		diff=right-left;
	}
	else {diff =0;}
	/*printf("Node with val %d has diff %d\n",(root)->val,diff);*/
	if((diff <=1) && (isAVL(root->l)==0) && (isAVL(root->r)==0)){
		return 0;
	}
	return -1;
}

int depth(avlNode *root){
	int dr=0;
	int dl=0;
	if(root==NULL){
		return 0;
	}
	/*dr=depth(root->right);
	dl=depth(root->left);*/
	return 1+max(depth(root->r),depth(root->l));
	/*if(dr>dl){
		return dr+1;
	}
	if(dr<dl){
		return dl+1;
	}
	else {return dl+1;}*/
}

int max(int a, int b){
	if(a>=b){return a;}
	if(a<b){return b;}
	}

int add_bst(avlNode **root,int val) {
   if (root == NULL) { return -1; }
   if (*root == NULL) {
        *root = (avlNode *)malloc(sizeof(avlNode)*1);
        ((*root)->val)=val;
        ((*root)->l)=NULL;
        ((*root)->r)=NULL;

	return 0;
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

int rotate(avlNode **root,unsigned int Left0_Right1){
	avlNode *pivot;
	avlNode *oldroot=*root;
	if(root==NULL){return -1;}
	if(Left0_Right1==0){
		if(((*root)->r)==NULL){ return -1;}
		else {
			pivot=(*root)->r;
			(*root)=pivot;
			oldroot->r=pivot->l;
			pivot->l=oldroot;
			return 0;
		}
		}

	 if(Left0_Right1==1){
                if(((*root)->l)==NULL){ return -1;}
                else { pivot=(*root)->l;
                (*root)=pivot;
               
                oldroot->l=pivot->r;
                
                pivot->r=oldroot;
		return 0;
       		 }
	}
	else { return -1;}

}
	
	
int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1){
	
	unsigned int Left=0;
	unsigned int Right=1;
	int myval = -5;
	if(root==NULL) {return -1;}
	/*	if((*root)->l==NULL) {return -1;}*/
	
	if(MajLMinR0_MajRMinL1==1){       
		rotate(&((*root)->l),Left);
		rotate(&(*root),Right);
		return 0;
	}
	if(MajLMinR0_MajRMinL1==0){
       		rotate(&((*root)->r),Right);
		printLevelOrder(*root);
		printf("root val: %d\n", (*root)->val);
		printf("root right val: %d\n", ((*root)->r)->val);
		myval = rotate(root,Left);
		printf("myval %d\n", myval);
        	return 0;
	}
	else {return -1;}

}





	
