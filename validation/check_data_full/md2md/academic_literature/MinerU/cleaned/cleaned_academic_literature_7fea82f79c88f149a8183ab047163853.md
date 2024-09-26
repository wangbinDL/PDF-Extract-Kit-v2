# Formation of coalition structures as a non-cooperative game 2: applications  

Dmitry Levando,   ∗  

# Abstract  

The paper uses a non-cooperative simultaneous game for coalition structure formation (Levando, 2016) to demonstrate some applications of the introduced game: a cooperation, a Bayesian game within a coali- tion with intra-coalition externalities, a stochastic game, where states are coalition structures, self-enforcement properties of non-cooperative equilibrium and construction of a non-cooperative stability criterion.  

Keywords: Noncooperative Games, Cooperation, Bayesian Games, Stochas- tic Games, JEL  : C72, C73  

# 1 Subject of the paper  

The previous paper, Levando (2016), introduced a non-cooperative game to study coalition structures formation as a non-cooperative game. The sug- gested game consisted of a set of players    $N^{1}$  , a coalition structure construc- tion mechanism (  $\{K,{\mathcal{P}}(K),{\mathcal{R}}(K)\})$  , and individual properties of players,  

$(S_{i}(K),{\mathcal{U}}(K))_{i\in N}$  , such that  

$$
\Gamma(K)=\Big\langle K,\{K,\mathcal{P}(K),\mathcal{R}(K)\},(S_{i}(K),\mathcal{U}_{i}(K))_{i\in N}\Big\rangle,
$$  

where    $K$   is a maximum coalition size or a maximum number of deviators,  ${\mathcal{P}}(K)$   is a family of coalition structures such that any coalition size (a number of deviators ) does not exceed    $K$  ,    $\mathcal{R}(K)$   is a family of speciﬁc coalition structure formation rules,    $S_{i}(K)$   is a corresponding set of strategies of    $i\in N$  induced by    $K$  ,    $\mathcal{U}_{i}(K)$   is family of speciﬁc coalition structure payoﬀs for    $i$   in every partition    $P\in\mathcal{P}(K)$  . Games for all relevant    $K$   make a nested family  

$$
\Gamma=\{\Gamma(K=1),.\ldots,\Gamma(K),.\ldots\Gamma(K=N)\}\colon\Gamma(K=1)\subset\Gamma(K)\subset\Gamma(K=N).
$$  

The family of games is characterized by a list of equilibrium strategy pro- ﬁles,  $\Bigl(\sigma^{*}(1),.\,.\,,\sigma^{*}(K),.\,.\,,\sigma^{*}(K=N)\Bigr)$  , where    $\sigma^{*}(K)=(\sigma_{i}^{*}(K))_{i\in N}$  . and by a list of equilibrium partitions,  $\Big(\{P^{*}\}(1),.\,.\,.\,,\{P^{*}\}(K),.\,.\,.\,,\{P^{*}\}(K\,=\,$   $N){\Big)}$  ,    $\{P^{*}\}(K)\subset{\mathcal{P}}(K)$  . Every game   $\Gamma(K)$   from a family   $\Gamma$  , which has an equilibrium may be in mixed strategies.  

This paper demonstrates applications of the constructed game for: self- interest cooperation, a Bayesian stochastic game, studying self-enforcing properties of an equilibrium and construction of a non-cooperative criterion of coalition structure stability.  

# 2 Cooperation  

To explain formally cooperation we will retell with necessary changes the example from the corporate dinner game in Levando (2016). The result of this example will be used to explain formal deﬁnition of what a cooperation in allocations of self-interest players can be. In this section the term ”coop- eration” means only a cooperation of players in allocations over coalitions.  

Cooperation in payoﬀs is not addressed here.  

# 2.1 Cooperation in a corporate dinner game  

Consider a game of 4 players: A is a President; B is a senior vice-president;  $C_{1},C_{2}$   are two other vice-presidents. Coalition is a group of players at  one table. Every player may sit only at one table. Coalition structure is an allocation of all players over no more than four tables. Empty tables are not taken into account.  

Individual set of strategies is a set of all coalition structures for the play- ers. Any player can choose a coalition structure. A set of strategies in the game is a direct (Cartesian) product of four individual strategy sets. A choice of all players is a point in the set of strategies of the game.  

