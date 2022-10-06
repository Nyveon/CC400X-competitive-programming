# Promotions

## Problem

Restaurant Rex has a system of levels for their chefs. Each chef falls into one of 3 levels according to their wages. Level 1 chefs have wages in the range of [0, 10^6) balabizos per hour, Level 2 chefs have wages in the range of [10^6, 2\*10^6) balabizos per hour and Level 3 [2*10^6 ,infinity) balabizos per hour. Every few months, there is a percentage increase or decrease in the wages depending on the level, where higher levels have their percentage greater than or equal to lower levels.

Note: If a Level 1 employee's wage becomes in the range of level 2 after the increase, then they get promoted to that level. The same applies for Level 2 getting promoted to 3. The opposite also applies for the decrease (ex. a level 3 employee could become a level 2 or 1 employee after a decrease).

Given the start wages of all employees and the wage increases at each level, output the current wages of certain employees after all previous increases.

## Constraints

- 1 ≤ t ≤ 50
- 1 ≤ n ≤ 50000
- 1 ≤ q ≤ 1000000
- 1 ≤ wi ≤ 4000000
- wi ≤ wi+1
- -80 ≤ p ≤ 100
- 1 ≤ r ≤ 8
- 1 ≤ e ≤ n

## Input

Input starts with a line containing t, the number of test cases then t test cases will follow. Each test case starts with n q where n is the number of employees and q is the number of queries that follow,
Second line of each test case's input contains w1 w2 w3 … wn separated by spaces where wi is the wage of the employee with employee id of i at time 0.
q lines follows each in one of the following format:
1 p1 p2 p3 e r,where p1 ≤ p2 ≤ p3 and pi is the percentage of wage increase of level i, e is the employee id and r is the number of times this query happened.
2 e1 e2 this asks for the sum of the wages of employees with employee id between e1 and e2 both inclusive

## Output

For each test case, for each query
if it starts with 1, output a line for each occurrence of the query stating the wage of the employee with id e after that increase
if it starts with 2, output a line containing the answer to the query.
The output should be a rational number, with exactly six decimal points of precision (no more, no less), padding or rounding as necessary
Notes:
Each line of input is a point in time in increasing order and they are dependent on each other.
Rex can not afford to pay more than 10^18 balabizos in wages, so the total sum of wages ≤ 10^18
In queries of type 1, you only need to print the value for employee with ID *e*, but all employees will have their salary increased/decreased

Sample Input

```text
5
8 1
1662293 1725370 2997840 3253006 3776933 3986536 3992353 3998699
1 -71 -62 3 2 8
10 8
1818833 2245485 2547920 2564630 2679082 3505807 3792425 3874382 3946714 3993148
1 -75 -24 21 2 1
2 3 5
2 3 3
1 5 18 52 1 7
2 9 10
2 8 8
2 6 10
2 5 10
8 5
1069913 2255999 2256002 2333259 2542802 3514268 3914337 3993353
1 -67 7 42 4 6
1 29 42 62 7 5
2 8 8
2 4 4
1 -69 43 65 8 7
2 2
1689379 3431002
1 15 90 92 1 1
2 2 2
7 2
815382 1262582 1314261 3409111 3713153 3921918 3944840
1 89 92 97 3 5
1 -17 -6 72 4 7
```

Sample Output

```text
655640.600000
190135.774000
55139.374460
15990.418593
4637.221392
1344.794204
389.990319
113.097193
2717036.850000
9427874.720000
3082983.200000
1631129.434400
1924732.732592
2271184.624459
3452200.629177
5247344.956349
7975964.333651
12123465.787149
180095739.999093
87880581.970967
433518304.025296
494286520.816501
3313227.780000
4704783.447600
6680792.495592
9486725.343741
13471149.988112
19129032.983119
51988021.972557
84220595.595543
136437364.864780
221028531.080943
358066220.351128
365294254.234584
213436204.197608
602735519.487063
994513607.153654
1640947451.803530
2707563295.475823
4467479437.535109
7371341071.932929
12162712768.689333
3209820.100000
6587523.840000
2523381.120000
4971060.806400
9792989.788608
19292189.883558
38005614.070609
173980558.126894
299246559.978257
514704083.162602
885291023.039676
1522700559.628242
2619044962.560576
4504757335.604192
```
