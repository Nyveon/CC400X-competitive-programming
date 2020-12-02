#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

// Nyveon
// Advent of code 2020

int main() {

    // Input
    string passwords[1000];
    char characters[1000];
    int min_char[1000];
    int max_char[1000];

    ifstream input_file ("../day2_input.txt");
    char char_dump;
    char line_char;
    string line;

    int i = 0;
    while (input_file >> min_char[i]) {
        input_file >> char_dump >> max_char[i] >> characters[i] >> char_dump >> passwords[i];
        i++;
    }

    // -- Part 1 --
    int valid_passwords = 0;
    for (int i = 0; i < 1000; i++) {
        //string password = passwords[i];
        int char_count = count(passwords[i].begin(), passwords[i].end(), characters[i]);

        if (char_count <= max_char[i] && char_count >= min_char[i]) {
            valid_passwords++;
        }
    }
    // Output
    cout << "Part 1: " << valid_passwords << "\n";


    // -- Part 2 --
    valid_passwords = 0;
    for (int i = 0; i < 1000; i++) {
        if ((passwords[i][max_char[i]-1] == characters[i]) ^ (passwords[i][min_char[i]-1] == characters[i])) {
            valid_passwords++;
        }
    }
    // Output
    cout << "Part 2: " << valid_passwords << "\n";



    return 0;
}