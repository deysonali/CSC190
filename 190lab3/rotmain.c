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

int main(void){
	unsigned int left = 0;
	unsigned int right = 0;
	unsigned int majlminr= 0;
	unsigned int majrminr=0;
	avlNode *root1=NULL;
	avlNode *root2=NULL;
	avlNode *root3=NULL;
	avlNode *root4=NULL;
	int ans1=0;
	int ans2=0;
	int ans3=0;
	add_bst(&root1,5);
	add_bst(&root1,6);
	add_bst(&root1,1);
	add_bst(&root1,3);
	add_bst(&root1,4);
	add_bst(&root2,20);
        add_bst(&root2,30);
        add_bst(&root2,10);
        add_bst(&root2,25);
        add_bst(&root2,40);
	add_bst(&root2,50);
	add_bst(&root2,60);
	add_bst(&root3,10);
        add_bst(&root3,5);
        add_bst(&root3,15);
	add_bst(&root3,4);
        add_bst(&root3,6);
        add_bst(&root3,14);
	add_bst(&root3,16);
	add_bst(&root4,1);
        add_bst(&root4,5);
        add_bst(&root4,4);


	printf("root 1 Level Order: \n");
	printLevelOrder(root1);
	printf("root 2 Level Order: \n");
	printLevelOrder(root2);
	printf("root 3 Level Order: \n");
	printLevelOrder(root3);
	printTreeInOrder(root1);
	printf("root 4 Level Order: \n");
        printLevelOrder(root4);

	ans1=isAVL(root1);

	ans2=isAVL(root2);
	ans3=isAVL(root3); 
	if(ans2==0){ printf("tree 2 is AVL\n");}
        if(ans2==-1){printf("tree 2 is not AVL\n");}

	if(ans1==0){ printf("tree 1 is AVL\n");}
	if(ans1==-1){printf("tree 1 is not AVL\n");}
	
	if(ans3==0){ printf("tree 3 is AVL\n");}
        if(ans3==-1){printf("tree 3 is not AVL\n");}
	dblrotate(&root4,0);

	printf("Minor R Major L tree 4 in level order then in order\n");
	printLevelOrder(root4);
	printTreeInOrder(root4);
	rotate(&root2,0);
	printf("Left Rotated tree 2 level order then in order\n");
	printLevelOrder(root2);
	printTreeInOrder(root2);
	}
	
