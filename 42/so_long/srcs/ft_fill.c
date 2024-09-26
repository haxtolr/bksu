/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_fill.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/02/02 01:21:44 by heecjang          #+#    #+#             */
/*   Updated: 2023/02/20 07:51:10 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "so_long.h"

char	**ft_dupmap(t_data *data);
void	ft_check_load(char **map, int row);
void	ft_fill(char **area, t_data *data, int x, int y);
void	ft_flood(char	**area, t_data *data);
void	ft_flood_full(t_data *data);

char	**ft_dupmap(t_data *data)
{
	char	**area;
	int		i;
	int		j;

	area = (char **)malloc(sizeof(char *) * data->row);
	if (!area)
		return (0);
	i = 0;
	while (i < data->row)
	{
		area[i] = malloc(sizeof(char) * (data->column + 1));
		if (!area[i])
		{
			ft_free(area, i);
			return (0);
		}
		j = 0;
		while (j < data->column)
		{
			area[i][j] = data->map.area[i][j];
			j++;
		}
		area[i++][j] = '\0';
	}
	return (area);
}

void	ft_check_load(char **map, int row)
{
	int	i;
	int	j;

	ft_printf("\n======게임 시작======\n");
	i = 0;
	while (i < row)
	{
		j = 0;
		while (map[i][j] != '\0')
		{
			if (map[i][j] == 'C' || map[i][j] == 'E')
			{
				ft_printf("Error\n맵 경로를 확인해주세요\n여기서 종료");
				ft_free(map, row);
				exit (1);
			}
			j++;
		}
	i++;
	}
}

void	ft_fill(char **area, t_data *data, int x, int y)
{
	if (x < 0 || y < 0 || x >= data->column \
			|| y >= data->row || area[y][x] == '1' || area[y][x] == 'x')
		return ;
	area[y][x] = 'x';
	ft_fill(area, data, x - 1, y);
	ft_fill(area, data, x + 1, y);
	ft_fill(area, data, x, y - 1);
	ft_fill(area, data, x, y + 1);
	return ;
}

void	ft_flood(char	**area, t_data *data)
{
	ft_fill(area, data, data->player.x, data->player.y);
}

void	ft_flood_full(t_data *data)
{
	char	**area;

	area = ft_dupmap(data);
	ft_flood(area, data);
	ft_check_load(area, data->row);
	ft_free(area, data->row);
}
