/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/07 12:39:26 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/18 12:52:49 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	unsigned char	*temp_s1;
	unsigned char	*temp_s2;

	temp_s1 = (unsigned char *)s1;
	temp_s2 = (unsigned char *)s2;
	while (n)
	{
		if (*temp_s1 == '\0' && *temp_s2 == '\0')
			break ;
		if (*temp_s1 != *temp_s2)
		{
			if (*temp_s1 > *temp_s2)
				return (1);
			else
				return (-1);
		}
		temp_s1++;
		temp_s2++;
		n--;
	}
	return (0);
}
