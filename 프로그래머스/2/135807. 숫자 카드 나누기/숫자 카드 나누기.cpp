#include <string>
#include <vector>
#include <iostream>

using namespace std;

int gcd(int num1, int num2) {
    if (num1 < num2) {
        int temp = num1;
        num1 = num2;
        num2 = temp;
    }
    
    while (num2 != 0) {
        int remain = num1 % num2;
        num1 = num2;
        num2 = remain;
    }
    
    return num1;
}

int solution(vector<int> arrayA, vector<int> arrayB) {
    int gcdA = arrayA[0];
    int gcdB = arrayB[0];
    
    for (int i=1; i<arrayA.size(); i++) {
        gcdA = gcd(gcdA, arrayA[i]);
    }
    
    for (int i=1; i<arrayB.size(); i++) {
        gcdB = gcd(gcdB, arrayB[i]);
    }
    
    bool arrayAFlag = true; 
    for (auto& numB : arrayB) {
        if (gcdA > numB) continue;
        if (numB % gcdA == 0) {
            arrayAFlag = false;
            break;
        }
    }
    
    bool arrayBFlag = true;
    for (auto& numA : arrayA) {
        if (gcdB > numA) continue;
        if (numA % gcdB == 0) {
            arrayBFlag = false;
            break;
        }
    }
    
    if (arrayAFlag && arrayBFlag) {
        return max(gcdA, gcdB);
    } else if (arrayAFlag && !arrayBFlag) {
        return gcdA;
    } else if (!arrayAFlag && arrayBFlag) {
        return gcdB;
    } else {
        return 0;
    }
}