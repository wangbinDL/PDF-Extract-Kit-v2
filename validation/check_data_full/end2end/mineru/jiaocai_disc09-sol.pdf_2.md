1.3 // Assume n holds the length of arr 2 double  fast product( double    $\mathsf{\star a r r}$  ,  int  n) { 3 double  product  $=~1$  ; 4 #pragma omp parallel  for 5 for  ( int    $\mathrm{~\bf~i~}=\;\theta\,;\,\mathrm{~\bf~i~}<\,\mathsf{n}\,;\,\mathrm{~\bf~i++~})\;\;\{$  6 product   $\star=$   arr[i]; 7 } 8 return  product; 9 }  

(a) What is wrong with this code? The code has the shared variable product. (b) Fix the code using  #pragma  omp critical 1 double  fast product( double  \*arr,  int  n) { 2 double  product  $\c=~1$  ; 3 #pragma omp parallel  for 4 for  ( int    $\textrm{i}=\,\emptyset$  ;   $\textup{i}<\textsf{n}$  ;   $\mathrm{i++}$  ) { 5 #pragma omp critical 6 product   $\star=$   arr[i]; 7 } 8 return  product; 9 } (c) Fix the code using  #pragma  omp reduction(operation: var) 1 double  fast product( double  \*arr,  int  n) { 2 double  product  $\c=~1$  ; 3 #pragma omp parallel  for  reduction(\*: product) 4 for  ( int    $\textrm{i}=\,\emptyset$  ;   $\textup{i}<\textsf{n}$  ;   $\mathrm{i++}$  ) { 5 product   $\star=$   arr[i]; 6 } 7 return  product; 8 }  

2 Logic Gates  

2.1 Label the following logic gates:  

2.2 Convert the following to boolean expressions:  

(a) NAND  