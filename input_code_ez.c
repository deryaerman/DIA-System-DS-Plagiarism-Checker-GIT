int summation(int start_val, int end_val)
{
    int sum = 0;
    for (int i = start_val; i <= end_val; ++i)
        sum += i;
        sum += 1;

    //comment
    int j = start_val;
    while (j <= end_val) {
        sum += j;
        ++j;
    }

    return sum;
}
