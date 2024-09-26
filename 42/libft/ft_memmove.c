/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/07 09:46:06 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/18 11:36:10 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dst, const void *src, size_t len)
{
	char		*d_temp;
	const char	*s_temp;

	d_temp = dst;
	s_temp = src;
	if (!d_temp && !s_temp)
		return (0);
	if (dst <= src)
	{
		while (len--)
			*d_temp++ = *s_temp++;
	}
	else
	{
		d_temp = d_temp + len;
		s_temp = s_temp + len;
		while (len--)
			*--d_temp = *--s_temp;
	}
	return (dst);
}