Preferences are such that everyone (besides A) would like to have a dinner with A, but A only with B. Everyone wants players outside his table to eat individually, due to possible dissipation of rumors or information exchange. No one can enforce others to form or not to form coalitions.  

In every partition any coalition (i.e. a table with players who eat at the table) is formed only if everybody at the table agrees to have dinner together, otherwise the player eats alone. The same coalition belongs to diﬀerent coalitions, but with diﬀerent allocations of other players over other coalitions.  

The game is simultaneous and one shot. Realization of the ﬁnal partition ( a coalition structure) depends on choices of coalition structures of all play- ers. Example. Let player A choose    $\{\{A,B\},\{C_{1}\},\{C_{2}\}\}$  ; player B choose  $\{\{A,B\},\{C_{1}\},\{C_{2}\}\}$  ; player    $C_{1}$   choose    $\{\{A,C_{1}\},\{B\},\{C_{2}\}\}$  , and player    $C_{2}$  choose    $\{\{A,C_{2}\},\{B\},\{C_{2}\}\}$  . Then the ﬁnal partition is    $\{\{A,B\},\{C_{1}\},\{C_{2}\}\}$  It is clear that strong Nash equilibrium (Aumann, 1960), which is based on a deviation of a coalition of any size, does not discriminate between coalition structures mentioned above.  

Players have preferences over coalition structures. Payoﬀproﬁle of the game should be deﬁned for every ﬁnal coalition structure. Table 1 presents coalition structures only with the best individual payoﬀs.   Thus only some partitions from the big set of all strategies deserve attention. The ﬁrst column is a number of a strategy. The second column is an allocation of players over a coalition structure, i.e. a strategy, and also a list of best ﬁnal coalition structures. The third column is a payoﬀproﬁle for all players of every listed coalition structure. The fourth column is a list of coalition values in the listed coalition structure, if to calculate values from the cooperative game theory.  

Payoﬀs are deﬁned for a game of four players in such a way, that an increase in the size of a maximum coalition from    $K=2$   to    $K=3,4$   only de- creases individual payoﬀs. Thus from one side there is ”an optimal” coalition size, from another an increase in a maximum coalition size does not change the equilibrium. The last property will be addressed formally in one of the following sections of the current paper.  

<td><table  border="1"><thead><tr><td><b>num</b></td><td><b>Best final partitions</b></td><td><b>Non-cooperative payoff profile (UA, UB, Uc1, Uc2)</b></td><td><b>Values of coalitions as in cooperative game theory</b></td></tr></thead><tbody><tr><td>1</td><td>[{A, B],[Ci], [C2]]</td><td>(10,10,3,3)</td><td>20AB, 3c1, 3c2</td></tr><tr><td>2*</td><td>{{A, B], {C1, C2]]</td><td>(8,8,5,5)</td><td>16AB, 10c1,C2</td></tr><tr><td>3</td><td>{{A, C1},{B, C2]]</td><td>(3,5,10,5)</td><td>13AC1, 10BC2</td></tr><tr><td>4</td><td>[{A, Ci],[B], [C2]]</td><td>(3,3,10,3)</td><td>13AC1, 3B, 3C2</td></tr><tr><td>5</td><td>{{A, C2},{B, Ci})</td><td>(3,5,5,10)</td><td>13AC2, 10BC1</td></tr><tr><td>6</td><td>{{A, C2],{B],[C1]]</td><td>(3,3,3,10)</td><td>13ACt, 3B, 3c1</td></tr><tr><td>7</td><td>all other partitions</td><td>(1,1,1,1)</td><td>≤4</td></tr></tbody></table></td>  

The game runs as follows. Players simultaneously and independently announce choices of desirable coalition structures, then the ﬁnal coalition structure is formed according to the rule above, and payoﬀs are assigned. The rule is not formalized for a shorter exposition.  

Players A and B would always like to be together, then with    $C_{1}$   or    $C_{2}$  . Being rational    $A$   and    $B$   would choose coalition structure with the highest payoﬀ, i.e. the strategy 1. The ﬁrst best choices of    $C_{1}$   and    $C_{2}$   is to have a dinner with    $A$  . However, A will never choose to be with either of them. Hence, non-realization of this option makes a potential loss for both    $C_{1}$   and  $C_{2}$  .  

