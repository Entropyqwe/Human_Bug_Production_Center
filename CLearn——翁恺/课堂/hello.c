#include <stdio.h>

int main(void) {
    printf("你好，C 语言 on macOS with VS Code!\n");
    printf("标准: C11, 编译器: %s\n", __clang_version__);
    return 0;
}
