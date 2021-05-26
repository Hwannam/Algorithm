#include <stack>
#include <iostream>
using namespace std;

int main()
{
	int num;
	cin >> num;

	stack<int> s;
	
	for (int i = 0; i < num; i++)
	{
		int callnum;
		cin >> callnum;
		if (callnum == 0)
			s.pop();
		else
			s.push(callnum);
	}
	int result = 0;
	while (!s.empty())
	{
		result += s.top();
		s.pop();
	}
	cout << result << endl;
	return 0;
}
