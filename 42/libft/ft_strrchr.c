/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/07 14:51:02 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/19 20:38:31 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	size_t	slen;

	slen = ft_strlen(s);
	while (s[slen] != c && slen != 0)
	{
		if (s[slen] == (char)c)
			return ((char *)(s + slen));
		slen--;
	}
	if (s[slen] == (char)c)
		return ((char *)(s + slen));
	return (0);
}
