# Практический пример кольцевого двусвязного списка: музыкальный плейлист.

from linked_list_itog import CircularDoublyLinkedList


class Playlist:
    # Плейлист использует готовую структуру CircularDoublyLinkedList.

    def __init__(self):
        self.songs = CircularDoublyLinkedList()

    def add_song(self, title):
        # Новая песня добавляется в конец кольцевого списка.
        self.songs.insert(self.songs.len(), title)

    def next_song(self):
        # direction = 1: переход на след песню по ссылке cursor.next.
        return self.songs.move_cursor(1)

    def previous_song(self):
        # direction = -1: переход на предыдущ песню по ссылке cursor.prev.
        return self.songs.move_cursor(-1)

    def current_song(self):
        if self.songs.cursor is None:
            return None
        return self.songs.cursor.data

    def show(self):
        """Показывает три узла и отмечает текущую композицию."""
        titles = self.songs.iter()
        if not titles:
            print("Плейлист пуст.")
            return

        print("\nПлейлист (кольцо):")
        print("<->".join(titles) + "<->" + titles[0] + "(возврат к началу)")
        print("Всего узлов:", self.songs.len())
        print("Текущая композиция:", self.current_song())
        print("Индекс курсора:", self.songs.cursor_index())
        print("Связи корректны:", self.songs.validate())


playlist = Playlist()
for title in ("Песня 1", "Песня 2", "Песня 3"):
    playlist.add_song(title)

print("Демонстрация кольцевого двусвязного списка")
print("Команды: 1 — следующая, 2 — предыдущая, 3 — показать список, 0 — выход")
playlist.show()

while True:
    command = input("\nВыберите команду: ").strip()

    if command == "1":
        print("Сейчас играет:", playlist.next_song())
    elif command == "2":
        print("Сейчас играет:", playlist.previous_song())
    elif command == "3":
        playlist.show()
    elif command == "0":
        print("Выход из плейлиста.")
        break
    else:
        print("Неизвестная команда. Введите 1, 2, 3 или 0.")

