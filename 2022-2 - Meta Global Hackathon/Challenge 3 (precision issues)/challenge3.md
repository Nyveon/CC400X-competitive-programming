# Wanikani

## Problem

Wanikani is an online tool for learning kanji, Chinese characters that are used in Japanese. Each kanji has a reading\* (how it's pronounced) and a meaning.
A review session in which you review N kanji actually has 2*N questions, as you're tested on the reading and meaning separately. In the corner of the screen is a counter that tracks the number of kanji for which you've finished reviewing both the meaning and reading, but nowhere does it tell you how many questions you have left.
You're currently partway through a review and the counter says K. You don't remember how many questions you've answered so far, but you'd like to know how many remain. What's the expected number of questions left in this review session, assuming that all questions come in a uniformly random order?

## Constraints

- 10 ≤ T ≤ 20
- 1 ≤ N ≤ 5000
- 0 ≤ K < N

## Input

Your input file starts with a non-negative integer T, the number of review sessions.
T lines will follow, each line contains two non-negative integers N, K representing the total amount of kanji and the number of kanji you have finished reviewing.

## Output

For each test case, for each query
The number of expected questions remaining in this review session. Absolute and relative errors of up to 10^-6 will be ignored.

## Explanation of Sample

In the first session having 1 kanji and a counter of 0 means either zero or one questions have been asked so far which means there could be 2 or 1 questions left, this gives us a expected value of

- 2 \* 0.5 + 1 * 0.5 = 1.5
- 2 ∗ 0.5+1 ∗ 0.5=1.5

\*Most kanji have many readings, but Wanikani mercifully teaches just the most important one.

Sample Input

```text
1 0
2 0
2 1
```

Sample Output

```text
1.500000
3.125000
1.250000
```
