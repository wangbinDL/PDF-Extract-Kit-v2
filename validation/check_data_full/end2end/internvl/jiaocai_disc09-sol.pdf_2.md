```markdown
# Parallelism, SDS 3

## 1.3
### double fast_product(double *arr, int n) {
1. double product = 1;
2. #pragma omp parallel for
3. for (int i = 0; i < n; i++) {
4. product *= arr[i];
5. }
6. return product;
7. }

(a) What is wrong with this code?
The code has the shared variable product.

(b) Fix the code using #pragma omp critical
```c
double fast_product(double *arr, int n) {
    double product = 1;
    #pragma omp parallel for
    for (int i = 0; i < n; i++) {
        #pragma omp critical
        {
            product *= arr[i];
        }
    }
    return product;
}
```
(c) Fix the code using #pragma omp reduction(operation: var).
```c
double fast_product(double *arr, int n) {
    double product = 1;
    #pragma omp parallel for reduction(*: product)
    for (int i = 0; i < n; i++) {
        product *= arr[i];
    }
    return product;
}
```

## 2 Logic Gates
### 2.1
Label the following logic gates:
NOT, AND, OR, XOR, NAND, NOR, XNOR

### 2.2
Convert the following to boolean expressions:
(a) NAND