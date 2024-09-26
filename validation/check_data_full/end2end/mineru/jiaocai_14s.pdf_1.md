conﬂict serial iz able schedules. The general form of view serial iz ability is very expensive to test, and only a very restricted form of it is used for concurrency control.  

14.6 Answer:  There is a serial iz able schedule corresponding to the precedence graph below, since the graph is acyclic. A possible schedule is obtained by doing a topological sort, that is,    $T_{1},\,T_{2},\,\bar{T_{3}},\,T_{4},\,T_{5}$  .  

14.7 Answer: A cascade less schedule is one where, for each pair of transactions    $T_{i}$   and  $T_{j}$   such that    $T_{j}$   reads data items previously written by    $T_{i},$   the commit operation of  $T_{i}$   appears before the read operation of  $T_{j}$  . Cascadeless schedules are desirable because the failure of a transaction does not lead to the aborting of any other transaction. Of course this comes at the cost of less concurrency. If failures occur rarely, so that we can pay the price of cascading aborts for the increased concurrency, non cascade less schedules might be desirable.  

14.8 Answer:  

a. A schedule showing the Lost Update Anomaly:  

In the above schedule, the value written by the transaction    $T_{2}$   is lost because of the write of the transaction    $T_{1}$  .  

b. Lost Update Anomaly in Read Committed Isolation Level  

The locking in the above schedule ensures the Read Committed isolation level. The value written by transaction  $T_{2}$   is lost due to  $T_{1}$  ’s write.  

c. Lost Update Anomaly is not possible in Repeatable Read isolation level. In repeatable read isolation level, a transaction    $T_{1}$   reading a  