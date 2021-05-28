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
		string menu;
		cin >> menu;
		if (menu =="push")
		{
			int num;
			cin >> num;
			s.push(num);
		}
		else if (menu == "pop")
		{
			if (s.empty())
			{
				cout << -1 << endl;
			}
			else
			{
				cout << s.top() << endl;
				s.pop();
			}
		}
		else if (menu == "top")
		{
			if (s.empty())
			{
				cout << -1 << endl;
			}
			else
				cout << s.top() << endl;
		}
		else if (menu == "size")
			cout << s.size() << endl;
		else if (menu == "empty")
			cout << (s.empty() ? 1 : 0) << endl;
	}
	return 0;
}
