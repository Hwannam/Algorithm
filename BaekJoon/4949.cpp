#include <stack>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	string sentence;
	stack<char> s;

	while (1)
	{
		bool complete = true;
		cin.clear();
		getline(cin, sentence);
		
		if (sentence == ".")
			break;
		for (int i = 0; i < sentence.length(); i++)
		{
			if (sentence[i] == '(' || sentence[i] == '[')
				s.push(sentence[i]);
			else if (sentence[i] == ')')
			{
				if (!s.empty() &&s.top() == '(')
					s.pop();
				else
				{
					complete = false;
					break;
				}
			}
			else if (sentence[i] == ']')
			{
				if (!s.empty() && s.top() == '[')
					s.pop();
				else
				{
					complete = false;
					break;
				}
			}
		}
		if (!s.empty())
			complete = false;

		cout << (complete == true ? "yes" : "no") << endl;

		while (!s.empty())
			s.pop();
		
	}
	return 0;
}
