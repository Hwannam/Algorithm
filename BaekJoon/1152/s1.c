#include <stdio.h>
#include <string.h>

int main(){
    char str1[1000001];
    scanf("%[^\n]s", str1);
    int result = 0;
    for(int i=1; i<strlen(str1)-1; i++){
        if(str1[i]==' ') result++;
    }
    if((strlen(str1)==1) && (str1[0] == ' ')) result = -1;
    printf("%d", result+1);
    return 0;
}