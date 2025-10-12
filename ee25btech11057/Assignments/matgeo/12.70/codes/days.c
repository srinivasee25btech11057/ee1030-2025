#include <stdio.h>

double days_for_bullocks_alone(double X, double Y) {
    // From equations:
    // 8*(X*b + Y*t) = 1
    // 5*((X/2)*b + 2*Y*t) = 1
    // Solve for b, t symbolically and return 1/(X*b)
    double a1 = 8 * X;
    double b1 = 8 * Y;
    double c1 = 1;

    double a2 = 5 * (X / 2.0);
    double b2 = 5 * (2.0 * Y);
    double c2 = 1;

    // Expressing equations in rate form:
    // (a1/a1)*b + (b1/a1)*t = c1/a1
    // (a2/a1)*b + (b2/a1)*t = c2/a1

    double det = a1 * b2 - a2 * b1;
    double b_rate = (c1 * b2 - c2 * b1) / det;
    double t_rate = (a1 * c2 - a2 * c1) / det;

    // time for X bullocks alone = 1 / (X * b_rate)
    double T = 1.0 / (X * b_rate);
    return T;
}

int main() {
    double X, Y;
    printf("Enter number of bullocks (X): ");
    scanf("%lf", &X);
    printf("Enter number of tractors (Y): ");
    scanf("%lf", &Y);

    double T = days_for_bullocks_alone(X, Y);
    printf("Days taken by %g bullocks alone = %.2f days\n", X, T);

    return 0;
}

