/* https://www.codewars.com/kata/515e271a311df0350d00000f */


#include <vector>

int square_sum(const std::vector<int>& numbers)
{
    int sum = 0;
    for (int i = 0 ; i <  numbers.size() ; i++){
      sum +=numbers[i]*numbers[i];
    }
    
    return sum;
}
