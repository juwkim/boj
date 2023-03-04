#include <unistd.h>

int main()
{
	char	res[2000000];
	char	buf[1000000 + 1];
	int		size = read(0, buf, 1000000);

	if (size == 0)
		return (0);
	int		idx = 0;
	int		cur = 0;
	while (idx < size)
	{
		switch (buf[idx])
		{
			case ' ':
				++idx;
				break ;
			case '<':
			case '>':
			case '(':
			case ')':
				res[cur++] = buf[idx++];
				res[cur++] = ' ';
				break ;
			case '&':
			case '|':
				res[cur++] = buf[idx++];
				res[cur++] = buf[idx++];
				res[cur++] = ' ';
				break ;
			default:
				while (strchr("<>()&| ", buf[idx]) == NULL)
					res[cur++] = buf[idx++];
				res[cur++] = ' ';
		}
	}
	res[--cur] = '\0';
    write(1, res, cur);
	return (0);
}