/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/02/11 22:41:06 by heecjang          #+#    #+#             */
/*   Updated: 2023/02/20 07:46:41 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "so_long.h"

int		ft_close(t_data *game);
void	ft_run(t_data *game);
void	ft_data(t_data *data);
void	ft_load(t_data *data, char *name);

int	main(int argc, char *argv[])
{
	t_data	game;

	ft_check_argc(argc);
	ft_check_name(argv[1]);
	ft_check_rec(&game, argv[1]);
	ft_data(&game);
	ft_load(&game, argv[1]);
	ft_check_el(&game);
	ft_check_wh(&game);
	ft_check_er_el(&game);
	ft_check_wall(&game);
	ft_flood_full(&game);
	ft_run(&game);
	return (0);
}

int	ft_close(t_data *game)
{
	mlx_destroy_window(game->ptr, game->win);
	ft_free(game->map.area, game->row);
	free(game->ptr);
	exit(0);
	return (0);
}

void	ft_run(t_data *game)
{
	game->ptr = mlx_init();
	game->win = mlx_new_window(game->ptr, game->window.width, \
			game->window.height, "so_long");
	ft_render_bg(game);
	ft_render(game);
	game->foot_print.x = game->player.x;
	game->foot_print.y = game->player.y;
	mlx_hook(game->win, 17, 1L << 0, ft_close, game);
	mlx_key_hook(game->win, ft_key_hook, game);
	mlx_loop_hook(game->ptr, ft_loop_hook, game);
	mlx_loop(game->ptr);
}

void	ft_data(t_data *data)
{
	data->map.p = 0;
	data->map.c = 0;
	data->map.e = 0;
	data->map.counter = 0;
	data->map.wall = "./textures/wall.xpm";
	data->map.player = "./textures/player.xpm";
	data->map.floor = "./textures/floor.xpm";
	data->map.collect = "./textures/collect.xpm";
	data->map.exit = "./textures/exit.xpm";
	data->block = 32;
	data->window.width = data->block * data->column;
	data->window.height = data->block * data->row;
}

void	ft_load(t_data *data, char *name)
{
	int		fd;
	int		i;

	fd = open(name, O_RDONLY);
	data->map.area = (char **)malloc(sizeof(char *) * data->row);
	if (!data->map.area)
		return ;
	i = 0;
	while (i < data->row)
	{
		data->map.area[i] = get_next_line(fd);
		i++;
	}
	close(fd);
}
