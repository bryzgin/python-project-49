[![Actions Status](https://github.com/bryzgin/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/bryzgin/python-project-49/actions)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=bryzgin_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=bryzgin_python-project-49)

# Brain Games

Комплект консольных игр, разработанных в рамках учебного проекта платформы Hexlet. Пакет включает в себя пять математических викторин. В рамках каждого игрового сеанса пользователю предлагается ответить на три случайных вопроса. Для успешного завершения игры необходимо дать три верных ответа подряд. В случае ошибки сессия завершается с выводом корректного ответа.

### Состав пакета:
* **brain-even** — проверка числа на четность.
* **brain-calc** — вычисление результатов арифметических выражений.
* **brain-gcd** — нахождение наибольшего общего делителя двух чисел.
* **brain-progression** — определение пропущенного элемента в арифметической прогрессии.
* **brain-prime** — проверка числа на то, является ли оно простым.

## Минимальные требования

* Python версии 3.10 или выше
* Пакетный менеджер uv

## Инструкция по установке

Пакет конфигурируется как автономная утилита командной строки. Установка с помощью `uv tool` позволяет выполнять команды напрямую, минуя использование префиксов виртуального окружения.

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com
   ```
2. Перейдите в каталог проекта:
   ```bash
   cd python-project-49
   ```
3. Выполните установку пакета в систему:
   ```bash
   uv tool install .
   ```

## Запуск приложений

После завершения установки вызов утилит осуществляется напрямую через терминал:

```bash
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

## Демонстрация работы (Asciinema)

В данном разделе представлены записи консольных сессий, демонстрирующие установку приложения, а также примеры игрового процесса с успешным и неудачным исходом.

### 1. Процесс установки
Демонстрация развертывания проекта и глобальной установки через команду `uv tool install .`:
[![asciicast](https://asciinema.org/a/GFHMoNCmFuo9If6y.svg)](https://asciinema.org/a/GFHMoNCmFuo9If6y)

### 2. Игра "Проверка на чётность" (brain-even)
Демонстрация игровых сессий (Победа и Поражение):
[![asciicast](https://asciinema.org/a/GFHMoNCmFuo9If6y.svg)](https://asciinema.org/a/GFHMoNCmFuo9If6y)

### 3. Игра "Калькулятор" (brain-calc)
Демонстрация игровых сессий (Победа и Поражение):
[![asciicast](https://asciinema.org/a/324zcPBoBxIMLkE2.svg)](https://asciinema.org/a/324zcPBoBxIMLkE2)

### 4. Игра "Наибольший общий делитель" (brain-gcd)
Демонстрация игровых сессий (Победа и Поражение):
[![asciicast](https://asciinema.org/a/du0UmPWAtsCGAGoe.svg)](https://asciinema.org/a/du0UmPWAtsCGAGoe)

### 5. Игра "Арифметическая прогрессия" (brain-progression)
Демонстрация игровых сессий (Победа и Поражение):
[![asciicast](https://asciinema.org/a/2GQgjkuMcBT1xauo.svg)](https://asciinema.org/a/2GQgjkuMcBT1xauo)

### 6. Игра "Простое число" (brain-prime)
Демонстрация игровых сессий (Победа и Поражение):
[![asciicast](https://asciinema.org/a/F51HEQVWBoD8AKF1.svg)](https://asciinema.org/a/F51HEQVWBoD8AKF1)
