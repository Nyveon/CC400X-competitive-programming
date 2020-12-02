#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// Nyveon
// Advent of code 2020

int main() {

    // Input
    ifstream input_file ("../day1_input.txt");
    int a[200];
    int line;
    int i = 0;
    while (input_file >> line) {
        a[i] = line;
        i++;
    }

    // -- Part 1 --
    // O(n^2), not bad for this input size really
    for (int i = 0; i < 200; i++) {
        for (int j = 0; j < 200; j++) {
            if (a[i] + a[j] == 2020) {
                // Output
                cout << a[i] * a[j] << "\n";
                goto superbreak;
            }
        }
    }

    superbreak:;

    // -- Part 2 --
    // O(n^3), not too good,but still manageable xd
    for (int i = 0; i < 200; i++) {
        for (int j = 0; j < 200; j++) {
            for (int k = 0; k < 200; k++) {
                if (a[i] + a[j] + a[k] == 2020) {
                    // Output
                    cout << a[i] * a[j] * a[k] << "\n";
                    return 0;
                }
            }
        }
    }

    return 0;
}
