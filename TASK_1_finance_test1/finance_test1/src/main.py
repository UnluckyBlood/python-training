import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "finance.json")

# Загрузка данных из файла (если файл есть)
def load_data():
    """Загружает записи из JSON-файла."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []  # если файла нет, возвращаем пустой список

# Сохранение данных в файл
def save_data(records):
    """Сохраняет список записей в JSON-файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=4)

# Добавление новой записи
def add_record(records):
    """Запрашивает у пользователя данные и добавляет запись."""
    print("\n--- Добавление записи ---")
    typ = input("Тип (доход/расход): ").strip().lower()
    if typ in ["доход", "д", "1"]:
        typ = "доход"
    elif typ in ["расход", "р", "2"]:
        typ = "расход"
    else:
        print("Ошибка: неверный тип. Допустимо: доход/расход, д/р, 1/2")
        return
    category = input("Категория (например, еда, зарплата): ").strip()
    try:
        amount = float(input("Сумма: "))
    except ValueError:
        print("Ошибка: введите число")
        return
    description = input("Описание (необязательно): ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")  # текущая дата и время

    record = {
        "type": typ,
        "category": category,
        "amount": amount,
        "description": description,
        "date": date
    }
    records.append(record)
    save_data(records)
    print("Запись добавлена!")

# Просмотр всех записей
def view_records(records):
    """Выводит все записи в читаемом виде."""
    if not records:
        print("Записей пока нет.")
        return
    print("\n--- Все записи ---")
    for i, r in enumerate(records, 1):
        print(f"{i}. {r['date']} | {r['type']} | {r['category']} | {r['amount']} руб. | {r['description']}")

# Показать статистику
def show_stats(records):
    """Выводит общий доход, расход и баланс."""
    total_income = sum(r['amount'] for r in records if r['type'] == 'доход')
    total_expense = sum(r['amount'] for r in records if r['type'] == 'расход')
    balance = total_income - total_expense
    print("\n--- Статистика ---")
    print(f"Общий доход:  {total_income} руб.")
    print(f"Общий расход: {total_expense} руб.")
    print(f"Баланс:       {balance} руб.")

# Основное меню
def main():
    records = load_data()
    try:
        while True:
            print("\n=== Трекер финансов ===")
            print("1. Добавить запись")
            print("2. Показать все записи")
            print("3. Показать статистику")
            print("4. Выход")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                add_record(records)
            elif choice == "2":
                view_records(records)
            elif choice == "3":
                show_stats(records)
            elif choice == "4":
                print("До свидания!")
                break
            else:
                print("Неверный ввод, попробуйте снова.")
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем. До свидания!")

if __name__ == "__main__":
    main()