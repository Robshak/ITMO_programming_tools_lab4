# Тесты для дерева отрезков
Эти тесты проверяют корректность реализации операций дерева отрезков. Тесты написаны на Python с использованием библиотеки unittest. Каждая функция теста проверяет специфическую часть логики, чтобы гарантировать правильную работу сегментного дерева при различных сценариях.

## Оглавление
1. Описание тестов
2. Предварительная настройка
3. Обёртка C++
4. Список тестов
   + Тест: Инициализация дерева
   + Тест: Обновление и запрос значения
   + Тест: Множественные обновления
   + Тест: Граничные обновления
   + Тест: Перекрывающиеся диапазоны


## Описание тестов
Эти тесты проверяют операции над деревом отрезков, такие как инициализация, обновление, запрос на диапазон и комбинированные проверки. Тесты проводят как проверку базовой функциональности, так и проверку работы с граничными случаями, чтобы убедиться в корректной обработке всех сценариев.

## Предварительная настройка
Каждый тест инициализирует дерево отрезков с размером 32. Перед каждым тестом вызывается метод `setUp`, который выполняет следующие действия:
Вызывает `initialize_tree(size)`, чтобы инициализировать дерево нулями.
Вызывает `build_wrapper(size)`, чтобы построить дерево отрезков с дефолтными значениями.

## Обёртка C++
```python
lib_path = os.path.join(os.path.dirname(__file__), "CPPProject", "libsegment_tree.so")
segment_tree = ctypes.CDLL(lib_path)

class Node(ctypes.Structure):
    _fields_ = [("min", ctypes.c_int), ("max", ctypes.c_int), ("sum", ctypes.c_int)]

# Setting arguments and types for functions
segment_tree.initialize_tree.argtypes = [ctypes.c_int]
segment_tree.build_wrapper.argtypes = [ctypes.c_int]
segment_tree.update_wrapper.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
segment_tree.query_wrapper.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
segment_tree.query_wrapper.restype = Node
```

## Список тестов
### Тест: Инициализация дерева
Описание: Проверяет, что после инициализации дерево отрезков содержит корректные начальные значения (`min = inf`, `max = -inf`, `sum = 0`).

```python
def test_initial_values(self):
    result = segment_tree.query_wrapper(0, 32, self.size)
    self.assertEqual(result.min, 0)
    self.assertEqual(result.max, 0)
    self.assertEqual(result.sum, 0)
```

### Тест: Обновление и запрос значения
Описание: Проверяет, что при обновлении значения в узле дерево отрезков корректно обновляет значение и отражает изменения при запросе на этот узел.

```python
def test_single_update(self):
    segment_tree.update_wrapper(15, 10, self.size)

    result = segment_tree.query_wrapper(10, 20, self.size)
    self.assertEqual(result.min, 0)
    self.assertEqual(result.max, 10)
    self.assertEqual(result.sum, 10)
```

### Тест: Множественные обновления
Описание: Выполняет несколько обновлений в разных узлах в пределах одного диапазона и проверяет правильность вычисления минимального, максимального и суммарного значений для данного диапазона.

```python
def test_multiple_updates_in_range(self):
    segment_tree.update_wrapper(10, 5, self.size)
    segment_tree.update_wrapper(11, 7, self.size)
    segment_tree.update_wrapper(12, 3, self.size)

    result = segment_tree.query_wrapper(10, 13, self.size)
    self.assertEqual(result.min, 3)
    self.assertEqual(result.max, 7)
    self.assertEqual(result.sum, 15)
```

### Тест: Граничные обновления
Описание: Обновляет крайние значения дерева и проверяет, что дерево корректно обрабатывает минимальные и максимальные значения при запросе на весь диапазон.

```python
def test_edge_updates(self):
    segment_tree.update_wrapper(0, 20, self.size)
    segment_tree.update_wrapper(31, 40, self.size)

    result = segment_tree.query_wrapper(0, 32, self.size)
    self.assertEqual(result.min, 0)
    self.assertEqual(result.max, 40)
    self.assertEqual(result.sum, 60)
```

### Тест: Перекрывающиеся диапазоны
Описание: Проверяет корректность работы дерева с перекрывающимися диапазонами, включая обновлённые значения, с оценкой минимальных, максимальных и суммарных значений для обоих диапазонов.

```python
def test_overlapping_ranges(self):
    segment_tree.update_wrapper(14, 8, self.size)
    segment_tree.update_wrapper(18, 12, self.size)
    
    # Первый диапазон включает обновлённые значения
    result1 = segment_tree.query_wrapper(10, 20, self.size)
    self.assertEqual(result1.min, 0)
    self.assertEqual(result1.max, 12)
    self.assertEqual(result1.sum, 20)

    # Второй диапазон также включает обновлённые значения, но шире
    result2 = segment_tree.query_wrapper(15, 30, self.size)
    self.assertEqual(result2.min, 0)
    self.assertEqual(result2.max, 12)
    self.assertEqual(result2.sum, 12)
```

## Заключение
Эти тесты охватывают основные операции дерева отрезков, включая инициализацию, обновления, запросы на диапазоны и проверку значений. Убедитесь, что все тесты выполняются корректно перед выпуском новой версии, чтобы гарантировать правильную работу структуры данных и её соответствие требованиям проекта.
