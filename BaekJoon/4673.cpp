#include <iostream>
using namespace std;

int notself(int num)
{
	int newnum = num;
	while (1)
	{
		newnum += num % 10;
		num = num / 10;
		if (num == 0)
			break;
	}
	return newnum;
}
int main()
{
	bool ary[10001];
	fill_n(ary, 10001, true);
	for (int i = 1; i < 10001; i++)
	{
		if(notself(i) <10001)
		ary[notself(i)] = false;
	}
	for (int i = 1; i < 10001; i++)
	{
		if (ary[i] == true)
			cout << i << endl;
	}
	return 0;
}
