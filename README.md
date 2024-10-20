# Solve Quadratic Equation - SQE
Программа для решения квадратных уравнений через дискриминант
## Установка
Выполните эти команды:
```
cd ~
```
```
git clone https://github.com/Nikolaevviktord/sqe/
```
```
sudo mv ~/sqe/sqe.py /usr/bin/sqe.py
```
Далее вставьте в файл `~/.bashrc` строку:
```
alias sqe='python3 /usr/bin/sqe.py'
```
## Использование
Синтаксис команды:
```
sqe a b c
```
a - коэфицент при x<sup>2</sup>, b - коэфицент при x, с - свободный член.
## Пример
```
sqe -0.5 3 -4
```
Вывод:
```
D: 1.0
Solutions: 2
Solution 1: 4.0
Solution 2: 2.0
```
