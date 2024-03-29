#include <stdlib.h>
#include "header.h"


void arrange(char* input, int n)
{
    /*
        Approach: Specific solution for n=3,4,5,6,7. From n>=8 , the first two moves make the input into 
        WBBW__(n-4 problem)BBWW
        Solve the n-4 recursively
        After solving we have
        WBBWWW....WWBB.....BB__BBWW
        Do:
        W__WWW....WWBB.....BBBBBBWW
        WWWWWW....WWBB.....BBBBBB__

        Time complexity:
        C(n) = C(n-4)+4 where C(n) = n for n=4,5,6,7 as can be seen from implementation
        After i iterations:
        C(n) = C(n-4i) + 4i
        Assume n is multiple of 4.
        n-4i = 4 implies i = (n-4)/4
        C(n) = C(4)+n-4 = n (exclamation mark. Can't put the symbol there xD)


    */

    if(n==3)
    {
        input = (char*)realloc(input, (2*n+5)*sizeof(char));
        input[2*n+4] = '\0';
        int i= 2*n + 3;
        while(i>=4)
        {
            input[i] = input[i-2];
            --i;
        }
        input[2] = '_';
        input[3] = '_';


        input[2] = input[5]; input[3] = input[6];
        input[5] = '_'; input[6] = '_';

        input[5] = input[8]; input[6] = input[9];
        input[8] = '_'; input[9] = '_';

        input[0] = input[6]; input[1] = input[7];
        input[6] = '_'; input[7] = '_';

    }
    else if(n==4)
    {

        input[0] = input[2*n-1]; input[1] = input[2*n];

        input[2*n-1] = input[n]; input[2*n] = input[n+1];

        input[n] = input[1]; input[n+1] = input[2];

        input[1] = input[2*n]; input[2] = input[2*n+1]; 

        input[2*n] = '_'; input[2*n+1] = '_';

    }

    else if(n==5)
    {

        input[0] = input[2*n-1]; input[1] = input[2*n];

        input[2*n-1] = input[n-1]; input[2*n] = input[n];

        input[n-1] = input[7]; input[n] = input[8];
        
        input[7] = input[1]; input[8] = input[2];

        input[1] = input[2*n]; input[2] = input[2*n+1];

        input[2*n] = '_'; input[2*n+1] = '_'; 

    }

    else if(n==6)
    {

        input[0] = input[2*n-1]; input[1] = input[2*n];

        input[2*n-1] = input[8]; input[2*n] = input[9];

        input[8] = input[3]; input[9] = input[4];
        
        input[3] = input[7]; input[4] = input[8];

        input[7] = input[1]; input[8] = input[2];

        input[1] = input[2*n]; input[2] = input[2*n+1]; 

        input[2*n] = '_'; input[2*n+1] = '_'; 

    }

    else if(n==7)
    {

        input[0] = input[2*n-1]; input[1] = input[2*n];

        input[2*n-1] = input[6]; input[2*n] = input[7];

        input[6] = input[9]; input[7] = input[10];
        
        input[9] = input[4]; input[10] = input[5];

        input[4] = input[10]; input[5] = input[11];

        input[10] = input[1]; input[11] = input[2];

        input[1] = input[2*n]; input[2] = input[2*n+1];

        input[2*n] = '_'; input[2*n+1] = '_'; 

    }

    else
    {
     
        input[0] = input[2*n-1]; input[1] = input[2*n];
 
        input[2*n-1] = input[4]; input[2*n] = input[5];
      
        input[4] = '_'; input[5] = '_';
        
        arrange(input+4,n-4);

        input[2*n-4] = input[1]; input[2*n-3] = input[2];
        input[1] = input[2*n]; input[2] = input[2*n+1]; 
        input[2*n] = '_'; input[2*n+1] = '_'; 
    }
    
}
