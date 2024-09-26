/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long_utils.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/02/15 00:15:21 by heecjang          #+#    #+#             */
/*   Updated: 2023/02/20 08:21:16 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "so_long.h"

int		ft_strlen_n(char *str);
void	ft_free(char **area, int row);

void	ft_free(char **area, int row)
{
	int	i;

	i = 0;
	while (i < row)
	{
		free(area[i]);
		i++;
	}
	free (area);
}

int	ft_strm(char *str, char *finder, int len)
{
	int	i;
	int	t;

	t = 0;
	i = len;
	while (i != len - 4)
	{
		if (i - 4 == len)
			break ;
		if (str[i - 4] != finder[t])
			return (0);
	i++;
	t++;
	}
	return (1);
}

int	ft_strlen_n(char *str)
{
	int	i;

	if (!str)
	{
		ft_printf("Error\n 빈 맵파일 입니다.");
		exit (1);
	}
	i = 0;
	while (str[i] != '\0' && str[i] != '\n')
	{
		i++;
	}
	return (i);
}
