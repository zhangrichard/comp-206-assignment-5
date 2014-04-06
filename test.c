#include <stdio.h>
#include <stdlib.h>
int main(void)
{
//FILE *f = fopen("data.txt","r");
printf("Content-Type:text/html;charset=iso-8859-1\n\n");

printf("<html>");
//if (f==NULL)
//{
printf("<head><title>ERROR</title></head>\n");
printf("<body><p>Unable to open file!</p><body>\n");
//else
//{
//while((ch=fgetc(f)) != EOF) putchar(ch);
//}
printf("</html>\n");
return 0;
}