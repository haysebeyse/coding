#include <stdio.h>
int main()
{
   int* pc, c;
   
   c = 22;
   printf("\nAddress of c: %p\n", (void *)&c);
   printf("Value of c: %d\n\n", c);  // 22
   
   pc = &c;
   printf("Address of pointer pc: %p\n", (void *)pc);
   printf("Content of pointer pc: %d\n\n", *pc); // 22
   
   c = 11;
   printf("Address of pointer pc: %p\n", (void *)pc);
   printf("Content of pointer pc: %d\n\n", *pc); // 11
   
   *pc = 2;
   printf("Address of c: %p\n", (void *)&c);
   printf("Value of c: %d\n\n", c); // 2
   return 0;
}