Both players    $C_{1}$   and    $C_{2}$   are aware of this. Another common knowledge, that they both know about each other, is that if they make a coalition of two, each will be better oﬀ. This behavior meets sociological understanding of cooperation - to unite in order to prevent a loss, to which each is individually exposed to.  

A cooperation between    $C_{1}$   and    $C_{2}$   does not demolish the coalition    $\{A,B\}$  , but only reduces payoﬀs for it’s members. At the same time players A and B cannot prevent cooperation between    $C_{1}$   and    $C_{2}$   (or to insure against).  

On the other hand, if players A and B choose strategy 2 they will obtain coalition    $\{A,B\}$   in any case. In terms of mixed strategies this means that an equilibrium mixed strategy for    $A$   and for    $B$   is the whole probability space over two points, two coalition structures.  

From the forth column we can see that the corresponding cooperative game has an empty core. Strong Nash equilibrium cannot be applied here also. Coalition value approach also supports the idea of cooperation, but without an explicit allocation of payoﬀs. This means it ignores individual rationality and incentive compatibility to participate in a coalition. For ex- ample, how players    $C_{1}$   and    $C_{2}$   should divide the value of a joint coalition  $\{C_{1},C_{2}\}$   equal to 10?  

The constructed game has a unique equilibrium, which in terms of indi- vidual payoﬀs is characterized as the second-best eﬃcient for every player. There are two coalitions in the equilibrium coalition structure.  

# 2.2 Formal deﬁnition of cooperation  

This section formalizes an idea of cooperation presented in the example above. We demonstrate only one way for deﬁning cooperation, when it is intentional and complete.  

Deﬁnition 1  (complete cooperation in a coalition) .  In a game    $\Gamma(K)$   with an equilibrium    $\sigma^{*}(K)=(\sigma_{i}^{*})_{i\in N}$   a set of players    $g$  ,  completely cooperate in a coalition    $g$  ex ante if for every player    $i\in g$   there is  

ex ante  : for every  i  in    $g$  , a desirable coalition  g  always belongs to a chosen coalition structure, i.e such if    $s_{i}$   is chosen by    $i$  , then    $s_{i}\in S_{i}(P_{i})$  ,    $g\in$   $P_{i}$  , where    $P_{i}$   is a coalition structure chosen by    $i$  , however coalition structures chosen by diﬀerent players may be diﬀerent.  

ex post 1  : every realized coalition structure contains    $g$  , i.e.  $g\ \in\ \forall P^{*}$  , where    $P^{*}$  is a formed equilibrium partition of    $\Gamma(K)$  ,  

$E U_{i}^{\Gamma(K)}\Big(\sigma^{*}(K)\Big)\geq E U_{i}^{\Gamma(K)}\Big(\sigma_{i}^{*}(K),\sigma_{-i}^{*}(K)\Big),f o r\forall\sigma_{i}(K)\neq\sigma_{i}^{*}(K),$  

First of all, cooperation is deﬁned for a game  $\Gamma(K)$  . If a game changes due to a change in the number of deviators    $K$  , the cooperation may evaporate.  

Every player chooses a partition with the desirable coalition    $g$   with pos- itive probability. But individually chosen coalition structures by all players may be diﬀerent.  

After the game is over the coalition    $g$   always belongs to every ﬁnal equilib- rium coalition structure, disregard allocation of players over other coalitions. A ﬁnal partition may diﬀer from a chosen one, but in any case it will contain the desirable coalition.  

The deﬁned cooperation assumes agents are acting from self-interest mo- tivations. The lunch game example further expands the case, where there is imperfect cooperation.  

The dinner game example has the complete cooperation for players    $C_{1}$  and    $C_{2}$  . The deﬁnition does not exclude inter and intra-coalition interaction.  

If we relax some conditions of the deﬁnition we will obtain weaker conditions for cooperation. Cooperation in repeated games is of special interest and will be addressed in one of the next papers.  

# 3 Bayesian games  

