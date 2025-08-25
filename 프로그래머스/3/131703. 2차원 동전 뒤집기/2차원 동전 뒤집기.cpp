#include <string>
#include <vector>
#include <iostream>

using namespace std;

int m, n;
vector<int> visitedRow;
vector<vector<int>> beginning, target;
int minCnt;

int check() {
    int neededCnt = 0;
    for (int x=0; x<n; x++) {
        bool normSame = (beginning[0][x]+visitedRow[0])%2 == target[0][x];
        for (int y=1; y<m; y++) {
            bool isSame = (beginning[y][x]+visitedRow[y])%2 == target[y][x];
            if (normSame != isSame) return -1;
        }
        
        if (!normSame) {
            neededCnt++;
        }
    }
    return neededCnt;
}

void dfs (int y, int flipCnt) {
    if (y == m) {
        int colFlipCnt = check();
        
        if (colFlipCnt != -1) {
            minCnt = min(minCnt, flipCnt+colFlipCnt);
        } 
        return;
    }
    
    // 해당 행 전체를 뒤집고
    visitedRow[y] = 1;
    dfs(y+1, flipCnt+1);
    
    visitedRow[y] = 0; // 되돌리기 및 뒤집지 않기
    dfs(y+1, flipCnt);
}

int solution(vector<vector<int>> b, vector<vector<int>> t) {
    minCnt = 21;
    m = t.size();
    n = t[0].size();
    visitedRow.assign(m, 0);
    beginning = b;
    target = t;
    
    dfs(0, 0);
    
    if (minCnt >= 21) return -1;
    return minCnt;
}