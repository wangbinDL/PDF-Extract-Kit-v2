```
1.3//Assumenholdsthelengthofarr
2doublefast_product(double*arr,intn){
3doubleproduct=1;
4#pragmaompparallelfor
5for(inti=0;i<n;i++){
6product*=arr[i];
7}
8returnproduct;
9}
```
1.1Whatiswrongwiththiscode?

Thecodehasthesharedvariableproduct.
2. Fixthecodeusing#pragmaompcritical

```
1doublefast_product(double*arr,intn){
2doubleproduct=1;
3#pragmaompparallelfor
4for(inti=0;i<n;i++){
5#pragmaompcritical
6product*=arr[i];
7}
8returnproduct;
9}
```
3.cFixthecodeusing#pragmaompreduction(operation:var).

```
1doublefast_product(double*arr,intn){
2doubleproduct=1;
3#pragmaompparallelforreduction(*:product)
4for(inti=0;i<n;i++){
5product*=arr[i];
6}
7returnproduct;
8}
```

## 2 Logic Gates

Label the following logic gates:

```
1NOT,AND,OR,XOR,NAND,NOR,XNOR
2.2Convertthefollowingtobooleanexpressions: 1.NAND