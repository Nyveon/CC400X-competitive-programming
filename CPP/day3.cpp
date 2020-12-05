#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

// Nyveon
// Advent of code 2020
// Day 3

// Debugging function for displaying a line of a slope
void display_slope(int xpos, int ypos, char map[323][32]) {
    for (int i = 0; i < 31; i++) {
        if (i != xpos) {
            cout << map[ypos][i];
        } else {
            if (map[xpos][ypos] == '#') {
                cout << 'X';
            } else {
                cout << 'O';
            }
        }
    } cout << endl;
}

// Function for counting trees on slope
int slope(int xspeed, int yspeed, char map[323][32]) {
    int xpos = 0;
    int ypos = 0;
    int tree_count = 0;
    while (ypos < 323) {
        if (map[ypos][xpos] == '#') {
            tree_count++;
        }
        xpos += xspeed;
        ypos += yspeed;
        xpos = xpos % 31;
    }
    return tree_count;
}


int main() {

    // Variables
    char map[323][32];
    char ch;
    int i = 0;
    int j = 0;

    // Input
    ifstream input_file ("../day3_input.txt");
    while (input_file >> ch) {
        map[i][j] = ch;
        j++;
        if (j == 31) {
            i++;
            j = 0;
        }
    }

    // -- Parts 1 and 2 --
    int a = slope(1, 1, map);
    int b = slope(3, 1, map); // Part 1
    int c = slope(5, 1, map);
    int d = slope(7, 1, map);
    int e = slope(1, 2, map);
    long long ans = (long long)a * b * c * d * e; // Part 2

    // Output
    cout << "Part 1: " << b << "\n";
    cout << "Part 2: " << ans << "\n";
    return 0;

}
