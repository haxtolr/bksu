/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_mlx_hook.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/15 12:21:30 by heecjang          #+#    #+#             */
/*   Updated: 2023/02/18 22:28:23 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "so_long.h"

int		ft_check_move(t_data *game, int new_x, int new_y);
void	ft_move(t_data *game, int new_x, int new_y);
int		ft_loop_hook(t_data *game);
int		ft_key_hook(int keycode, t_data *game);

int	ft_check_move(t_data *game, int new_x, int new_y)
{
	char	pos;

	pos = game->map.area[new_y][new_x];
	if (pos == '0' || pos == 'C')
	{
		if (pos == 'C')
			game->map.c--;
		return (1);
	}
	if ((pos == 'E') && (game->map.c == 0))
	{
		ft_printf("\n\n======= 승 리 =======");
		return (2);
	}
	if (pos == 'E')
		return (3);
	return (0);
}

void	ft_move(t_data *game, int new_x, int new_y)
{
	if (game->player.x == game->exit.x && game->player.y == game->exit.y)
	{
		game->map.area[game->player.y][game->player.x] = 'E';
	}
	else
		game->map.area[game->player.y][game->player.x] = '0';
	game->map.area[new_y][new_x] = 'P';
	game->foot_print.x = game->player.x;
	game->foot_print.y = game->player.y;
	game->player.x = new_x;
	game->player.y = new_y;
	game->map.counter++;
	ft_printf("\ncounter = %d", game->map.counter);
}

int	ft_loop_hook(t_data *game)
{
	ft_render_player(game);
	return (0);
}

int	ft_key_hook(int keycode, t_data *game)
{
	int	new_x;
	int	new_y;
	int	check;

	new_x = game->player.x;
	new_y = game->player.y;
	if (keycode == KEY_A || keycode == KEY_LEFT)
		new_x--;
	else if (keycode == KEY_D || keycode == KEY_RIGHT)
		new_x++;
	else if (keycode == KEY_W || keycode == KEY_UP)
		new_y--;
	else if (keycode == KEY_S || keycode == KEY_DOWN)
		new_y++;
	else if (keycode == KEY_ESC)
		ft_close(game);
	else
		return (0);
	check = ft_check_move(game, new_x, new_y);
	if (check == 1 || check == 3)
		ft_move(game, new_x, new_y);
	if (check == 2)
		ft_close(game);
	return (check);
}
