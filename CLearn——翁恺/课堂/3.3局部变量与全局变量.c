//*在C语言中，当局部变量与全局变量同名时，局部变量会屏蔽全局变量，使用该变量时，访问局部变量
#include <stdio.h>

int a = 10; // 全局变量 a，初始值为 10

void F() {
    int a = 20; // 函数 F 内部的局部变量 a，初始值为 20
    printf("%d\n", a); // 打印当前作用域下的 a
}

void main() {
    int a = 30; // main 函数内部的局部变量 a，初始值为 30
    F();        // 调用函数 F
    printf("%d\n", a); // 打印 main 函数作用域下的 a
}