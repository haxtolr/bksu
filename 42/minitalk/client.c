/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   client.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/11 19:57:57 by heecjang          #+#    #+#             */
/*   Updated: 2023/01/17 16:41:37 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "minitalk.h"

void	check_msg(char *msg, int pid);
void	send_msg(char *msg, int pid);

int	main(int ac, char *av[])
{
	int	pid;

	if (ac != 3)
	{
		ft_printf("error\n");
		return (0);
	}
	pid = ft_atoi(av[1]);
	check_msg(av[2], pid);
	return (0);
}

void	check_msg(char *msg, int pid)
{
	char	*checker;

	checker = ft_strjoin(msg, "\n");
	if (checker == NULL)
		exit(1);
	send_msg(checker, pid);
	free(checker);
	exit(0);
}

void	send_msg(char *msg, int pid)
{
	int	i;
	int	t;
	int	c;

	i = 0;
	while (msg[i] != '\0')
	{
		t = 0;
		while (t < 8)
		{
			c = msg[i] >> (7 - t) & 1;
			if (c == 0)
				kill(pid, SIGUSR1);
			if (c == 1)
				kill(pid, SIGUSR2);
			usleep(30);
			t++;
		}
		usleep(30);
		i++;
	}
}
