#include <string>
#include <vector>

using namespace std;

bool check(vector<int>& stones, int k, int nPeople) {
    int step = 1;
    for (int canPeople : stones) {
        if (canPeople >= nPeople) {
            step = 1;
        } else {
            step++;
            if (step > k) return false;
        }
    }
    return true;
}

int solution(vector<int> stones, int k) {
    int lo = 1;
    int hi = 200000000;
    int mid = (lo + hi)/2;
    while (lo < hi-1) {
        mid = (lo+hi)/2;
        if (check(stones, k, mid)) {
            lo = mid;
        } else {
            hi = mid;
        }
    }
        
    return lo;
}