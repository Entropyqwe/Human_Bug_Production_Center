int judgeSolutions(int a, int b, int c) {
    if (a == 0) {
        if (b != 0) return 1; 
        return c == 0;
    }
    return (long long)b * b - 4LL * a * c >= 0;
}