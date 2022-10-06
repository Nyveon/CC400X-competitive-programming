// Eric K.
// Meta Global Hackathon 2022
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

// g++ meta6.cpp && ./a.out < ti.txt > out.txt

// Returns the corre4sponding chef level
long long get_level(long double x) {
    if (x < 1000000) {
        return 1;
    } else if (x < 2000000) {
        return 2;
    } else {
        return 3;
    }
}

// Formats the output, long long double to string
string format(long double x) {
    return to_string(x);
}

int main() {
    // 1 <= t <= 50
    long long t;
    cin >> t;

    while (t--) {
        // Test cases
        // 1 <= n <= 50000
        // 1 <= q <= 1000000
        // 1 <= wi <= 4000000
        long long n, q;
        long double wages[50001];
        cin >> n >> q;
        for (long long i = 0; i < n; i++) {
            cin >> wages[i];
        }
        cout << t << endl;

        while (q--) { // Queries
            long long query_type;
            cin >> query_type;
            if (query_type == 1) {
                // Update
                // -80 <= pi <= 100
                // 1 <= e <= 50000
                // 1 <= r <= 8
                long double p1, p2, p3, p; long long e, r;
                cin >> p1 >> p2 >> p3 >> e >> r; e--;
                //cout << p1 << " " << p2 << " " << p3 << " " << e << " " << r << endl;
                for (long long i = 0; i < r; i++) {
                    for (long long j = 0; j < n; j++) {
                        switch (get_level(wages[j])) {
                            case 1: p = p1; break;
                            case 2: p = p2; break;
                            case 3: p = p3; break;
                        }
                        //wages[j] *= 1.0 + p/100.0;
                        //wages[j] *= p/100.0 + 1.0;
                        //wages[j] *= (100.0 + p)/100.0;
                        //wages[j] *= (p + 100.0)/100.0;

                        //wages[j] += (wages[j] * p)/100.0;
                        //wages[j] += (wages[j] / 100.0) * p;
                        //wages[j] += wages[j] * (p / 100.0);
                        //wages[j] += wages[j] * p / 100.0;

                        // Order of operations to Minimize floating polong long error
                        wages[j] = wages[j] * (p / 100.0 + 1.0);
                    }

                    string s = format(wages[e]);
                    cout << s << endl;
                }
            } else if (query_type == 2) {
                // Query
                // 1 <= ei <= 50000
                // 1 <= total <= 10^18
                long long e1, e2; cin >> e1 >> e2; e1--; e2--;

                long double total = 0;
                for (long long i = e1; i <= e2; i++) {
                    total += wages[i];
                }

                string s = format(total);
                cout << s << endl;
            }
        }
    }
}