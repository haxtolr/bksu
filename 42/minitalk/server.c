/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   server.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/11 14:37:02 by heecjang          #+#    #+#             */
/*   Updated: 2023/01/16 04:39:02 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "minitalk.h"

void	sig_hand(int sig);

int	main(void)
{	
	struct sigaction	act;

	act.sa_handler = sig_hand;
	sigemptyset(&act.sa_mask);
	act.sa_flags = SA_SIGINFO;
	sigaction(SIGUSR1, &act, 0);
	sigaction(SIGUSR2, &act, 0);
	ft_printf("PID : %d\n", getpid());
	while (1)
	{
		pause();
	}
}

void	sig_hand(int sig)
{
	static t_data	sdat;

	if (sig == SIGUSR1)
	{
		sdat.temp |= 0;
		if (sdat.index < 7)
			sdat.temp <<= 1;
	}
	else if (sig == SIGUSR2)
	{
		sdat.temp |= 1;
		if (sdat.index < 7)
			sdat.temp <<= 1;
	}
	sdat.index++;
	if (sdat.index == 8)
	{
		write(1, &sdat.temp, 1);
		sdat.temp = 0;
		sdat.index = 0;
	}
}
