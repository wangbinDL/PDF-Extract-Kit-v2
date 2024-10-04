1.3 // Assume \(\mathrm{n}\) holds the length of arr
2 double fast_product(double \(* \operatorname{arr}\), int \(\mathrm{n}\) ) \{
3 double product \(=1\);
4 \#pragma omp parallel for
5 for (int \(i=0 ; i<n ; i++)\{\)
6 product \(*=\operatorname{arr}[i]\);
7 \}
8 return product;
\(9 \}\)
(a) What is wrong with this code?
The code has the shared variable product.
(b) Fix the code using \#pragma omp critical
1 double fast_product(double \(* \operatorname{arr}\), int \(\mathrm{n}\}\{\)
2 double product \(=1\);
3 \#pragma omp parallel for
4 for (int \(i=0\); \(i<n\); i++) \{
5 \#pragma omp critical
6 product \(*=\operatorname{arr}[i]\);
7 \}
8 return product
\(9 \}\)
(c) Fix the code using \#pragma omp reduction(operation: var).
1 double fast_product(double \(* \operatorname{arr}\), int \(\mathrm{n})\{\)
2 double product \(=1\);
3 \#pragma omp parallel for reduction(*: product)
4 for (int \(i=0\); \(i<n\); i++) \{
6 \}
7 return product;
8 \}
2 Logic Gates
2.1 Label the following logic gates:

NOT, AND, OR, XOR, NAND, NOR, XNOR
2.2 Convert the following to boolean expressions:
(a) NAND