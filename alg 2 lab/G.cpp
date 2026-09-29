#include <iostream>
using namespace std;

int main() {
    // коли-во длин верёвок, кол-во домиков
    int N, K;
    cin >> N >> K;
    
    int ropes[N];
    int maxLen = 0;
    
    // Читаем длины веревок и находим максимальную
    for (int i = 0; i < N; i++) {
        cin >> ropes[i];
        if (ropes[i] > maxLen) {
            maxLen = ropes[i];
        }
    }
    
    // Бинарный поиск по длине веревки
    int left = 1;           // минимальная длина (1 см)
    int right = maxLen;     // максимальная длина
    int answer = 0;         // здесь запоминаем ответ
    
    while (left <= right) {

        int mid = (left + right) / 2;  
        
        // Считаем, сколько веревок длины mid можно получить
        int count = 0;
        for (int i = 0; i < N; i++) {
            // += кол-во отрезков длиной mid можно отрезать на верёвочке
            count += ropes[i] / mid;  // сколько кусков из i-й веревки
        }
        
        // Если получили достаточно веревок
        if (count >= K) {
            answer = mid;       // запоминаем ответ
            left = mid + 1;     // пробуем длину побольше
        } 
        else {
            right = mid - 1;    // пробуем длину поменьше
        }
    }
    
    cout << answer << endl;
    return 0;
}