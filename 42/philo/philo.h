#ifndef PHILO_H
# define PHILO_H

# include <stdbool.h>
# include <stdlib.h>
# include <unistd.h>
# include <stdio.h>
# include <pthread.h>
# include <sys/time.h>

//	alloc_err
# define MALLOC_ERR "Error. in ft_malloc"
//	input_err
# define ERR_IN_1 "Invalid input CHARACTER"
# define ERR_IN_2 "Error. Invalid input VALUES"
//	pthread_err
# define TH_ERR "Error. CREATING THREADS"
# define JOIN_ERR "Error. JOINING THREADS"
# define INIT_ERR_1 "Error. INIT FORKS"
//	time_err
# define TIME_ERR "Error. GETTING TIME"
//	philo_msg
# define TAKE_FORKS "has taken a fork"
# define THINKING "is thinking"
# define SLEEPING "is sleeping"
# define EATING "is eating"
# define DIED "died"

struct	s_data;

typedef struct s_philo
{
	struct s_data	*data;
	pthread_t		t1;
	int				id;
	int				eat_cont;
	int				status;
	int				eating;
	u_int64_t		time_to_die;
	pthread_mutex_t	lock;
	pthread_mutex_t	*r_fork;
	pthread_mutex_t	*l_fork;
}	t_philo;

typedef struct s_data
{
	pthread_t		*tid;
	int				philo_num;
	int				meals_nb;
	int				dead;
	int				finished;
	t_philo			*philos;
	u_int64_t		death_time;
	u_int64_t		eat_time;
	u_int64_t		sleep_time;
	u_int64_t		start_time;
	pthread_mutex_t	*forks;
	pthread_mutex_t	lock;
	pthread_mutex_t	write;
}	t_data;

//main
int		ft_error(char *str, t_data *data);
void	ft_exit(t_data *data);
int		is_philo_one(t_data *data);
void	clear_data(t_data	*data);

//	utils
long int	ft_atoi(const char *str);
int			input_checker(char **argv);
int			ft_usleep(useconds_t time);
int			ft_strcmp(char *s1, char *s2);

//	sim
void		eat(t_philo *philo);
void		messages(char *str, t_philo *philo);
void		take_forks(t_philo *philo);
void		drop_forks(t_philo *philo);
u_int64_t	get_time(void);

//	init
int		init_data(t_data *data, char **argv, int argc);
int		ft_malloc(t_data *data);
int		init_forks(t_data *data);
void	init_philos(t_data *data);
int 	init(t_data *data, char **argv, int argc);

//	actions
u_int64_t	get_time(void);
void		eat(t_philo *philo);
void		drop_forks(t_philo *philo);
void		take_forks(t_philo *philo);
void		messages(char *str, t_philo *philo);

//	threads
void	*ft_monitor(void *philo_pointer);
void	*is_all_eat(void *data_pointer);
int		thread_init(t_data *data);
void	*ft_routine(void *philo_pointer);

#endif