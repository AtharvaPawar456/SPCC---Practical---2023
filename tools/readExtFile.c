// read content from extrenal 'input.txt' file

#include <stdio.h>
#include <stdlib.h>

#define MAX_LINE_LENGTH 100

int main() {
    FILE *fp;
    char line[MAX_LINE_LENGTH];

    fp = fopen("input.txt", "r");
    if (fp == NULL) {
        printf("Error opening file.\n");
        exit(1);
    }

    while (fgets(line, MAX_LINE_LENGTH, fp) != NULL) {
        printf("%s", line);
    }

    fclose(fp);

    return 0;
}
