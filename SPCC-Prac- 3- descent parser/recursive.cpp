#include <stdio.h>
#include <string.h>
#include <iostream>
int i = 0;

using namespace std;

void E(char arr[]);
void E__(char arr[]);
void T(char arr[]);
void T__(char arr[]);
void F(char arr[]);

int main(void)
{
    char input[20];
    printf("Enter input string: ");
    cin >> input;
    E(input);

    if (i == strlen(input))
    {
        printf("Input Accepted");
    }
    else
    {
        printf("Not accepted");
    }
    return 0;
}

void E(char arr[])
{
    T(arr);
    E__(arr);
}

void E__(char arr[])
{
    if (arr[i] == '+')
    {
        i++;
        T(arr);
        E__(arr);
    }
}

void T(char arr[])
{
    F(arr);
    T__(arr);
}

void T__(char arr[])
{
    if (arr[i] == '*')
    {
        F(arr);
        T__(arr);
    }
}

void F(char arr[])
{
    if (arr[i] == '(')
    {
        i++;
        E(arr);
        if (arr[i] == ')')
        {
            i++;
        }
    }
    else if (arr[i] == 'i')
    {
        i++;
    }
    else
    {
        printf("Error at F\n");
        exit(1);
    }
}

/*
Output

test cases:
(i/i)       NA
i+i         A
i*i         failed
=i
i+



PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3> cd "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3\" ; if ($?) { g++ recursive.cpp -o recursive } ; if ($?) { .\recursive }
Enter input string: i+i
Input: UH��H�� H�MH�M�qError at T__
PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3> cd "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3\" ; if ($?) { g++ recursive.cpp -o recursive } ; if ($?) { .\recursive }
Enter input string: i++
Input: UH��H�� H�MH�M�qError at T__
PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3> cd "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3\" ; if ($?) { g++ recursive.cpp -o recursive } ; if ($?) { .\recursive }
Enter input string: (i/i)
Input: UH��H�� H�MH�M�q
PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3> cd "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3\" ; if ($?) { g++ recursive.cpp -o recursive } ; if ($?) { .\recursive }
Enter input string: i*i
Input: UH��H�� H�MH�M�qError at F
PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3> cd "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3\" ; if ($?) { g++ recursive.cpp -o recursive } ; if ($?) { .\recursive }
Enter input string: =i
Error at F
PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3> cd "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3\" ; if ($?) { g++ recursive.cpp -o recursive } ; if ($?) { .\recursive }
Enter input string: i+i
Input Accepted
PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3> cd "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3\" ; if ($?) { g++ recursive.cpp -o recursive } ; if ($?) { .\recursive }
Enter input string: i+
Error at F
PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3> cd "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3\" ; if ($?) { g++ recursive.cpp -o recursive } ; if ($?) { .\recursive }
Enter input string: (i/i)
PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3> cd "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3\" ; if ($?) { g++ recursive.cpp -o recursive } ; if ($?) { .\recursive }
Enter input string: (i/i)
PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3> cd "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3\" ; if ($?) { g++ recursive.cpp -o recursive } ; if ($?) { .\recursive }
Enter input string: (i/i)
Error at F
PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3> cd "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L -3\" ; if ($?) { g++ recursive.cpp -o recursive } ; if ($?) { .\recursive }
Enter input string: i+i
Input Accepted

*/