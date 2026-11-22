from player import Player
from maze import Maze
from items import Item, generate_starting_inventory


def show_help():
    print("\n--- Доступные команды ---")
    print(" w / a / s / d  - движение (вверх, влево, вниз, вправо)")
    print(" i              - открыть инвентарь")
    print(" srt val        - сортировать инвентарь по цене (sort)")
    print(" srt wt         - сортировать инвентарь по весу (sort)")
    print(" rev            - перевернуть инвентарь (reverse)")
    print(" drop           - выбросить последний предмет (pop)")
    print(" remove <имя>   - выбросить конкретный предмет (remove)")
    print(" use <имя>      - использовать предмет (например: use Зелье лечения)")
    print(" slice <с> <по> - показать часть инвентаря (срез списка)")
    print(" copy           - создать копию инвентаря (copy)")
    print(" q              - выйти из игры")


def show_inventory(player):
    print("\n--- Инвентарь ---")
    if not player.inventory:
        print("Пусто.")
    else:
        for i, item in enumerate(player.inventory):
            print(f"{i+1}. {item}")
    print(f"HP: {player.hp}/{player.max_hp}")


def main():
    print("=" * 40)
    print("ДОБРО ПОЖАЛОВАТЬ В ЛАБИРИНТ!")
    print("Соберите ключ и найдите портал, чтобы выбраться.")
    print("=" * 40)

    player = Player(0, 0)
    maze = Maze(5, 5)
    player.add_multiple_items(generate_starting_inventory())  # extend

    while player.hp > 0:
        print(f"\n[Координаты: ({player.x}, {player.y}) | HP: {player.hp}]")
        room = maze.get_room(player.x, player.y)

        if not room.visited:
            room.visited = True
            if room.room_type == "chest":
                print("Вы нашли сундук!")
                if room.loot:
                    print("В нём лежит:")
                    for item in room.loot:
                        print(f" - {item.name}")
                    player.add_multiple_items(room.loot)  # extend
                    room.loot = []
            elif room.room_type == "trap":
                print("Вы попали в ловушку! Потеряно 20 HP.")
                player.hp -= 20
            elif room.room_type == "key":
                print("Вы нашли КЛЮЧ ОТ ПОРТАЛА!")
                key = Item("Ключ", "key", 0.1, 0)
                player.add_item(key)  # append
                player.has_key = True
            elif room.room_type == "portal":
                print("Вы видите сияющий портал!")
                if player.has_key or "Ключ" in [i.name for i in player.inventory]:  # in
                    print("У вас есть ключ! Вы успешно выбрались из лабиринта. ПОБЕДА!")
                    break
                else:
                    print("Портал закрыт. Сначала нужно найти Ключ.")

        if player.hp <= 0:
            print("\nВы погибли... Игра окончена.")
            break

        cmd = input("\nВведите команду (h - помощь): ").strip().lower()

        if cmd == 'q':
            print("Вы вышли из игры.")
            break
        elif cmd == 'h':
            show_help()
        elif cmd == 'w' and player.y > 0:
            player.y -= 1
        elif cmd == 's' and player.y < maze.height - 1:
            player.y += 1
        elif cmd == 'a' and player.x > 0:
            player.x -= 1
        elif cmd == 'd' and player.x < maze.width - 1:
            player.x += 1
        elif cmd in ['w', 'a', 's', 'd']:
            print("Путь заблокирован стеной лабиринта.")
        elif cmd == 'i':
            show_inventory(player)
        elif cmd == 'srt val':
            player.sort_inventory("value")
            print("Инвентарь отсортирован по цене.")
        elif cmd == 'srt wt':
            player.sort_inventory("weight")
            print("Инвентарь отсортирован по весу.")
        elif cmd == 'rev':
            player.reverse_inventory()
            print("Порядок инвентаря изменен на обратный.")
        elif cmd == 'drop':
            dropped = player.drop_last_item()  # pop
            if dropped:
                print(f"Вы выбросили: {dropped.name}")
            else:
                print("Инвентарь пуст.")
        elif cmd.startswith('remove '):
            item_name = cmd[7:]
            for item in player.inventory:
                if item.name.lower() == item_name.lower():
                    player.remove_item(item)  # remove
                    print(f"Вы выбросили: {item_name}")
                    break
            else:
                print("Такого предмета нет.")
        elif cmd.startswith('use '):
            item_name = cmd[4:]
            idx = player.find_item_index(item_name)  # index + in
            
            if idx != -1:
                item = player.inventory[idx]
                if item.item_type == "potion":
                    player.heal(20)
                    player.inventory.pop(idx)  # pop
                    print("Вы выпили зелье и восстановили 20 HP.")
                else:
                    print("Этот предмет нельзя использовать.")
            else:
                print("Такого предмета нет.")
        elif cmd.startswith('slice '):
            try:
                parts = cmd.split()
                start, end = int(parts[1]), int(parts[2])
                sliced = player.get_inventory_slice(start, end)  # slice
                print("Срез инвентаря:")
                for it in sliced:
                    print(f" - {it.name}")
            except (IndexError, ValueError):
                print("Использование: slice <начало> <конец> (например: slice 0 2)")
        elif cmd == 'copy':
            inv_copy = player.copy_inventory()  # copy
            print(f"Создана копия инвентаря. В копии {len(inv_copy)} предметов.")
        else:
            print("Неизвестная команда. Введите 'h' для списка команд.")


if __name__ == "__main__":
    main()
