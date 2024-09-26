/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/26 13:33:13 by heecjang          #+#    #+#             */
/*   Updated: 2022/11/17 06:22:26 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_nl(int fd, char *buff);
char	*ft_new(char *back);
char	*ft_cut(char *back);
char	*get_next_line(int fd);

char	*ft_cut(char *back)
{
	int		i;
	char	*ct_temp;

	i = 0;
	while (back[i] && back[i] != '\n')
		i++;
	if (back[i] == '\n')
	{
		i++;
		ct_temp = ft_strdup(back + i);
		free(back);
		back = ct_temp;
		if (!back[0])
		{
			free (back);
			back = NULL;
		}
	}
	else
	{
		free (back);
		back = NULL;
	}
	return (back);
}

char	*ft_new(char *back)
{
	int		i;
	char	*nw_temp;

	i = 0;
	while (back[i] && back[i] != '\n')
		i++;
	if (back[i] == '\n')
	{
		nw_temp = ft_substr(back, 0, i + 1);
		return (nw_temp);
	}
	else
	{
		nw_temp = ft_strdup(back);
		return (nw_temp);
	}
}

char	*ft_nl(int fd, char *back)
{
	char	*nl_temp;
	char	*buff;
	ssize_t	rd_size;

	buff = malloc(sizeof(char *) * BUFFER_SIZE + 1);
	if (!buff)
		return (0);
	rd_size = read(fd, buff, BUFFER_SIZE);
	buff[rd_size] = '\0';
	while (rd_size)
	{
		if (!back)
			back = ft_strdup("");
		nl_temp = ft_strjoin(back, buff);
		if (!nl_temp)
			return (0);
		free(back);
		back = nl_temp;
		if (ft_strchr(back, '\n'))
			break ;
		rd_size = read(fd, buff, BUFFER_SIZE);
		buff[rd_size] = '\0';
	}
	free(buff);
	return (back);
}

char	*get_next_line(int fd)
{
	static char	*back;
	char		*temp;

	if (fd < 0 || BUFFER_SIZE <= 0 || read(fd, 0, 0) < 0)
	{
		if (back)
			free(back);
		back = NULL;
		return (0);
	}
	back = ft_nl(fd, back);
	if (!back)
		return (NULL);
	temp = ft_new(back);
	back = ft_cut(back);
	return (temp);
}
