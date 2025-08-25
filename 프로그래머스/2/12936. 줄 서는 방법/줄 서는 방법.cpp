#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n, long long k) {
    vector<int> answer;
    
    // 팩토리얼(!) 결과값 저장
    vector<long long> factorial(n+1, 1);
    for (int i=2; i<factorial.size(); i++) {
        factorial[i] = i*factorial[i-1];
    }
    
    // number = {1, 2, ... , n};
    vector<int> number;
    for (int num=1; num<=n; num++) {
        number.push_back(num);
    }
    
    while (!number.empty()) {
        long long q = (k-1) / factorial[number.size()-1];
        long long r = (k-1) % factorial[number.size()-1];
        
        answer.push_back(number[q]);
        number.erase(number.begin() + q);
        
        k = r+1;
    }

    return answer;
}