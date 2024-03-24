#include "philo.h"

long int	ft_atoi(const char *str);
int			input_checker(char **argv);
int			ft_usleep(useconds_t time);
int			ft_strcmp(char *s1, char *s2);

long int	ft_atoi(const char *str)
{
	long int	sign;
	long int	i;
	long int	result;

	result = 0;
	i = 0;
	sign = 1;
	while ((str[i] >= 9 && str[i] <= 13) || str[i] == 32)
		i++;
	if (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			sign = sign * -1;
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
		{
			result = (result * 10) + (str[i++] - '0') * sign;
			if (result > 2147483647 || result < -2147483648)
				return (ft_error(ERR_IN_2, NULL));
		}
	return (result);
}

int	input_checker(char **argv)
{
	int	i;
	int	j;

	i = 1;
	while (argv[i])
	{
		j = 0;
		while (argv[i][j])
		{
			if (argv[i][j] == ' ')
			{
				j++;
				continue ;
			}
			if ((argv[i][j] < 48 || argv[i][j] > 57))
				return (ft_error(ERR_IN_1, NULL));
			j++;
		}
		i++;
	}
	return (0);
}

int	ft_usleep(useconds_t time)
{
	u_int64_t	start;

	start = get_time();
	while ((get_time() - start) < time)
		usleep(time);
	return (0);
}

int	ft_strcmp(char *s1, char *s2)
{
	while (*s1 != '\0' && (*s1 == *s2))
	{
		s1++;
		s2++;
	}
	return (*(char *)s1 - *(char *)s2);
}