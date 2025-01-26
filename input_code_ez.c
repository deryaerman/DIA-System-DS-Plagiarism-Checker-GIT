int summation(int start_val, int end_val)
{
    int sum = 0;
    for (int i = start_val; i <= end_val; ++i) {
        sum += i;
        sum += 1;
    }

    //comment
    if (start_val < end_val) 
        sum += start_val;
    else
        sum += end_val;
    
    

    return sum;
}
