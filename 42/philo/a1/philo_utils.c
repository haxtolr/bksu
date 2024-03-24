#include "philo.h"

int		ft_atoi(const char *str);
size_t	ft_strlen(const char *s);

int	ft_atoi(const char *str)
{
	int			i;
	int			sign;
	long int	result;

	i = 0;
	sign = 1;
	result = 0;
	while (str[i] == ' ' || str[i] == '\t' || str[i] == '\n' || str[i] == '\v' || str[i] == '\f' || str[i] == '\r')
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
	{
		result = result * 10 + (str[i] - '0');
		i++;
		if (result > 2147483647 || result < -2147483648)
			return (0);
	}
	return (result * sign);
}

size_t	ft_strlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

void	ft_putnbr_fd(int n, int fd)
{
	char	c;

	if (n == -2147483648)
	{
		write(fd, "-2147483648", 11);
		return ;
	}
	if (n < 0)
	{
		write(fd, "-", 1);
		n *= -1;
	}
	if (n >= 10)
		ft_putnbr_fd(n / 10, fd);
	c = n % 10 + '0';
	write(fd, &c, 1);
}	

void	ft_putstr_fd(char *s, int fd)
{
	write(fd, s, ft_strlen(s));
}

int		ft_isdigit(int c)
{
	if (c >= '0' && c <= '9')
		return (1);
	return (0);
}

long	get_time_in_ms(void)
{
	struct timeval	time;

	gettimeofday(&time, NULL);
	return (time.tv_sec * 1000 + time.tv_usec / 1000);
}

void	print_status(t_data *data, int philo_id, char *msg)
{
	pthread_mutex_lock(&data->forks[data->num_of_philos]);
	ft_putnbr_fd(get_time_in_ms() - data->philos[0].last_time_eaten, 1);
	ft_putstr_fd(" ", 1);
	ft_putnbr_fd(philo_id, 1);
	ft_putstr_fd(" ", 1);
	ft_putstr_fd(msg, 1);
	ft_putstr_fd("\n", 1);
	pthread_mutex_unlock(&data->forks[data->num_of_philos]);
}