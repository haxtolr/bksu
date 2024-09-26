/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/12 15:23:34 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/18 15:12:38 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char				*temp;
	int					len;
	unsigned int		i;

	i = 0;
	if (s == 0 || f == 0)
		return (0);
	len = ft_strlen(s);
	temp = malloc(sizeof(char) * len + 1);
	if (temp == 0)
		return (0);
	while (s[i])
	{
		temp[i] = f(i, s[i]);
		i++;
	}
	temp[i] = '\0';
	return (temp);
}
