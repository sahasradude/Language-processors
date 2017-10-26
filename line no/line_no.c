#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(int argc, char * argv[]) {
    char buffer[128];
    sprintf(buffer, "bash ./line_no.sh %s %s", argv[1], argv[2]);
    return system(buffer);
}
