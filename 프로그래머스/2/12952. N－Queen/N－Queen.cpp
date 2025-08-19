#include <string>
#include <vector>

using namespace std;

// (x, y)에 퀸을 놓을 수 있는지 확인하는 함수
bool check(int y, int x, vector<int>& visited) {
    for (int py=0; py<y; py++) {
        int px = visited[py];
        
        if (px == x) return false; 
        if (abs(px-x) == abs(py-y)) return false;
    }
    return true;
}

void backtrack(int y, vector<int>& visited, int& answer) {
    if (y == visited.size()) answer++;
    
    for (int x=0; x<visited.size(); x++) {
        if (check(y, x, visited)) {
            visited[y] = x;
            backtrack(y+1, visited, answer);
            visited[y] = -1;
        }
    }

}

int solution(int n) {
    int answer = 0;
    
    vector<int> visited(n, -1);
    backtrack(0, visited, answer);
        
    return answer;
}