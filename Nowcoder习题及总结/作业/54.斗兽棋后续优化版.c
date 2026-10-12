#include <stdio.h>
#include <string.h>

int main() {
    char s1[20], s2[20];
    if (scanf("%s %s", s1, s2) != EOF) {
        if ((strcmp(s1, "elephant") == 0 && strcmp(s2, "tiger") == 0) ||(strcmp(s1, "tiger") == 0 && strcmp(s2, "cat") == 0) ||(strcmp(s1, "cat") == 0 && strcmp(s2, "mouse") == 0) ||(strcmp(s1, "mouse") == 0 && strcmp(s2, "elephant") == 0)) {
            printf("win\n");
        } 
      else if ((strcmp(s2, "elephant") == 0 && strcmp(s1, "tiger") == 0) || (strcmp(s2, "tiger") == 0 && strcmp(s1, "cat") == 0) ||(strcmp(s2, "cat") == 0 && strcmp(s1, "mouse") == 0) ||
(strcmp(s2, "mouse") == 0 && strcmp(s1, "elephant") == 0)) {
            printf("lose\n");
        } 
        else {
            printf("tie\n");
        }
    }
    return 0;
}