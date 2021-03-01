#include <stdio.h>
#include <stdlib.h>
#include <string.h>



//gcc -o test_c test_c.c
//gcc -o test_c test_c.c;./test_c


struct Rect
{
  
  int x;
  int y;

  int wd;
  int ht;
};

typedef struct Rect Rect;


int addNums(int i1, int i2)
{
	int i3 = i1+i2;

	return i3;
}

//In and out params
char *getLN(int *pInt)
{
//allocate a box named line that holds 8 bytes which is an address to the character
	// then initialize it to hold address of string "jajv"
  char *line = "jajv";
  
  unsigned int len = strlen(line);

  *pInt = *pInt + len; 
  return line;
}//END getLN


int main()
{
	//printf("%s %d\n","hello world jajv", 777);
#if 0
	int i = 10;
	printf("%d\n",i);


	//int i = 10;
	printf("addr i : %p\n",(void*)&i);

    int iTotal = addNums(10,20);
    printf("iTotal : %d\n",iTotal);

//Name access
    Rect rect1 = {10,20,100,100};
    printf("rect1.x : %d\n",rect1.x);
   	
   	Rect *pRect1 = &rect1;
    printf("rect1->x : %d\n",pRect1->x);
   	printf("rect1->y : %d\n",pRect1->y);

  	printf("*((((int*)pRect1)+1)) : %d\n",*((((int*)pRect1)+1)));

//Print address of rect1
  	printf("pRect1 %p\n", pRect1);

    printf("pRect1+1 %p\n",pRect1+1);
    
    printf("pRect1+1 - pRect1 %p\n",(void*)((pRect1+1) - pRect1));

    int arr1[4] = {1,2,3,4};

    //int *pInt1 = &arr1[3];
    int *pInt1 = arr1;
    printf("*pInt1 %d\n",*pInt1);
    printf("*(pInt1+3) %d\n",*(pInt1+3));

    printf("sizeof(int) : %lu\n",sizeof(int));
    printf("sizeof(long) : %lu\n",sizeof(long));

    printf("sizeof(char *) : %lu\n",sizeof(char *));

    printf("sizeof(char) : %lu\n",sizeof(char));

    printf("sizeof(int *) : %lu\n",sizeof(int *));

  char *str = "abcd";
  char *pStr = str; 
  char *clone = malloc(strlen(str));
  strcpy(clone,str);
  printf("%s %lu\n", clone, strlen(clone));

#endif //0

//- allocate a box/mem of 4 bytes to hold an int and init it to 0
  int len=100;

//- allocate a box of 8 bytes to hold an char * and init to NULL
  char *pLine = NULL;

  pLine = getLN(&len); 

//- allocate a box of 8 bytes to hold an int1 * and init to NULL
  //int *pInt = NULL;
  
  printf("pLine : %s len : %d\n", pLine, len);


}//END main
