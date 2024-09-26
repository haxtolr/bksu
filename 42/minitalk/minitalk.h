/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   minitalk.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/14 16:08:10 by heecjang          #+#    #+#             */
/*   Updated: 2023/01/16 05:31:32 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef MINITALK_H
# define MINITALK_H

# include "libft/libft.h"
# include <signal.h>

typedef struct sdat
{
	char	temp;
	int		index;
}	t_data;

void	sig_hand(int sig);
void	send_msg(char *msg, int pid);

#endif