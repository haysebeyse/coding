#include <stdio.h>

int f(int *a, int n) {

	if(n<=0)
		return 0;
	else if(*a % 2 == 0)
		return *a + f(a+1,n-1);
	else
		return *a - f(a+1,n-1);
	
}
int main() {

	int a[] = {12,7,5};
	printf("%i\n", f(a,3));
  
}

// 12 + 7 - 5 = 14