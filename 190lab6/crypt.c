#include<stdio.h>
#include<stdlib.h>

unsigned char FSR(unsigned char x) {
   unsigned char oldbit0 = x & 0x1; /* extract bit 0 */
   unsigned char r = x >> 1;        /* shift right   */
   unsigned char newbit7 = oldbit0 << 7; /* move bit0 to the bit7 pos */
   r = r | newbit7; /* rotate the old value of bit 0 into the bit 7 pos */
   return r;
}

unsigned char prng(unsigned char x, unsigned char pattern) {	
   unsigned char oldbit0 = x & 0x1; /* extract bit 0 */
   unsigned char r = x >> 1;        /* shift right   */
   unsigned char newbit7 = oldbit0 << 7; /* move bit0 to the bit7 pos */
   r = r | newbit7; /* rotate the old value of bit 0 into the bit 7 pos */
   r = r^pattern;
   return r;
}

int crypt(char *data,unsigned int size,unsigned char password) {
	int i;
	unsigned char prngVal;

	if (data == NULL){
		return -1;
	}
	if (password == 0){
		return -1;
	}
	
	prngVal = password;
	for(i=0;i<size;i++){
		prngVal = prng(prngVal,0xb8);
		data[i] = data[i]^prngVal;
		
	} 
	return 0;
}

/*int main (void){
	char data[6];
	unsigned int size = 5;
	
	data = "Happy\0";
	unsigned int pwd = 32;
	crypt(&data, size, pwd);
        printf("New word = %s\n",data);
        
        return 0;
}*/

