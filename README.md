# Solve Quadratic Equation - SQE
Программа для решения квадратных уравнений через дискриминант
## Установка
Выполните эти команды:
```SH
cd ~
```
```SH
git clone https://github.com/Nikolaevviktord/sqe/
```
```SH
sudo mv ~/sqe/sqe.py /usr/bin/sqe.py
```
```SH
rm -r ~/sqe
```
Далее вставьте в файл `~/.bashrc` строку:
```SH
alias sqe='python3 /usr/bin/sqe.py'
```
## Использование
Синтаксис команды:
```SH
sqe a b c
```
a - коэфицент при x<sup>2</sup>, b - коэфицент при x, с - свободный член.
## Пример
```SH
sqe -0.5 3 -4
```
Вывод:
```
D: 1.0
Solutions: 2
Solution 1: 4.0
Solution 2: 2.0
```
