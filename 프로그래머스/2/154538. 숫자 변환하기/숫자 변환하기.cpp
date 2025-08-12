#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int x, int y, int n) {
    vector<int> dp(y+1, y+1);
    dp[x] = 0;
    
    for (int number=x; number<=y; number++) {
        int curOpCnt = dp[number];
        
        if (number+n <= y && dp[number+n] > curOpCnt+1) {
            dp[number+n] = curOpCnt+1;
        } 
        if (number*2 <= y && dp[number*2] > curOpCnt+1) {
            dp[number*2] = curOpCnt+1;
        }
        if (number*3 <= y && dp[number*3] > curOpCnt+1) {
            dp[number*3] = curOpCnt+1;
        }
    }
    
    if (dp[y] > y) return -1;
    
    return dp[y];
}