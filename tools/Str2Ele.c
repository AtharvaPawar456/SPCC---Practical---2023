#include <stdio.h>
#include <string.h>

int main()
{
    char input[] = "apple,banana,cherry";
    char *token;
    char *delimiter = ",";

    token = strtok(input, delimiter);

    while (token != NULL)
    {
        printf("%s\n", token);
        token = strtok(NULL, delimiter);
    }

    return 0;
}
/*
OUTPUT:
apple
banana
cherry

*/