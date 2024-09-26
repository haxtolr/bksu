/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_av_check.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/02/28 10:46:40 by heecjang          #+#    #+#             */
/*   Updated: 2023/03/09 01:35:58 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_empty(char *av);
int	ft_two(char **av);
int	check_av(char **av);

int	ft_empty(char *av)
{
	int	i;

	i = 0;
	if (!av[i])
		return (0);
	while (av[i])
	{
		if (av[i] != ' ')
			return (1);
		i++;
	}
	return (0);
}

int	ft_two(char **av)
{
	int	i;
	int	j;

	i = -1;
	while (av[++i])
	{
		j = 0;
		while (av[++j])
			if (j != i && !nb_check(av[i], av[j]))
				return (1);
	}
	return (0);
}

int	check_av(char **av)
{
	int	i;
	int	nb;

	i = -1;
	nb = 0;
	if (ft_two(av))
		return (0);
	while (av[++i])
	{
		if (!(ft_nbr(av[i])))
			return (0);
		nb += ft_zero(av[i]);
	}
	if (nb > 1)
		return (0);
	return (1);
}
