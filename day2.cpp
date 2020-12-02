#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

// Nyveon
// Advent of code 2020

int main() {

    // Variables
    string passwords[1000];
    char characters[1000];
    int min_char[1000], max_char[1000];
    char char_dump;

    // -- Input --
    ifstream input_file ("../day2_input.txt");
    int i = 0;
    while (input_file >> min_char[i]) {
        input_file >> char_dump >> max_char[i] >> characters[i] >> char_dump >> passwords[i];
        i++;
    }

    // -- Part 1 --
    int valid_passwords = 0;
    for (int i = 0; i < 1000; i++) {
        int char_count = count(passwords[i].begin(), passwords[i].end(), characters[i]);
        valid_passwords += (char_count <= max_char[i] && char_count >= min_char[i]);
    }
    cout << "Part 1: " << valid_passwords << "\n";

    // -- Part 2 --
    valid_passwords = 0;
    for (int i = 0; i < 1000; i++) {
        valid_passwords += ((passwords[i][max_char[i] - 1] == characters[i]) ^ (passwords[i][min_char[i] - 1] == characters[i]));
    }
    cout << "Part 2: " << valid_passwords << "\n";

    return 0;
}