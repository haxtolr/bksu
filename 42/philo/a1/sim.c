#include "philo.h"

void	*start_simulation(void *arg)
{
	t_philo	*philo;

	philo = (t_philo *)arg;
	while (1)
	{
		philo_take_forks(philo);
		philo_eat(philo);
		philo_drop_forks(philo);
		print_status(philo->data, philo->id, "is sleeping");
		usleep(philo->data->time_to_sleep * 1000);
		print_status(philo->data, philo->id, "is thinking");
	}
}

void	philo_take_forks(t_philo *philo)
{
	pthread_mutex_lock(philo->left_fork);
	print_status(philo->data, philo->id, "has taken a fork");
	pthread_mutex_lock(philo->right_fork);
	print_status(philo->data, philo->id, "has taken a fork");
}

void	philo_drop_forks(t_philo *philo)
{
	pthread_mutex_unlock(philo->left_fork);
	pthread_mutex_unlock(philo->right_fork);
}

void	philo_eat(t_philo *philo)
{
	print_status(philo->data, philo->id, "is eating");
	philo->last_time_eaten = get_time_in_ms();
	philo->num_of_times_eaten++;
	usleep(philo->data->time_to_eat * 1000);
}

void	philo_sleep(t_philo *philo)
{
	print_status(philo->data, philo->id, "is sleeping");
	usleep(philo->data->time_to_sleep * 1000);
}

void	philo_think(t_philo *philo)
{
	print_status(philo->data, philo->id, "is thinking");
}

bool	check_philo_alive(t_philo *philo, t_data *data)
{
	if (get_time_in_ms() - philo->last_time_eaten > data->time_to_die)
	{
		print_status(data, philo->id, "died");
		return (false);
	}
	return (true);
}

bool	check_all_philos_alive(t_data *data)
{
	int	i;

	i = 0;
	while (i < data->num_of_philos)
	{
		if (!check_philo_alive(&data->philos[i], data))
			return (false);
		i++;
	}
	return (true);
}

void	*monitor_simulation(void *arg)
{
	t_data	*data;

	data = (t_data *)arg;
	while (1)
	{
		if (!check_all_philos_alive(data))
			return (NULL);
	}
}