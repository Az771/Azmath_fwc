#include <stdio.h>
#include <stdbool.h> // For using 'bool' type

// Function to calculate the boolean expression
// f(P,Q,R) = PQ + QR' + PR'
bool calculate_function(bool P, bool Q, bool R) {
    return (P && Q) || (Q && !R) || (P && !R);
}

int main() {
    printf("Truth Table for f(P,Q,R) = PQ + QR' + PR'\n");
    printf("---------------------------------------\n");
    printf("P | Q | R | f(P,Q,R)\n");
    printf("---------------------------------------\n");

    // Iterate through all 8 possible combinations of P, Q, R
    for (int p_val = 0; p_val <= 1; p_val++) {
        for (int q_val = 0; q_val <= 1; q_val++) {
            for (int r_val = 0; r_val <= 1; r_val++) {
                bool P = (bool)p_val;
                bool Q = (bool)q_val;
                bool R = (bool)r_val;

                bool result = calculate_function(P, Q, R);

                printf("%d | %d | %d | %d\n", P, Q, R, result);
            }
        }
    }

    return 0;
}
