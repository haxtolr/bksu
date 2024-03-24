#include "philo.h"

int main(int ac, char **av)
{
    t_data data;

    if (ac != 5 && ac != 6)
        return (1);
    data.num_of_philos = ft_atoi(av[1]);
    data.time_to_die = ft_atoi(av[2]);
    data.time_to_eat = ft_atoi(av[3]);
    data.time_to_sleep = ft_atoi(av[4]);
    if (ac == 6)
        data.num_of_times_each_philo_must_eat = ft_atoi(av[5]);
    else
        data.num_of_times_each_philo_must_eat = -1;
    if (data.num_of_philos < 2 || data.num_of_philos > 200 || data.time_to_die < 60 || data.time_to_eat < 60 || data.time_to_sleep < 60 || data.num_of_times_each_philo_must_eat < -1)
        return (1);
    init_philos(&data);
    create_threads(&data);
    join_threads(&data);
    return (0);
}

void    init_philos(t_data *data)
{
    int i;

    i = 0;
    data->philos = malloc(sizeof(t_philo) * data->num_of_philos);
    data->forks = malloc(sizeof(pthread_mutex_t) * data->num_of_philos);
    while (i < data->num_of_philos)
    {
        data->philos[i].id = i + 1;
        data->philos[i].num_of_times_eaten = 0;
        data->philos[i].last_time_eaten = get_time_in_ms();
        data->philos[i].data = data;
        if (i == 0)
            data->philos[i].left_fork = &data->forks[data->num_of_philos - 1];
        else
            data->philos[i].left_fork = &data->forks[i - 1];
        data->philos[i].right_fork = &data->forks[i];
        pthread_mutex_init(&data->forks[i], NULL);
        i++;
    }
}

void    create_threads(t_data *data)
{
    int i;

    i = 0;
    while (i < data->num_of_philos)
    {
        pthread_create(&data->philos[i].monitor_thread, NULL, start_simulation, &data->philos[i]);
        i++;
    }
}

void    join_threads(t_data *data)
{
    int i;

    i = 0;
    while (i < data->num_of_philos)
    {
        pthread_join(data->philos[i].monitor_thread, NULL);
        i++;
    }
}