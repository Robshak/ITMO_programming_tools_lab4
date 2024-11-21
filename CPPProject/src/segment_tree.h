#ifndef SEGMENT_TREE_H
#define SEGMENT_TREE_H

#include <vector>
#include <algorithm>

const int inf = 1e9;

// Структура для узла сегментного дерева
struct Node {
    int min = inf;
    int max = -inf;
    int sum = 0;
};

// Вектор для хранения дерева
extern std::vector<Node> tree;

// Функция для слияния двух узлов
Node merge(Node a, Node b);

// Функция для построения дерева
void build(int v, int l, int r);

// Функция для обновления дерева
void update(int v, int l, int r, int pos, int new_val);

// Функция для запроса
Node query(int v, int l, int r, int ql, int qr);

// Внешний интерфейс для взаимодействия с Python через C
extern "C" {
    // Инициализация сегментного дерева
    void initialize_tree(int n);

    // Обёртка для построения дерева
    void build_wrapper(int n);

    // Обёртка для обновления дерева
    void update_wrapper(int pos, int new_val, int n);

    // Обёртка для выполнения запроса
    Node query_wrapper(int ql, int qr, int n);
}

#endif // SEGMENT_TREE_H
