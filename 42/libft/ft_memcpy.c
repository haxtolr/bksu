/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/07 09:21:54 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/18 11:35:31 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dst, const void *src, size_t n)
{
	char		*d_temp;
	const char	*s_temp;

	d_temp = dst;
	s_temp = src;
	if (!src && !dst)
		return (0);
	while (n != 0)
	{
		*d_temp = *s_temp;
		d_temp++;
		s_temp++;
		n--;
	}
	return (dst);
}
