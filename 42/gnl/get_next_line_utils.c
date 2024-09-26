/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/31 14:19:06 by heecjang          #+#    #+#             */
/*   Updated: 2022/11/17 05:09:32 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_substr(char const *s, unsigned int start, size_t len);
char	*ft_strjoin(char *s1, char *s2);
size_t	ft_strlen(const char *s);
char	*ft_strdup(char *s1);
char	*ft_strchr(const char *s, int c);

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char			*temp;
	size_t			i;

	i = 0;
	if (!s)
		return (0);
	if (ft_strlen(s) < start)
		return (ft_strdup(""));
	if (len > ft_strlen(s))
		len = ft_strlen(s);
	temp = (char *)malloc(sizeof(char) * (len + 1));
	if (temp == 0)
		return (0);
	while (i < len && s[start] != '\0')
		temp[i++] = s[start++];
	temp[i] = '\0';
	return (temp);
}

char	*ft_strchr(const char *s, int c)
{
	while (*s)
	{
		if (*s == (char)c)
			return ((char *)s);
		s++;
	}
	if (*s == (char)c)
		return ((char *)s);
	return (0);
}

char	*ft_strjoin(char *s1, char *s2)
{
	char	*temp;
	int		i;

	if (!s2 || !s1)
		return (NULL);
	i = 0;
	temp = malloc(sizeof(char *) * (ft_strlen(s1) + ft_strlen(s2) + 1));
	if (temp == 0)
		return (0);
	while (*s1 != '\0')
		temp[i++] = *s1++;
	while (*s2 != '\0')
		temp[i++] = *s2++;
	temp[i] = '\0';
	return (temp);
}

size_t	ft_strlen(const char *s)
{
	size_t	i;

	i = 0;
	if (!s)
		return (0);
	while (*s != '\0')
	{
		s++;
		i++;
	}
	return (i);
}

char	*ft_strdup(char *s1)
{
	char	*temp;
	int		i;
	int		t;

	t = 0;
	i = 0;
	if (!s1)
		return (0);
	while (s1[i] != '\0')
		i++;
	temp = malloc(sizeof(char *) * i + 1);
	if (temp == 0)
		return (0);
	while (i > t)
	{
		temp[t] = s1[t];
		t++;
	}
	temp[t] = '\0';
	return (temp);
}
