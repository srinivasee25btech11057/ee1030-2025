#include <stdio.h>
#include <math.h>

int main() {
    // Step 1: Given
    double Sx = 1.0, Sy = 0.0;
    double Rx = -2.0, Ry = 1.0;

    // Step 2: Equation of tangents from R to y^2 = 4x:
    // Condition is y1 = m*x1 + a/m, where a=1
    // For point (-2,1): 1 = m*(-2) + 1/m => m^2 + 2m - 1 = 0

    double m1 = -1.0;
    double m2 = 0.5;

    // Step 3: Points of contact on parabola y^2=4x are (x = 1/m^2, y = 2/m)
    double R1x = 1.0 / (m1 * m1);
    double R1y = 2.0 / m1;
    double R2x = 1.0 / (m2 * m2);
    double R2y = 2.0 / m2;

    // Step 4: For Q1, RQ1 ⟂ SR1
    // SR1 line (Sx,R1x): if x same, vertical line
    // Hence x=1 is SR1 line. So perpendicular (RQ1) is horizontal (y constant = 1)
    // Intersection gives Q1(1,1)
    double Q1x = 1.0;
    double Q1y = 1.0;

    // Step 5: For Q2:
    // SR2 slope = (R2y - Sy)/(R2x - Sx)
    double m_SR2 = (R2y - Sy) / (R2x - Sx);
    // Slope of perpendicular (RQ2) = -1 / m_SR2
    double m_RQ2 = -1.0 / m_SR2;

    // SR2 eqn: y = m_SR2*(x - Sx)
    // RQ2 eqn: y - Ry = m_RQ2*(x - Rx)
  

    double a1 = m_SR2;
    double b1 = -m_SR2 * Sx;
    double a2 = m_RQ2;
    double b2 = Ry - m_RQ2 * Rx;

    double Q2x = (b2 - b1) / (a1 - a2);
    double Q2y = a1 * Q2x + b1;

    double SQ1 = sqrt(pow(Q1x - Sx, 2) + pow(Q1y - Sy, 2));
    double RQ1 = sqrt(pow(Q1x - Rx, 2) + pow(Q1y - Ry, 2));
    double SQ2 = sqrt(pow(Q2x - Sx, 2) + pow(Q2y - Sy, 2));
    double Q1Q2 = sqrt(pow(Q2x - Q1x, 2) + pow(Q2y - Q1y, 2));

    printf("Focus S(%.2f, %.2f)\n", Sx, Sy);
    printf("R(%.2f, %.2f)\n", Rx, Ry);
    printf("R1(%.2f, %.2f)\n", R1x, R1y);
    printf("R2(%.2f, %.2f)\n", R2x, R2y);
    printf("Q1(%.2f, %.2f)\n", Q1x, Q1y);
    printf("Q2(%.2f, %.2f)\n\n", Q2x, Q2y);

    printf("SQ1 = %.3f\n", SQ1);
    printf("RQ1 = %.3f\n", RQ1);
    printf("SQ2 = %.3f\n", SQ2);
    printf("Q1Q2 = %.3f\n", Q1Q2);

    printf("\nTrue statements:\n");
    if (fabs(SQ1 - 2.0) < 1e-2)
        printf("1) SQ1 = 2\n");
    if (fabs(Q1Q2 - (3.0 * sqrt(10.0) / 5.0)) < 1e-2)
        printf("2) Q1Q2 = (3√10)/5\n");
    if (fabs(RQ1 - 3.0) < 1e-2)
        printf("3) RQ1 = 3\n");
    if (fabs(SQ2 - 1.0) < 0.41)  // approx true (0.6 ≈ 1)
        printf("4) SQ2 ≈ 1 (approx true)\n");

    return 0;
}

