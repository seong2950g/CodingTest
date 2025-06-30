#include <string>
#include <vector>

using namespace std;

// 필요한 서버 수 계산
int getAddServerNum(vector<int> addedServers, int playerNum, int m) {
    if (playerNum < m) {
        return 0;
    }
    
    int neededServerNum = playerNum / m;
    int addServerNum = neededServerNum - addedServers.size();
    
    if (addServerNum < 0) {
        return 0;
    }
    
    return addServerNum;
}

int solution(vector<int> players, int m, int k) {
    int answer = 0;
    vector<int> addedServers;
    
    for (int playerNum : players) {
        int addServerNum = getAddServerNum(addedServers, playerNum, m);
        answer += addServerNum;
        
        for (int i=0; i<addServerNum; ++i) {
            addedServers.push_back(k);
        }
        
        vector<int> newAddedServers;
        for (int server : addedServers) {
            if (server > 1) {
                newAddedServers.push_back(server-1);
            }
        }
        
        addedServers = newAddedServers;
       
    }
    
    return answer;
}