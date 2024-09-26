/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/02/15 01:40:54 by heecjang          #+#    #+#             */
/*   Updated: 2023/02/20 08:21:12 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SO_LONG_H
# define SO_LONG_H

# include <stdlib.h>
# include "../lib/libft/libft.h"
# include "../lib/gnl/get_next_line.h"
# include "../lib/ft_printf/ft_printf.h"
# include <fcntl.h>
# include "../mlx/mlx.h"
# include <unistd.h>

# define X_EVENT_KEY_PRESS	2
# define X_EVENT_KEY_RELEASE	3
# define X_EVENT_KEY_EXIT	17

# define KEY_ESC	53
# define KEY_LEFT	123
# define KEY_RIGHT	124
# define KEY_UP		126
# define KEY_DOWN	125
# define KEY_A		0
# define KEY_S		1
# define KEY_D		2
# define KEY_W		13

typedef struct s_map
{
	char	**area;
	char	*wall;
	char	*floor;
	char	*player;
	char	*collect;
	char	*enmy;
	char	*exit;
	int		p;
	int		c;
	int		e;
	int		counter;
}	t_map;

typedef struct s_vec
{
	int	x;
	int	y;
}	t_vec;

typedef struct s_dim
{
	int	width;
	int	height;
}	t_dim;

typedef struct s_data
{
	void	*ptr;
	void	*win;
	void	*img;
	int		row;
	int		column;
	int		block;
	t_map	map;
	t_dim	window;
	t_vec	player;
	t_vec	exit;
	t_vec	foot_print;
}	t_data;

int		ft_close(t_data *game);
void	ft_run(t_data *game);
void	ft_data(t_data *data);
void	ft_load(t_data *data, char *name);
int		ft_strlen_n(char *str);
void	ft_free(char **area, int row);
void	ft_render_bg(t_data *game);
void	ft_draw(t_data *game, char *path, int j, int i);
void	ft_render(t_data *game);
void	ft_render_player(t_data *game);
int		ft_check_move(t_data *game, int new_x, int new_y);
void	ft_move(t_data *game, int new_x, int new_y);
int		ft_loop_hook(t_data *game);
int		ft_key_hook(int keycode, t_data *game);
char	**ft_dupmap(t_data *data);
void	ft_check_load(char **map, int row);
void	ft_fill(char **area, t_data *data, int x, int y);
void	ft_flood(char **area, t_data *data);
void	ft_flood_full(t_data *data);
void	ft_check_el(t_data *data);
void	ft_check_er_el(t_data *data);
void	ft_check_wh(t_data *data);
void	ft_check_wall(t_data *data);
void	ft_check_argc(int number);
void	ft_check_name(char *str);
int		ft_open(char *name);
void	ft_check_rec(t_data *data, char *name);
int		ft_strm(char *str, char *finder, int len);

#endif
