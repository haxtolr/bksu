#ifndef PHILO_H
# define PHILO_H

# include <pthread.h>
# include <stdbool.h>
# include <sys/time.h>
# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>

typedef struct s_philo
{
	int				id;
	int				num_of_times_eaten;
	long			last_time_eaten;
	pthread_mutex_t	*left_fork;
	pthread_mutex_t	*right_fork;
	pthread_t		thread;
	pthread_t		monitor_thread;
	struct s_data	*data;
}	t_philo;

typedef struct s_data
{
	int				num_of_philos;
	int				time_to_die;
	int				time_to_eat;
	int				time_to_sleep;
	int				num_of_times_each_philo_must_eat;
	pthread_mutex_t	*forks;
	t_philo			*philos;
}	t_data;


/*
** Utils functions
*/

size_t	ft_strlen(const char *s);
int		ft_atoi(const char *s);
int		ft_isdigit(int c);
long	get_time_in_ms(void);
void	ft_putnbr_fd(int n, int fd);
void	ft_putstr_fd(char *s, int fd);
void	print_status(t_data *data, int philo_id, char *msg);

/*
** Initialization and Execution functions
*/

void	init_philos(t_data *data);
void	create_threads(t_data *data);
void	join_threads(t_data *data);

/*
** Thread functions
*/

void	*start_simulation(void *arg);
void	philo_take_forks(t_philo *philo);
void	philo_drop_forks(t_philo *philo);
void	philo_eat(t_philo *philo);
void	philo_sleep(t_philo *philo);
void	philo_think(t_philo *philo);
bool	check_philo_alive(t_philo *philo, t_data *data);
bool	check_all_philos_alive(t_data *data);
void	*monitor_simulation(void *arg);

#endif
