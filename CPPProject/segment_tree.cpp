#include <vector>

const int inf = 1e9;

struct Node {
    int min = inf;
    int max = -inf;
    int sum = 0;
};

std::vector<Node> tree;

Node merge(Node a, Node b) {
    Node res;
    res.min = std::min(a.min, b.min);
    res.max = std::max(a.max, b.max);
    res.sum = a.sum + b.sum;
    return res;
}

void build(int v, int l, int r) {
    if (l + 1 == r) {
        tree[v].min = tree[v].max = 0;
        tree[v].sum = 0;
        return;
    }

    int m = (l + r) / 2;
    build(2 * v + 1, l, m);
    build(2 * v + 2, m, r);
    
    tree[v] = merge(tree[2 * v + 1], tree[2 * v + 2]);
}

void update(int v, int l, int r, int pos, int new_val) {
    if (l + 1 == r) {
        tree[v].min = tree[v].max = new_val;
        tree[v].sum = new_val;
        return;
    }

    int m = (l + r) / 2;
    
    if (pos >= m)
        update(2 * v + 2, m, r, pos, new_val);
    else
        update(2 * v + 1, l, m, pos, new_val);

    tree[v] = merge(tree[2 * v + 1], tree[2 * v + 2]);
}

Node query(int v, int l, int r, int ql, int qr) {
    if (ql >= r || qr <= l)
        return Node();
    if (ql <= l && qr >= r)
        return tree[v];
        
    int mid = (l + r) / 2;
    return merge(query(2 * v + 1, l, mid, ql, qr),
                 query(2 * v + 2, mid, r, ql, qr));
}

extern "C" {
void initialize_tree(int n) {
    tree.resize(4 * n);
}

void build_wrapper(int n) {
    build(0, 0, n);
}

void update_wrapper(int pos, int new_val, int n) {
    update(0, 0, n, pos, new_val);
}

Node query_wrapper(int ql, int qr, int n) {
    Node res = query(0, 0, n, ql, qr);
    return res;
}

} // extern "C"