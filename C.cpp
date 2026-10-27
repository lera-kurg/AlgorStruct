#include <iostream>
#include <vector>
#include <string>

using namespace std;

class MinHeap
{
private:
    vector<int> heap;    // куча с нуля

    void siftUp(int i)   // просеивание вверх
    {
        // вычисляем индекс родителя
        int p = (i - 1) / 2;
        // пока текущий эл-т < родителя
        // завершится, когда эл-т на своём месте или достиг корня
        while (heap[i] < heap[p])
        {
            swap(heap[i], heap[p]);
            // поднимаемся выше
            i = p;
            p = (i - 1) / 2;
        }
    }

    void siftDown(int i) // просеивание вниз
    {
        // пока у эл-а есть хотя бы левый ребёнок
        while (2 * i + 1 < heap.size())
        {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            // проверка н авыход за границы
            if (left >= heap.size())
                return;
            // если правого ребёнка нет, то...
            if (right == heap.size())
                right = left;
            // выбираем индекс меньшего из двух детей
            int j = heap[right] < heap[left] ? right : left;
            // Если меньший ребёнок меньше текущего элемента, то...
            if (heap[j] < heap[i])
                swap(heap[j], heap[i]);
            // Перемещаемся на позицию ребёнка для следующей итерации
            i = j;
        }
    }

public:
    void clear()
    {
        heap.clear();
    }
    // добавляем новый эл-т
    void add(int x)
    {
        heap.push_back(x);
        // поднимаем новый элемент вверх,
        // пока он меньше своего родителя.
        siftUp(heap.size() - 1);
    }
    // Возвращает минимум и удаляет его из кучи.
    int extract() {
        int removed = heap[0];
        // Перемещаем последний элемент кучи на место корня.
        heap[0] = heap.back();
        // Удаляем последний элемент (он теперь "скопирован" в корень)
        heap.pop_back();
        // опускаем новый корень вниз,
        // меняя его с меньшим из детей.
        siftDown(0);
        return removed;
    }

    bool isEmpty() const {
        return heap.empty();
    }
};

int main()
{
    MinHeap h;
    int x;
    string command;

    while (cin >> command)
    {
        if (command == "CLEAR")
        {
            h.clear();
        }
        else if (command == "ADD")
        {
            cin >> x;
            h.add(x);
        }
        else if (command == "EXTRACT")
        {
            if (h.isEmpty())
            {
                cout << "CANNOT\n";
            }      
            else{
                
                cout << h.extract() << "\n";
            }
        }
    }
    return 0;
}

