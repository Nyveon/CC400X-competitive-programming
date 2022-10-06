# Rollercoasters

## Problem

You are planning a visit to an amusement park with three friends and need to decide which rollercoasters you want to go on. The park is a big crowded place, so they insist you visit the rollercoasters in the order laid out on the map.
Each of your friends has their own special way of picking which amusements they would like to visit, it's your job to help them figure out how much fun they are going to have at the amusement park, based on their respective strategies.
Your friend, Bob wants each rollercoaster he goes on to be strictly scarier than the previous he went on and he doesn't want to travel far between rollercoasters he goes on.
In particular, Bob must visit rollercoasters in the same relative order that they appear on the map, and if he chooses to go on a certain rollercoaster, then the next one he goes on (if any) must be the immediately following one. For example, he may choose to go on the 3rd and 4th rollercoasters, or on the 3rd, 4th, and 5th rollercoasters, but not on just the 3rd and 5th rollercoasters.
Like Alice, Bob has 10 units of fun for each rollercoaster he goes on, and he wants to maximize the amount of fun he has.
Your input is a file with K lines. The ith line contains a single integer representing the scariness of the ith rollercoaster. The rollercoasters are given in the order in which they appear on the amusement park map.
Output a single integer, the maximum amount of fun which Bob can have on the trip.

## Constraints

1 ≤ K ≤ 10,000

## Sample Explanation

In this example, Bob can visit at most 2 rollercoasters and still have fun (so he can have at most 20 units of fun). This could be either by visiting the first and then the second rollercoaster (Scariness 1 and then 2), or the third and then the fourth (Scariness 1 and then 3).

Sample Input

```text
1
2
1
3
````

Sample Output

```text
20
```
