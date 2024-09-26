/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_check_map.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/13 11:45:04 by heecjang          #+#    #+#             */
/*   Updated: 2023/02/18 22:28:20 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "so_long.h"

void	ft_check_el(t_data *data);
void	ft_check_er_el(t_data *data);
void	ft_check_wh(t_data *data);
void	ft_check_wall(t_data *data);

void	ft_check_el(t_data *data)
{
	int	i;
	int	j;

	i = 0;
	while (i < data->row)
	{
		j = 0;
		while (j < data->column)
		{
			if (data->map.area[i][j] == 'P' || \
					data->map.area[i][j] == 'C' || \
					data->map.area[i][j] == 'E' || \
					data->map.area[i][j] == '0' || \
					data->map.area[i][j] == '1')
			{
			}
			else
			{
				ft_printf("Error\n 맵의 구성요소를 확인해주세요");
				exit(1);
			}
			j++;
		}
		i++;
	}
}

void	ft_check_er_el(t_data *data)
{
	if (data->map.p != 1)
	{
		ft_printf("Error\n 플레이어가 1명이 아닙니다.");
		exit(1);
	}
	if (data->map.c < 1)
	{
		ft_printf("Error\n 코인이 너무 적습니다.");
		exit(1);
	}
	if (data->map.e != 1)
	{
		ft_printf("Error\n 탈출구는 1개여야 합니다.");
		exit(1);
	}
}

void	ft_check_wh(t_data *data)
{
	int	i;
	int	j;

	i = -1;
	while (++i < data->row)
	{
		j = -1;
		while (++j < data->column)
		{
			if (data->map.area[i][j] == 'P')
			{
			data->map.p++;
			data->player.x = j;
			data->player.y = i;
			}
			else if (data->map.area[i][j] == 'C')
				data->map.c++;
			else if (data->map.area[i][j] == 'E')
			{
				data->map.e++;
				data->exit.x = j;
				data->exit.y = i;
			}
		}
	}
}

void	ft_check_wall(t_data *data)
{
	int	i;
	int	j;

	i = 0;
	while (i < data->row)
	{
		j = 0;
		while (j < data->column)
		{
			if (data->map.area[0][j] != '1' || \
					data->map.area[data->row - 1][j] != '1' || \
					data->map.area[i][0] != '1' || \
					data->map.area[i][data->column - 1] != '1')
			{
				ft_printf("Error\n 맵이 벽에 둘러져 있지 않습니다.");
				exit (1);
			}
			j++;
		}
		i++;
	}
}
