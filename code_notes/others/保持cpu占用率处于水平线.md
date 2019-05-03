
这也是网上查到的，觉得挺有趣的，就写了试了试。当时测试的时候用的是 vc++ 。下面这段代码是比较麻烦的要自己手动改参数。让cpu一半时间运行，一半时间不运行，使cpu占用率保持在50%。（没记错是这样的。）
```c
#include <stdio.h>
#include <windows.h>

long i;
int main() {
    while(1) {
        for( i=0;i<200000000000000;i++)
            ;

        Sleep(10);
        
    }
    return 0;
}

```