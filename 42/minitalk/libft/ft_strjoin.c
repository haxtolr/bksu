/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/10 14:58:30 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/18 12:47:58 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*temp;
	int		i;

	if (!s1 || !s2)
		return (0);
	i = 0;
	temp = (char *)malloc(sizeof(char) * ft_strlen(s1) + ft_strlen(s2) + 1);
	if (temp == 0)
		return (0);
	while (*s1 != '\0')
		temp[i++] = *s1++;
	while (*s2 != '\0')
		temp[i++] = *s2++;
	temp[i] = '\0';
	return (temp);
}
