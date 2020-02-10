#include <stdio.h>
#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

typedef int Status;

Status ListInsert(struct SqList *L, int i, int e)
{
	int k;
	if ( L->length == MAXSIZE)	//顺序线性表已满
	{
		return ERROR;
	}
	if (i<1 || i>L->length+1)	//i不在线性表范围内
	{
		return ERROR;
	}
	if (i<=L->length)	//若插入元素不再表尾
	{
		for (k=L->length-1; k>=i-1; k--)
		{
			L->data[k+1] = data[k];
		}
	}

	L->data[i-1] = e;
	L->length++;

	return OK;
}