/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/10 14:43:39 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/19 20:28:21 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

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
