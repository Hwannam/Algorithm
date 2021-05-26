#include <iostream>
using namespace std;

bool isnum(int num)
{
	if (num < 100)
		return true;
	else
	{
		if ((num / 100) - ((num % 100) / 10) == ((num % 100) / 10) - (num % 10))
			return true;
		else
			return false;
	}
}
int main()
{
	int num;
	cin >> num;

	int sum = 0;
	for (int i = 1; i <= num; i++)
	{
		if (isnum(i))
			sum++;
	}
	cout << sum << endl;
	return 0;
}
