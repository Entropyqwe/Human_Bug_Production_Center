//*只在乎单一数组的编号而不是具体的值，经典问题：约瑟夫环
 #include <stdio.h>

int main() {
  
    int n, k, m;
    int people[105] = {0}; //*对于标记数组必须要进行赋值操作，将之赋成一个值，避免出现相互影响的情况

    scanf("%d %d %d", &n, &k, &m);

    int count = 0;      // 当前报的数 (1, 2, ... m)
    int out_count = 0;  // 已经出列的人数
    int current = k;    // 当前报数的人的编号（从 k 开始）

    // 只要出列的人数还没达到 n-1 (也就是还剩最后一个人)，就继续循环
    while (out_count < n - 1) {
        
        // 如果这个人还在圈里 (people[current] == 0)
        if (people[current] == 0) {//*current存在的意义和i差不多，因为已经说明了，树枝为0的才在这个数组中，如果因为报到了m所以出局了就会改为1，就不在这个数组中了
            count++; // 他报数
            
            // 如果他报到了 m
            if (count == m) {
                people[current] = 1; // 标记为出列
                out_count++;         // 出列人数加1
                count = 0;           // 报数归零，下一个人重新从1开始报
            }
        }

        // 移动到下一个人
        current++;

        // 【关键点】：这里模拟“围成一圈”
        // 如果编号到了 n，说明到了队尾，要回到编号 0
        if (current == n) {
            current = 0;//*约瑟夫环的关键，关键在于如何书写出围成一圈的这个设定 
        }
    }

    // 循环结束后，找出那个唯一还是 0 (没出列) 的人
    for (int i = 0; i < n; i++) {
        if (people[i] == 0) {
            printf("%d\n", i);
            break;
        }
    }

    return 0;
}