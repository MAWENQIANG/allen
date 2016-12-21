//警告：注意写出字符不要串行
#include <stdio.h>
main()
{
	int i,j,k,n=0;
	double sum;
	for(i=1;i<=4;i++)
	{
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				if(i != j && i != k && j != k)
				{
					sum=(i*100)+(j*10)+k;
					printf("%-4.0lf ",sum);
					sum=0;
					n++;
				}
			}
		}
	}
	printf("%d\n",n);
}
