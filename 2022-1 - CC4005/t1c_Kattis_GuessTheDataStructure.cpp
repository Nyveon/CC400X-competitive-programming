// Nyveon (Eric K)
// T1 CC4005
// Problem C - Adivina la estructura
// [!]
// DISCLAIMER: esto es mi mismo código del semestre pasado, donde también se hizo este problema.
// ver: https://github.com/Nyveon/CC400X-competitive-programming
// [!]

using namespace std;
#include <iostream>
#include <stack>
#include <queue>

int main() {

    int n;
    while (cin >> n) {

        // Simulation data structures
        stack<int> simulation_stack;
        queue<int> simulation_queue;
        priority_queue<int> simulation_priority_queue;

        // Data structure validity bits
        int valid = 1 + 2 + 4; // 1s: stack, 2s: queue, 4:s pqueue
        // 111
        // pq, queue, stack

        // Run simulation
        while (n--) {
            int instruction, value;
            cin >> instruction >> value;

            switch (instruction) {
                case 1: // Throw element into the bag
                    simulation_stack.push(value);
                    simulation_queue.push(value);
                    simulation_priority_queue.push(value);
                    break;
                case 2: // Take an element out of the bag
                    if (!simulation_stack.empty()) {
                        int a, b, c;
                        a = simulation_stack.top();
                        simulation_stack.pop();

                        if (a != value) {
                            valid = valid & 0 + 2 + 4; // Mask out stack
                        }

                        b = simulation_queue.front();
                        simulation_queue.pop();

                        if (b != value) {
                            valid = valid & 1 + 0 + 4; // Mask out queue
                        }

                        c = simulation_priority_queue.top();
                        simulation_priority_queue.pop();

                        if (c != value) {
                            valid = valid & 1 + 2 + 0; // Mask out pqueue
                        }
                    } else { // edge case where it tries to do an illegal operation
                        valid = 0;
                    }
                    break;
            }
        }

        // Output
        // si, se que esto es feo, pero funciona xd
        switch (valid) {
            case 0 + 0 + 0:
                cout << "impossible" << endl;
                break;
            case 1 + 0 + 0:
                cout << "stack" << endl;
                break;
            case 1 + 2 + 0:
                cout << "not sure" << endl;
                break;
            case 0 + 2 + 0:
                cout << "queue" << endl;
                break;
            case 1 + 0 + 4:
                cout << "not sure" << endl;
                break;
            case 0 + 0 + 4:
                cout << "priority queue" << endl;
                break;
            case 1 + 2 + 4:
                cout << "not sure" << endl;
                break;
            case 0 + 2 + 4:
                cout << "not sure" << endl;
                break;
        }
    }

    return 0;
}