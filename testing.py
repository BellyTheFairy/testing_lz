import math

def function(a, b, c, d, f):
    return (a + b) / (c - d) + math.sqrt(f)

def testing(a, b, c, d, f):
    args = f"a={a}, b={b}, c={c}, d={d}, f={f}"
    try:
        result = function(a, b, c, d, f)
        print(f"{args}\nРезультат: {res}")
        return result
    except ZeroDivisionError:
        msg = 'деление на ноль'
    except TypeError:
        msg = 'ошибка типов данных'
    except ValueError:
        msg = 'корень из отрицательного числа'
    except Exception as exc:
        msg = f'неизвестная ошибка: {exc}'
    print(f"{args}\nОшибка: {msg}")
    return msg
  
if __name__ == '__main__':
    print('Ручное тестирование')
    testing(2, 3, 5, 3, 4)
    testing(1.5, 2.5, 4.0, 2.0, 0.25)
    testing(1, 1, 3, 1, 0)
    testing(5, 5, 2, 2, 9)
    testing(4, 2, 5, 1, -4)
    testing('2', 3, 5, 3, 4)
    testing(2, 3, 5, 3, complex(4, 1))
    print('Конец тестирования')
