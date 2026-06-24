## 📸 Screenshots

### 🎮 Empty Board

![Empty Board](screenshots/start_game.png)

Initial game state after launching the application.

### ✏️ Gameplay

![Gameplay](screenshots/gameplay.png)

Players take turns placing crosses and circles on the board.

### 🏆 Victory Screen

![Victory](screenshots/victory.png)

The game automatically detects a winner and draws a winning line.

### 🤝 Draw Situation

![Draw](screenshots/draw.png)

When all cells are filled and no winning combination exists, the game ends in a draw.

---

## 📸 Скріншоти

### 🎮 Початок гри

![Початок гри](screenshots/start_game.png)

Порожнє ігрове поле після запуску програми.

### ✏️ Ігровий процес

![Ігровий процес](screenshots/gameplay.png)

Гравці по черзі ставлять хрестики та нулики.

### 🏆 Перемога

![Перемога](screenshots/victory.png)

Гра автоматично визначає переможця та малює лінію перемоги.

### 🤝 Нічия

![Нічия](screenshots/draw.png)

Якщо всі клітинки заповнені та переможця немає, гра завершується нічиєю.
# ⭕❌ CrossZero — Turtle Graphics Game / Гра «Хрестики-нулики»

---

## 🌐 Language / Мова

* [🇬🇧 English](#english-version)
* [🇺🇦 Українська](#ukrainian-version)

---

<a name="english-version"></a>

# 🇬🇧 English Version

## 📌 Table of Contents

1. Project Purpose
2. Team Composition
3. File Contents
4. Modules & Technologies
5. How to Run
6. Project Overview
7. Conclusion

---

## 1. Project Purpose

**CrossZero** is a graphical Tic-Tac-Toe game developed in Python using the built-in `turtle` graphics library.

The project demonstrates fundamental programming concepts:

* Variables and data structures
* Lists for storing board state
* Conditional statements (`if`, `elif`, `else`)
* Loops (`for`, `while`)
* Functions and code organization
* Event-driven programming
* Mouse click handling
* Graphical rendering with Turtle Graphics

The game allows two players to compete on a 3×3 board, automatically detects victories and draws, and visually highlights the winning combination.

---

## 2. Team Composition

| Role      | Participant | GitHub     |
| --------- | ----------- | ---------- |
| Developer | Polina Revа | polinareva |

---

## 3. File Contents

```text
CrossZero/
│
└── CrossZero.py    # Main game file
```

### Navigation through the file

* Lines 1–25 — Screen setup and board drawing
* Lines 27–34 — Game state variables
* Lines 36–71 — Mouse click processing
* Lines 75–97 — Drawing X and O symbols
* Lines 100–113 — Draw detection
* Lines 115–131 — Victory detection
* Lines 133–170 — Winning line rendering
* Final lines — Event binding and game loop

---

## 4. Modules & Technologies

| Module                   | Purpose                                            |
| ------------------------ | -------------------------------------------------- |
| `turtle`                 | Drawing the board, symbols, text, and winning line |
| `Screen.onscreenclick()` | Mouse interaction                                  |
| Python Standard Library  | Core functionality                                 |

### Technologies

* Python 3.x
* Turtle Graphics
* Event-driven GUI programming

---

## 🚀 5. How to Run

### Requirements

* Python 3.7+
* tkinter (included with most Python installations)

### Installation

```bash
git clone https://github.com/polinareva/CrossZero.git
cd CrossZero
```

### Run

```bash
python CrossZero.py
```

A game window will appear with a 3×3 board.

### Controls

* Right mouse click inside a cell
* Player 1 places ❌
* Player 2 places ⭕
* Turns alternate automatically
* The game ends when a player wins or a draw occurs

---

## 6. Project Overview

### Game Mechanics

| Feature              | Description                                   |
| -------------------- | --------------------------------------------- |
| Board Representation | 9-element list stores cell states             |
| Turn System          | Alternates between Player 1 and Player 2      |
| Victory Detection    | Checks all 8 winning combinations             |
| Draw Detection       | Activated when the board is full              |
| Winning Line         | Drawn automatically through the winning cells |
| Graphical Interface  | Built entirely with Turtle Graphics           |

### Visual Elements

| Element      | Color          |
| ------------ | -------------- |
| Board        | White          |
| Background   | Black          |
| Cross (❌)    | Plum1          |
| Circle (⭕)   | Magenta        |
| Victory Text | Violet         |
| Winning Line | OrangeRed      |
| Draw Message | LightSlateBlue |

---

## 7. Conclusion

### Skills Practiced

* Event handling
* GUI programming fundamentals
* Coordinate systems
* State management
* Game logic implementation
* Victory and draw algorithms

### Possible Improvements

* Restart button
* Score tracking
* AI opponent
* Main menu
* Sound effects
* Better visual animations
* Multiplayer over network
* Refactoring into classes (OOP)

---

<a name="ukrainian-version"></a>

# 🇺🇦 Українська версія

## 📌 Зміст

1. Мета проєкту
2. Склад команди
3. Зміст файлів
4. Модулі та технології
5. Як запустити
6. Огляд проєкту
7. Висновок

---

## 1. Мета проєкту

**CrossZero** — це графічна реалізація гри «Хрестики-нулики», створена мовою Python із використанням стандартної бібліотеки `turtle`.

Проєкт демонструє основні концепції програмування:

* Роботу зі змінними
* Використання списків
* Умовні конструкції (`if`, `elif`, `else`)
* Цикли (`for`, `while`)
* Створення функцій
* Обробку подій
* Роботу з координатами
* Побудову графічного інтерфейсу

Гра дозволяє двом гравцям по черзі робити ходи, автоматично визначає переможця або нічию та відображає результат безпосередньо на ігровому полі.

---

## 2. Склад команди

| Роль      | Учасник     | GitHub     |
| --------- | ----------- | ---------- |
| Розробник | Поліна Рева | polinareva |

---

## 3. Зміст файлів

```text
CrossZero/
│
└── CrossZero.py    # Основний файл гри
```

### Навігація по файлу

* Рядки 1–25 — Налаштування екрана та малювання поля
* Рядки 27–34 — Ігрові змінні
* Рядки 36–71 — Обробка кліків миші
* Рядки 75–97 — Малювання хрестика та нулика
* Рядки 100–113 — Перевірка нічиєї
* Рядки 115–131 — Перевірка перемоги
* Рядки 133–170 — Малювання лінії перемоги
* Завершення файлу — запуск циклу гри

---

## 4. Модулі та технології

| Модуль                       | Призначення                                        |
| ---------------------------- | -------------------------------------------------- |
| `turtle`                     | Малювання поля, символів, тексту та лінії перемоги |
| `Screen.onscreenclick()`     | Обробка кліків миші                                |
| Стандартна бібліотека Python | Основна функціональність                           |

### Технології

* Python 3.x
* Turtle Graphics
* Подійно-орієнтоване програмування

---

## 🚀 5. Як запустити

### Необхідно

* Python 3.7+
* tkinter (зазвичай входить до Python)

### Клонування репозиторію

```bash
git clone https://github.com/polinareva/CrossZero.git
cd CrossZero
```

### Запуск

```bash
python CrossZero.py
```

Після запуску відкриється графічне вікно з ігровим полем 3×3.

### Керування

* Клік правою кнопкою миші по клітинці
* Гравець №1 ставить ❌
* Гравець №2 ставить ⭕
* Ходи чергуються автоматично
* Гра завершується після перемоги або нічиєї

---

## 6. Огляд проєкту

### Основні механіки

| Механіка            | Опис                                            |
| ------------------- | ----------------------------------------------- |
| Представлення поля  | Список із 9 елементів                           |
| Система ходів       | Почергові ходи двох гравців                     |
| Перевірка перемоги  | Аналіз 8 переможних комбінацій                  |
| Перевірка нічиєї    | Перевірка заповненості поля                     |
| Лінія перемоги      | Автоматично малюється через виграшну комбінацію |
| Графічний інтерфейс | Повністю створений за допомогою Turtle Graphics |

### Візуальні елементи

| Елемент                | Колір          |
| ---------------------- | -------------- |
| Поле                   | Білий          |
| Фон                    | Чорний         |
| Хрестик ❌              | Plum1          |
| Нулик ⭕                | Magenta        |
| Текст перемоги         | Violet         |
| Лінія перемоги         | OrangeRed      |
| Повідомлення про нічию | LightSlateBlue |

---

## 7. Висновок

### Чого навчає проєкт

* Обробка подій миші
* Основи GUI-програмування
* Робота з координатними системами
* Управління станом гри
* Реалізація ігрової логіки
* Алгоритми визначення перемоги та нічиєї

### Можливі покращення

* Кнопка перезапуску
* Таблиця результатів
* Штучний інтелект
* Головне меню
* Звукові ефекти
* Плавні анімації
* Мережева гра
* Перехід на об'єктно-орієнтований підхід (OOP)

---
