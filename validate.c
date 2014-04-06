#include <stdlib.h>
#include <stdio.h>
int main(void)
{
FILE *in;
in = fopen("survey.ssv", "w");
char string[200];
char c;
int a = 0;
char String[100];
int n = atoi(getenv("CONTENT_LENGTH"));
while ((c = getchar()) != EOF && a<n)
{
if (a < 200)
{
if (c!='+') string[a]=c;
else string[a]=' ';
a++;
}
}
String[a] = '\0';
printf("%s\n",String);
}