/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/10 17:51:28 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/19 21:00:20 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int		is_sp(char a, char c);
int		str_len(char const *s, char c);
int		arr_size(char const *s, char c);
void	ft_set_arr(char const *s, char c, int i, char **arr);

char	**ft_split(char const *s, char c)
{
	char	**arr;
	int		j;
	int		alen;
	int		i;

	if (!s)
		return (0);
	i = 0;
	alen = arr_size(s, c);
	arr = malloc(sizeof(char *) * (alen + 1));
	if (arr == 0)
		return (0);
	while (alen--)
	{
		j = 0;
		ft_set_arr(s, c, i, arr);
		while (is_sp(*s, c) == 1 && *s != '\0')
			s++;
		while (is_sp(*s, c) == 0 && *s != '\0')
			arr[i][j++] = *s++;
		arr[i++][j] = '\0';
	}
	arr[i] = NULL;
	return (arr);
}

void	ft_set_arr(char const *s, char c, int i, char **arr)
{
	arr[i] = malloc(sizeof(char) * (str_len(&*s, c) + 1));
	if (arr[i] == 0)
	{
		return ;
		while (i--)
		{
			free(arr[i]);
		}
		free(arr);
	}
}

int	is_sp(char a, char c)
{
	if (a == c)
		return (1);
	return (0);
}

int	str_len(char const *s, char c)
{
	int	slen;
	int	i;

	i = 0;
	slen = 0;
	while (is_sp(s[i], c) == 1 && s[i] != '\0')
		i++;
	while (is_sp(s[i], c) == 0 && s[i] != '\0')
	{
		i++;
		slen++;
	}
	return (slen);
}

int	arr_size(char const *s, char c)
{
	int	i;
	int	alen;

	alen = 0;
	i = 0;
	while (s[i])
	{
		while (is_sp(s[i], c) == 1 && s[i] != '\0')
			i++;
		if (is_sp(s[i], c) == 0 && s[i] != '\0')
		{
			alen++;
			while (is_sp(s[i], c) == 0 && s[i] != '\0')
				i++;
		}
	}
	return (alen);
}
