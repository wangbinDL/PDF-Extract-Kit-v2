```markdown
# Chapter 14 Transactions

## 14.6 Answer:
There is a serializable schedule corresponding to the precedence graph below, since the graph is acyclic. A possible schedule is obtained by doing a topological sort, that is, T1, T2, T3, T4, T5.

## 14.7 Answer:
A cascadeless schedule is one where, for each pair of transactions Ti and Tj such that Tj reads data items previously written by Ti, the commit operation of Ti appears before the read operation of Tj. Cascadeless schedules are desirable because the failure of a transaction does not lead to the aborting of any other transaction. Of course this comes at the cost of less concurrency. If failures occur rarely, so that we can pay the price of cascading aborts for the increased concurrency, noncascadeless schedules might be desirable.

## 14.8 Answer:

### a. A schedule showing the Lost Update Anomaly:
```
T1          T2
read(A)     read(A)
write(A)    write(A)
```
In the above schedule, the value written by the transaction T2 is lost because of the write of the transaction T1.

### b. Lost Update Anomaly in Read Committed Isolation Level
```
T1          T2
lock-S(A)   lock-X(A)
read(A)     read(A)
unlock(A)   write(A)
            unlock(A)
            commit
```
The locking in the above schedule ensures the Read Committed isolation level. The value written by transaction T2 is lost due to T1's write.

### c. Lost Update Anomaly is not possible in Repeatable Read isolation level. In repeatable read isolation level, a transaction T1 reading a
```