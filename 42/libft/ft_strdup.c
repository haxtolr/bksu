/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/10 14:27:55 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/19 14:39:39 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s1)
{
	char	*temp;
	int		i;
	int		t;

	t = 0;
	i = 0;
	while (s1[i] != '\0')
		i++;
	temp = (char *)malloc(sizeof(char) * i + 1);
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