In this section we demonstrate how intra-coalition externalities of the grand coalition may happen from equilibrium mixed strategies. In order to show that, a standard Battle of Sexes game is modiﬁed.  

Let there be two players, Ann and Bob. Each has two options: to be together with another or to be alone. In every option each can choose where to go: to Box or to Opera. Hence every player has four strategies. A set of strategies of the game leads to 16 outcomes. Every outcome consists of payoﬀproﬁle and a partition (or a coalition structure). Both players have preferences over coalition structures: they prefer to be together, then be separated.  

The rules of coalition structure formation mechanism are:  

1. If they both choose to be together, i.e. both choose the coalition struc- ture    $P_{j o i n t}=\{A n n,B o b\}$   then: (a) if both choose the same action for    $P_{j o i n t}$   (i.e. both choose Box or both choose Opera), then they go to where they both choose to go, (b) otherwise they do not go anywhere, but enjoy just being together;  

2. if at least one of them chooses to stay alone, i.e. chooses a parti- tion    $P_{s e p a r}\,=\,\{\{A n n\},\{B o b\}\}$  , then each goes alone to where she/he chooses, may be to diﬀerent Opera or diﬀerent Box performances.  

Table 2: Payoﬀfor the Bach-or-Stravinsky game. B is for Box, O is for Opera. If the players choose to be together, and it is realized due to the rule of coalition structure formation, then each obtains an additional ﬁxed payoﬀ  $\epsilon>0$  .  

<td><table  border="1"><thead><tr><td></td><td><b>BBob.Psepar</b></td><td><b>O Bob Paepar</b></td><td><b>BBob,Pioint</b></td><td><b>OBob,Pioint</b></td></tr></thead><tbody><tr><td>BAa, ear</td><td>(2; 1)*K=1 [{1], [2]]</td><td>(0;0) [{1], [2]]</td><td>(2;1) [{1], [2]]</td><td>(0;0) [{1], [2]]</td></tr><tr><td>O Am, Pepar</td><td>(0;0) [{1], [2]]</td><td>(1:2)*K=1 [(1], [2]]</td><td>(0;0) [[1], [2]]</td><td>(1;2) [[1], [2]]</td></tr><tr><td>BAr,Pont</td><td>(2;1) [[1], [2]]</td><td>(0;0) [{1], [2]]</td><td>(2 + e; 1 + e)*,K=2 [1, 2]</td><td>(e; e) [1, 2]</td></tr><tr><td>O An,Pjoint</td><td>(0;0) [(1], [2]]</td><td>(1;2) [(1], (2]]</td><td>(e; e) (1, 2]</td><td>(1 + c;2 + e)*.=2 [1, 2]</td></tr></tbody></table></td>  

Formally the rules are:  

${\mathcal{R}}(K=1)\colon S(K=1)\mapsto S(\{\{1\},\{2\}\}),$  ,  $\begin{array}{r l}&{\ddots\qquad\ddots\qquad\ddots\qquad\ddots\qquad\ddots}\\ &{\forall s\in S_{i}(K=1)=\{O_{A n n,P s e p a r},B_{A n n,P s e p a r}\}\times\{O_{B o b,P s e p a r},B_{B o b,P s e p a r}\}}\end{array}$  

and  

