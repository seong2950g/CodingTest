#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer;
    
    int answerFront = 0;
    int answerBack = 1000001;
    
    int frontIdx = 0;
    int backIdx = 0;
    int rangeSum = sequence[frontIdx];
    while (frontIdx >= 0 && backIdx < sequence.size()) {
        if (rangeSum < k) {
            rangeSum += sequence[++backIdx];
        } else if (rangeSum > k) {
            rangeSum -= sequence[frontIdx++];
        } else {
            // 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열
            if (backIdx-frontIdx < answerBack-answerFront) {
                answerFront = frontIdx;
                answerBack = backIdx;
            // 길이가 짧은 수열이 여러 개인 경우
            } else if (backIdx-frontIdx < answerBack-answerFront) {
                // 앞쪽에 나오는 수열
                if (frontIdx < answerFront) {
                    answerFront = frontIdx;
                    answerBack = backIdx;
                }
            }
            rangeSum += sequence[++backIdx];
        }
    }
    
    return {answerFront, answerBack};
}