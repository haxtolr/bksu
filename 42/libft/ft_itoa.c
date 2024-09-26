/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/10 19:22:03 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/18 15:44:33 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr(int nbr, char *temp, int len);

char	*ft_itoa(int n)
{
	int		len;
	char	*temp;
	int		nbr;

	nbr = n;
	len = 0;
	if (n < 0)
		len++;
	while (n != 0)
	{
		n = n / 10;
		len++;
	}
	if (nbr == 0)
		len++;
	temp = malloc(sizeof(char) * len + 1);
	if (temp == 0)
		return (0);
	temp[len] = '\0';
	ft_putnbr(nbr, temp, len);
	return (temp);
}

void	ft_putnbr(int nbr, char *temp, int len)
{
	int	k;
	int	sign;

	k = 0;
	if (nbr < 0)
		sign = -1;
	if (nbr == 0)
		temp[0] = '0';
	while (len--)
	{
		k = nbr % 10;
		nbr = nbr / 10;
		if (k < 0)
			k = k * -1;
		temp[len] = k + 48;
	}
	if (sign == -1)
		temp[0] = '-';
}
