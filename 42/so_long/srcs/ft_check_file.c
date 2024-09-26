/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_check_file.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/21 00:58:03 by heecjang          #+#    #+#             */
/*   Updated: 2023/02/20 08:24:40 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "so_long.h"

void	ft_check_argc(int number);
void	ft_check_name(char *str);
int		ft_open(char *name);
void	ft_check_rec(t_data *data, char *name);

void	ft_check_argc(int number)
{
	if (number > 2)
	{
		ft_printf("Error\n인자값이 너무 많습니다.");
		exit (1);
	}
	else if (number < 2)
	{
		ft_printf("Error\n맵파일을 넣어주세요");
		exit (1);
	}
}

void	ft_check_name(char *str)
{
	char	*ber;

	ber = ".ber";
	if (ft_strm(str, ber, ft_strlen(str)))
	{
		ft_printf("로딩중........\n");
	}
	else
	{
		ft_printf("Error\nber 맵이 아닙니다.\n");
		exit(1);
	}
}

int	ft_open(char *name)
{
	int	fd;

	fd = open(name, O_RDONLY);
	if (fd < 0)
	{
		ft_printf("Error\n읽기에 실패했습니다.");
		exit (1);
	}
	return (fd);
}

void	ft_check_rec(t_data *data, char *name)
{
	char	*line;
	int		fd;

	data->row = 0;
	data->column = 0;
	fd = ft_open(name);
	line = get_next_line(fd);
	data->column = ft_strlen_n(line);
	free(line);
	while (line != NULL)
	{
		line = get_next_line(fd);
		if (line != NULL && data->column != ft_strlen_n(line))
		{
			ft_printf("Error\n맵이 직사각형이 아닙니다.");
			free(line);
			close(fd);
			exit(1);
		}
		free(line);
		data->row++;
	}
	free(line);
	close(fd);
}
