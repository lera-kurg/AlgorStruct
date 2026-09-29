# include <iostream>
# include <vector>

//  !
// [2, 5, 7, 11, 15, 20]     dist = 9
//           !        !

using namespace std;

bool ok(vector<int>& arr, int k, int dist){
    int cows = 1;
    // запоминаем позицию последней поставленной коровы
    int last_cow_pos = arr[0];

    for (int i = 1; i<arr.size(); i++){
        // проверяем на >= нужного расстояния от послед до текущ стойла
        if (arr[i] - last_cow_pos >= dist){
            cows +=1;
            //обновляем позицию последней коровы
            last_cow_pos = arr[i];
        }

    }
    //если поставили >= k коров - dist достигнута
    return cows >= k;
}

int dvoich_search(vector<int>& arr, int k){

    int left = 0;
    //максимально возможное расстояние между коровами
    int right = arr.back() - arr[0] +1;

    while(right - left > 1){
        int mid = (left + right) / 2;
        //проверяем, можно ли расставить коров с расстоянием mid
        if(ok(arr, k, mid)){
            //если да, то ищем ещё большее расстояние
            left = mid;
        }
        else{
            //если нет - уменьшаем
            right = mid;
        }
    }
    return left;
}

int main(){
    int n, k;
    cin >> n >> k;
    vector<int> stoila;
    int i;
    while (cin >> i){
        stoila.push_back(i);
    }

    cout << dvoich_search(stoila, k);

    return 0;
}