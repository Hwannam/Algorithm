#include <stack>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	int num;
	cin >> num;

	stack<int> s;
	
	for (int i = 0; i < num; i++)
	{
		bool vps = true;
		string ps;
		cin >> ps;
		for (int j = 0; j < ps.length(); j++)
		{
			if (ps[j] == '(')
			{
				s.push(1);
			}
			else
			{
				if (s.empty())
				{
					vps = false;
					break;
				}
				else
					s.pop();
			}
		}
		if (!s.empty())
			vps = false;

		cout << (vps == true ? "YES" : "NO") << endl;
		while (!s.empty())
			s.pop();
	}
	
	return 0;
}
