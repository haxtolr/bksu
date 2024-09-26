/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   render.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/02/01 05:34:14 by heecjang          #+#    #+#             */
/*   Updated: 2023/02/18 02:43:54 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "so_long.h"

void	ft_render_bg(t_data *game);
void	ft_draw(t_data *game, char *path, int j, int i);
void	ft_render(t_data *game);
void	ft_render_player(t_data *game);

void	ft_render_bg(t_data *game)
{
	int	i;
	int	j;

	i = 0;
	while (i < game->row)
	{
		j = 0;
		while (j < game->column)
		{
			if (game->map.area[i][j] == 'P' || \
				game->map.area[i][j] == 'C' || \
				game->map.area[i][j] == 'E')
			{
				game->img = mlx_xpm_file_to_image(game->ptr, \
				game->map.floor, &game->block, &game->block);
				mlx_put_image_to_window(game->ptr, game->win, \
				game->img, (j * game->block), (i * game->block));
			}
			j++;
		}
		i++;
	}
}

void	ft_draw(t_data *game, char *path, int j, int i)
{
	game->img = mlx_xpm_file_to_image(game->ptr, \
			path, &game->block, &game->block);
	mlx_put_image_to_window(game->ptr, game->win, \
			game->img, (j * game->block), (i * game->block));
}

void	ft_render(t_data *game)
{	
	int	i;
	int	j;

	i = 0;
	while (i < game->row)
	{
		j = 0;
		while (j < game->column)
		{
			if (game->map.area[i][j] == '1')
				ft_draw(game, game->map.wall, j, i);
			else if (game->map.area[i][j] == '0')
				ft_draw(game, game->map.floor, j, i);
			else if (game->map.area[i][j] == 'P')
				ft_draw(game, game->map.player, j, i);
			else if (game->map.area[i][j] == 'C')
				ft_draw(game, game->map.collect, j, i);
			else if (game->map.area[i][j] == 'E')
				ft_draw(game, game->map.exit, j, i);
		j++;
		}
	i++;
	}
}

void	ft_render_player(t_data *game)
{
	if (game->foot_print.x == game->exit.x && \
			game->foot_print.y == game->exit.y)
	{
		ft_draw(game, game->map.floor, \
				game->foot_print.x, game->foot_print.y);
		ft_draw(game, game->map.exit, \
				game->foot_print.x, game->foot_print.y);
	}
	else
		ft_draw(game, game->map.floor, \
				game->foot_print.x, game->foot_print.y);
	ft_draw(game, game->map.player, game->player.x, game->player.y);
}
