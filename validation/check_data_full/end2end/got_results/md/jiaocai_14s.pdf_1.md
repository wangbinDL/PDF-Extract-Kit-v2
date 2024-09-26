conflict serializable schedules. The general form of view serializability is very expensive to test, and only a very restricted form of it is used for concurrency control.
14.6 Answer: There is a serializable schedule corresponding to the precedence graph below, since the graph is acyclic. A possible schedule is obtained by doing a topological sort, that is, \(T_{1}, T_{2}, T_{3}, T_{4}, T_{5}\).
14.7 Answer: A cascadeless schedule is one where, for each pair of transactions \(T_{i}\) and \(T_{j}\) such that \(T_{j}\) reads data items previously written by \(T_{i}\), the commit operation of \(T_{i}\) appears before the read operation of \(T_{j}\). Cascadesless schedules are desirable because the failure of a transaction does not lead to the aborting of any other transaction. Of course this comes at the cost of less concurrency. If failures occur rarely, so that we can pay the price of cascading aborts for the increased concurrency, noncascadeless schedules might be desirable.
14.8 Answer:
a. A schedule showing the Lost Update Anomaly:
\begin{tabular}{c|c}
\(T_{1}\) & \(T_{2}\) \\
\hline \begin{tabular}{c} 
read \((A)\) \\
write \((A)\)
\end{tabular} & \begin{tabular}{c} 
read \((A)\) \\
write \((\mathrm{A})\)
\end{tabular} \\
\hline
\end{tabular}
In the above schedule, the value written by the transaction \(T_{2}\) is lost because of the write of the transaction \(T_{1}\).
b. Lost Update Anomaly in Read Committed Isolation Level
\begin{tabular}{c|c}
\(T_{1}\) & \(T\)
\end{tabular}
\begin{tabular}{c|c}
\hline \begin{tabular}{c} 
lock-S \((A)\) \\
read \((A)\) \\
unlock \((A)\)
\end{tabular} & \begin{tabular}{c}
\(\operatorname{lock}-\mathrm{X}(A)\) \\
read \((A)\) \\
write \((A)\) \\
unlock \((A)\) \\
commit
\end{tabular}
\end{tabular}
The locking in the above schedule ensures the Read Committed isolation level. The value written by transaction \(T_{2}\) is lost due to \(T_{1}\) 's write.
c. Lost Update Anomaly is not possible in Repeatable Read isolation level. In repeatable read isolation level, a transaction \(T_{1}\) reading a