$$
\mathcal{R}(K=2)\colon S(K=2)\mapsto\left\{\begin{array}{l l}{S(\{1,2\}),}\\ {\mathrm{if~}s\in\{O_{A n n,P_{s e p a r}},B_{A n n,P_{s e p a r}}\}\times\{O_{B o b,P_{s e p a r}},B_{B o b,P_{s e p a r}}\},}\\ {S(K=2)\setminus S(\{1,2\}),\quad\mathrm{otherwise~}}\end{array}\right.
$$  

The whole Table 2 corresponds to the game with    $K=2$   where the game for    $K=1$   is a component. If Ann and Bob play the game with    $K=1$   with a single coalition structure    $\{\{A n n\},\{B o b\}\}$  , then the payoﬀs for this game are in the two-by-two top-left corner of Table 2. If Ann and Bob are together, then each obtains an additional payoﬀ  $\epsilon$  , and the corresponding cells make a two-by-two bottom-right corner.  

Every game with    $K=1$   and    $K=2$   has only one mixed strategies equi- librium and only one equilibrium partition. Mixed strategies equilibrium for  $K=1$   is described in every textbook. A change in    $K$   from    $K=1$   to    $K=2$  results in a changes of an equilibrium strategy proﬁle and an equilibrium partition.  

For    $K=2$   the game also has a mixed strategies equilibrium like for    $K=1$  . The diﬀerence is that now players have an allocation in a diﬀerent coalition structure in comparison to the case of    $K=1$  . Mixed strategies equilibrium for Ann is:    $\sigma^{*}(B_{A n n,P_{j o i n t}})=(1\!+\!\epsilon)/(3\!+\!2\epsilon)$  ,    $\sigma^{*}(O_{A n n,P_{j o i n t}})=(2\!+\!\epsilon)/(3\!+\!2\epsilon)$  ,  $i\in\{\mathrm{Ann},\mathrm{Prob}\}$  , what results in an equilibrium partition    $P_{j o i n t}$  , what is the grand coalition. And there is an equilibrium intra-coalition activity.  

The presented game allows to construct intra-coalition externalities from mixed strategies within one partition. Mixed intra-coalition externalities means that players are exposed to equilibrium ﬂuctuations from strategic actions of another player.  

A game as above can not be constructed within any cooperative game equilibrium concept. It is impossible to construct Shapley value (195) here even if there is one coalition: players have equilibrium mixed strategies inside it.  

# 4 Stochastic games  

Shapley (1953) deﬁned stochastic games as ” the play proceeds by steps from position to position, according to transition probabilities controlled jointly by the two player”. This section demonstrates how this type of games with coalition structures as states of a game may appear in the constructed game. The example diﬀers from example above as a set of the equilibrium mixed strategies induces more than one equilibrium coalition structure. We use a game, similar to corporate dinner game, but with identical players.  

# 4.1 Corporate lunch game  

There is a set of four identical players    $N\,=\,\{A,B,C,D\}$  . An individual strategy is a coalition structure, or an allocation of all players across tables during lunch. A coalition structure is an allocation of players over no more than four tables, where possibly empty tables do not matter. A rule of coalition formation is a unanimous agreement to form a coalition. If player chooses a coalition, but other members of the coalition did not choose him, the player eats alone.  

A player has preferences over coalition structures: she/he prefers to eat with someone and other players eat individually. If one eats alone he is hurt by a possible formed coalition of others. Coalition structures, and payoﬀ proﬁles for the highest cases payoﬀs are presented in Table 3:  

<td><table  border="1"><thead><tr><td><b>num</b></td><td><b>Coalition structure</b></td><td><b>Payoff profile UA, UB, Uc, UD</b></td><td><b>Coalition values as in cooperative game the</b></td></tr></thead><tbody><tr><td>1*</td><td>[A,B], [C],{D]: 0* = 0" = 1/3</td><td>(10,10,3,3)</td><td>20A,B, 3c, 3D</td></tr><tr><td>2*</td><td>(10,3,10,3)</td><td>20A,C, 3B, 3D</td></tr><tr><td>3*</td><td>[A, D],[C},{B): 0A = 0D = 1/3</td><td>(10,3,3,10)</td><td>20A,C, 3c, 3B</td></tr><tr><td>4</td><td>[A],B],[C,D]</td><td>(3,3,10,10)</td><td>3A, 3B, 29c,D</td></tr><tr><td>5</td><td>[A),{D), [C, B)</td><td>(3,10,10,3)</td><td>3A, 3B, 29c,D</td></tr><tr><td>6</td><td>{A),{C),{B, D)</td><td>(3,10,3,10)</td><td>3A, 3B, 29c,D</td></tr><tr><td>7</td><td>[A],{B),{C),{D)</td><td>(3,3,3,3)</td><td>3A, 3B, 3c, 3D</td></tr><tr><td>8</td><td>all other with K = 3, 4</td><td>(0,0,0,0)</td></tr></tbody></table></td>  

Payoﬀs in Table 3 are organized in the way that formation of a coalition by other players deteriorates payoﬀs for the rest. Formation of two 2-player coalitions does not improve payoﬀs for every player. Outcomes of the game are coalition structures or states of a stochastic game. An increase of    $K=2$  to    $K\,=\,3,4$   does not change an equilibrium in mixed strategies, hence we can speak about robustness of an equilibrium for    $K=2$   to an increase in K.  

It is clear that the game does not have an equilibrium in pure strategies. This is a Bayesian game, with a probability distribution of equilibrium mixed strategies. Equilibrium mixed strategies are indicated only for player A in the ﬁrst three lines of the Table 3.  

# 4.2 A formal deﬁnition of a stochastic game of coali- tion structure formation  

Let   $\Gamma(K)$   be a non-cooperative game as deﬁned above.  

Deﬁnition 2.  A game    $\Gamma(K)$   is a stochastic game if a set of equilibrium par- titions is bigger than two,    $\#(\{P^{*}\}(K))\geq2$  , where a state is an equilibrium partition    $P^{*}\in\{P^{*}\}(K)$  .  

Studying properties of stochastic games with non-cooperative coalition structure formation are left for future.  

In the same way we can construct a family of stochastic games, what is left for future.  

# 5 No self-enforcement of an equilibrium and non-cooperative criterion for stability  

Aumann (1990) used ”stag and hare” game to demonstrate absence of a self- enforcement property of Nash equilibrium. We use an extended version of the same game to demonstrate how by modifying the game we can reach a focal point of the game, unavailable within standard Nash equilibrium. Then we construct a non-cooperative coalition structure stability criteria.  

There are two hunters    $i\,=\,1,2$  . If players can hunt only individually, then    $K=1$  , and the only partition is    $P_{s e p a r}\,=\,\{\{1\},\{2\}\}$  . An individual strategy set of    $i$   is  $S_{i}(K=1)=\Bigl((P_{s e p a r},h a r e),(P_{s e p a r},s t a g)\Bigl)$  . For example, a strategy    $s_{i}=(P_{s e p a r},h a r e)$   is interpreted as player    $i$   chooses to hunt alone for a hare.  

A set of a corresponding strategies for the game with    $K=1$   is    $S(K=$   $1)=S_{1}(K=1)\times S_{1}(K=1)$  .  

For a game with    $K=2$   every hunter can choose either to hunt alone, in a coalition structure    $P_{s e p a r}\,=\,\{\{1\},\{2\}\}$  , or together,    $P_{j o i n t}\,=\,\{1,2\}$  . For every hunting partition a player chooses a target for hunting: a hare or a stag, as in the game for    $K=1$  . A set of strategies of    $i$   is  

$$
S_{i}(K=2)=\Bigl((P_{s e p a r},h a r e),(P_{s e p a r},s t a g),(P_{j o i n t},h a r e),(P_{j o i n t},s t a g)\Bigr),
$$  

where a strategy consists of two terms. A set of strategies of the game is a direct ( Cartesian) product,    $S(K=2)=S_{1}(K=2)\times S_{2}(K=2)$  .  

We do not rewrite the rules for coalition structure formation, as they are the same as in the BoS game above. The diﬀerence is a renaming of strategies.  

Every player knows, which game is played, either with    $K=1$   or with  $K=2$  . A case with uncertainty in parameter    $K$   is not addressed here and left for the future.  

We assume that there is a unanimous coalition formation rule, i.e. hunters can hunt together only if both choose to be together. However even if they both choose to hunt together, they may have a disagreement for whom to hunt. Payoﬀs for the both games   $\Gamma(K=1)$   and   $\Gamma(K=2)$   are presented in Table 4.  

If hunters play a game with    $K=1$   then a maximum achievable payoﬀis  $(8,8)$  , when each hunts individually for a hare. An an equilibrium strategy proﬁle is  $\Big((P_{s e p a r},h a r e),(P_{s e p a r},h a r e)\Big)$  . In the game   $\Gamma(K=1)$   the players can not reach the eﬃcient outcome (100 ,  100) of the game   $\Gamma(K=2)$  , when both hunt for a stag together. This focal point (in terminology of Schelling) can be reached only within the game   $\Gamma(K\,=\,2)$  . Thus the focal point is feasible in the game   $\Gamma(K=2)$  , but not in the game   $\Gamma(K=1)$  .  

Self-enforcing property of the equilibrium is that both players realize in- dividual gain from a change of a game from    $K=1$   to    $K=2$   and neither can deviate. But players can not reach the outcome (100; 100) without a change in a game.  

In literature a self-enforcement property of an equilibrium is not well- deﬁned, but intuitively it depends on what players think about willings of many others to deviate from an equilibrium.  

<td><table  border="1"><thead><tr><td></td><td><b>Psepar, hare</b></td><td><b>Psepar, stag</b></td><td><b>Pjoint,hare</b></td><td><b>Pjoint, stag</b></td></tr></thead><tbody><tr><td>Psepar,hare Psepar, stag</td><td>(8;8); {{1],[2]] (0;8); {{1],[2]]</td><td>(8;0); {{1],[2]] (0;0); {1],[2]]</td><td>(8;8);{[1], [2]] (0;8); {{1], [2]]</td><td>(8;0); {{1],{2]] (0;0); {{[1], [2]]</td></tr><tr><td>Psepar, stag</td><td>(0;8); {{1],[2]]</td><td>(0;0); {1],[2]]</td><td>(0;8); {{1], [2]]</td><td>(0;0); {{[1], [2]]</td></tr><tr><td>Pjoint, hare</td><td>(8;8); [{1], [2]]</td><td>(8;0); {[1],[2]]</td><td>(4;4); [1, 2]</td><td>(8;0); [1, 2]</td></tr><tr><td>Pjoint, stag</td><td>(0;8); {{1],[2]]</td><td>(0;0) ;{{1],[2]]</td><td>(0;8);{1, 2]</td><td>(100; 100)*; {1, 2}</td></tr></tbody></table></td>  

If there is an uncertainty, which game is played, either   $\Gamma(K\,=\,1)$   or  $\Gamma(K=2)$  , then players will randomize between two strategies:    $P_{s e p a r}$  , hare and    $P_{j o i n t},s t a g$  . In this case the game becomes a stochastic game as described above.  

# 5.1 Criterion of coalition structure (a partition) sta- bility  

There is a nested family of games  

$$
\Gamma=\{\Gamma(K=1),.\ldots,\Gamma(K),.\ldots\Gamma(K=N)\}\colon\Gamma(K=1)\subset\Gamma(K)\subset\Gamma(K=N).
$$  

It is characterized by list of equilibrium strategy proﬁles,  

$$
{\Big(}\sigma^{*}(1),.\,.\,.\,,\sigma^{*}(K),.\,.\,.\,,\sigma^{*}(K=N){\Big)},
$$  

where    $\sigma^{*}(K)=(\sigma_{i}^{*}(K))_{i\in N}$   and by a list of equilibrium partitions  

$$
\Bigl(\{P^{*}\}(1),.\,.\,,\{P^{*}\}(K),.\,.\,,\{P^{*}\}(K=N)\Bigr),
$$  

$\{P^{*}\}(K)\subset{\mathcal{P}}(K)$  . Every game   $\Gamma(K)$   from a family   $\Gamma$   has an equilibrium may be in mixed strategies.  

The family of games has an equilibrium expected payoﬀproﬁles:  

$$
\Big((E U_{i}^{\Gamma(1)})_{i\in N}^{*},.\,.\,,(E U_{i}^{\Gamma(K)})_{i\in N}^{*},.\,.\,,(E U_{i}^{\Gamma(K=N)})_{i\in N}^{*}\Big),
$$  

where   $(E U_{i}^{\Gamma(K)})_{i\in N}^{*}\equiv(E U_{i}^{\Gamma(K)}(\sigma^{*}))_{i\in N}$  .  

Let us take a game   $\Gamma(K_{0})\;\in\;\Gamma$   with    $\sigma^{*}(K_{0})$   as an equilibrium mixed strategy set. The question is: what is a condition when an equilibrium strategy proﬁle does not change with an increase in a maximum coalition size    $K_{0}$  ? We can do this by comparing expected utility for all players from diﬀerent games:   $\Gamma(K_{0}),.\,.\,.\,,\Gamma(K=N)$  .  

The criterion is based on the fact that a set of mixed strategies should not change with an increase in a variety of available coalition structures. The criterium is a suﬃcient criterium and deﬁnes a maximum coalition size, when an equilibrium for smaller coalition sizes still holds true.  

Deﬁnition 3.  Partition stability criterion  for a game    $\Gamma(K_{0})$   is a maxi- mum coalition size    $K^{*}$  when an equilibrium still holds true, i.e. for all    $i\in N$  there is a maximum number    $K^{*}$  such that  

1.  

$$
K^{*}=\operatorname*{max}_{\stackrel{K=K_{0},\ldots,N}{\Gamma(K_{0}),\ldots,\Gamma(K=N)}}\Big\{E U_{i}^{\Gamma(K_{0})}\Big(\sigma_{i}^{*}(K_{0}),\sigma_{-i}^{*}(K_{0})\Big)\geq E U_{i}^{\Gamma(K)}\Big(\sigma_{i}^{*}(K),\sigma_{-i}^{*}(K)\Big)\Big\},
$$  

2.  Dom   $\sigma^{*}(K^{*})=D o m~\sigma^{*}(K_{0})$  

where    $\sigma^{*}(K_{0})$   is an equilibrium in the game    $\Gamma(K_{0})$  ,    $\sigma^{*}(K)$   is an equilibrium in a game    $\Gamma(K)$  ,    $K=K_{0},.\,.\,.\,,N$  , and  Dom  is a domain of equilibrium mixed strategies set.  

The deﬁnition is operational, it can be constructed directly from a deﬁni- tion of a family of games. This deﬁnition guarantees stability of both payoﬀs and partition, and is a suﬃcient criterion of stability. Some applications may require weaker forms of the criterion.  

Now it is clear that the statement of Aumann (1990) that Nash equilib- rium is generally not self-enforcing is correct. In the extended version of stag and hare game we have seen that an increase in    $K$   changed an equilibrium. The same took place in a variation of Battle of Sexes game. However this did not happen in the Corporate Dinner or the Corporate Lunch game.  

The proposed criterion may serve as a measure of trust to an equilibrium or as a test for self-enforcing of an equilibrium. This criterion can be applied to study opportunistic behavior in coalition partitions. If players in a coali- tion    $g$   in a game   $\Gamma(K_{1})$   have perfect cooperation, this does not mean that in a wider game   $\Gamma(K_{2})$  ,    $K_{1}<K_{2}$  , they will still cooperate.  

# 6 Discussion  

The current paper demonstrates how some standard non-cooperative games can be constructed from the game oﬀered by Levando (2016), i.e. by in- cluding coalition structures into consideration. The proposed detail for a deﬁnition of a non-cooperative game improves interpret ability of results and wides applications for non-cooperative games. Using the example, the paper oﬀers a way to construct cooperation in coalition formation on self-interest fundamentals. The paper oﬀers also a non-cooperative criterion to measure stability of coalition structures using a deﬁnition of a non-cooperated games from a nested family.  

The two accompanying papers demonstrate applications of the same model to network games (a generalization of Myerson, 1977) and to simple repeated games.  

# References  

[1] Aumann, R., 1959. Acceptable points in general cooperative n-person games. Contributions to the theory of games. Annals of mathematic stud- ies, no. 40, Vol. IV, Princeton University Press, Princeton, NJ.

 [2] Aumann R., 1990. Nash equilibria are not self-enforcing. Economic Deci- sion Making: Games, Econometrics and Optimization, 201-206

 [3] Harsanyi, John C. ”Games with incomplete information played by Bayesian players, iiii: part i. the basic model.” Management science 50 (2004): 1804-1817.

 [4] Levando, D., 2016. Formation of coalition structures as a non-cooperative game 1: theory. mimeo.

 [5] Myerson, R. B., 1977. Graphs and Cooperation in Games. Mathematics of Operations Research 2, 225-229.

 [6] Nash, J. F., 1950. Equilibrium points in n-person games. Proceedings of the National Academy of Sciences, USA 36, 48-49.

 [7] Nash, J.F., 1951. Non-cooperative games. Annals of Mathematics 54, 286-295

 [8] Shapley, Lloyd S. ”Stochastic games.” Proceedings of the national academy of sciences 39.10 (1953): 1095-1100. APA  