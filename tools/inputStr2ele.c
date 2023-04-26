#include <stdio.h>
#include <string.h>

int main()
{
    char input[100];
    char output[strlen(input)];
    int i;

    printf("Enter a string: ");
    scanf("%s", input);

    for (i = 0; i < strlen(input); i++)
    {
        output[i] = input[i];
    }

    for (i = 0; i < strlen(input); i++)
    {
        printf("%c\n", output[i]);
    }

    return 0;
}

/*
OUTPUT:
Enter a string: hello world
h
e
l
l
o

*/