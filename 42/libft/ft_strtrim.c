/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/10 15:22:34 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/19 16:15:32 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*temp;
	int		start;
	int		end;
	int		i;

	if (!s1)
		return (0);
	i = 0;
	start = 0;
	end = ft_strlen(s1);
	while (s1[start] && ft_strchr(set, s1[start]))
		start++;
	while (end > start && ft_strchr(set, s1[end - 1]))
		end--;
	temp = (char *)malloc(sizeof(char) * (end - start + 1));
	if (temp == 0)
		return (0);
	while (end > start)
		temp[i++] = s1[start++];
	temp[i] = '\0';
	return (temp);
}	
