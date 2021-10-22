// [Nyveon]
// Tarea 1 Ejercicio 1
// A - Hoax or what

using namespace std;
#include <iostream>
#include <set>


int main() {

    // Cases
    int n;
    while (cin >> n) {
        multiset<int> urn;
        long long total_spent;
        total_spent = 0;

        // End case (n = 0)
        if (n == 0) {
            break;
        }

        // Input
        // Days in a case
        for (int i = 0; i < n; i++) {

            int k;
            cin >> k;


            // Bills in a day
            for (int j = 0; j < k; j++) {
                int val;
                cin >> val;
                urn.insert(val);
            }

            auto smallest = urn.begin();
            auto largest = urn.end();
            largest--;

            total_spent += (*largest) - (*smallest);

            urn.erase(smallest);
            urn.erase(largest);

            //largest = *(urn.rbegin()); // PORQUE PUNTEROS PORQUEEE
            //largest = *(urn.end());

            //total_spent += largest - smallest;
            //urn.erase(smallest);
            //urn.erase(largest);
        }



        // Output
        cout << total_spent << endl;


    }

    return 0;
}