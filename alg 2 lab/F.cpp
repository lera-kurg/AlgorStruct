# include <iostream>
# include <algorithm>

using namespace std;
// надо сделать 1 копию, чтобы далее делать параллел копирование => ост 5-1 копии сделать
// 5(кол-во копий) 1(сек копир принтер) 2(сек копир принтер)
// 1 3 1
// 1 2 1
// right = 4 сек
// mid = (0 + 4)/2 = 2
// mid/x + mid/y = 2 cек / 1 (за _ секунд делается 1 копия) + 2 сек / 2 (за _ секунд делается 1 копия) = 2 копии + 1 копия = 3 копии
// 3 копии >= n-1 (5-1)
// left = 3
// mid = 3
// ... 
// 4 копии >= n-1 (4)  при mid = 3
// выводим 3 + 1 (сек ранее сделанной копии) = 4 сек (мин вр копирования)


long long dvoich_sort(long long n, long long x, long long y){
    long long left = 0;
    // перед одновременным копированием 
    // надо сделать хотя бы одну копию
    long long f = min(x, y);
    long long right = f * (n-1);

    while(left < right){
        long long mid = (left + right)/2;
        // Если за mid времени можно сделать n копий,
        // то за большее время - точно можно
        if((mid/x) + (mid/y) >= n-1){
            right = mid;
        } 
        else{
            left = mid+1;
        }
    }
    return left + f;
}

int main(){
    int n, x, y;

    cin >> n >> x >> y;

    cout << dvoich_sort(n, x, y);

    return 0;
}