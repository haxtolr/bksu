/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_format2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/22 21:31:46 by heecjang          #+#    #+#             */
/*   Updated: 2023/01/16 04:33:32 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_putunnbr(unsigned int nb)
{
	int	i;

	i = 0;
	if (nb < 10)
		i += ft_putchar(nb + '0');
	else
	{
		i += ft_putunnbr(nb / 10);
		i += ft_putunnbr(nb % 10);
	}
	return (i);
}

int	ft_putnbr_hex(unsigned int nb, char x)
{
	int	i;

	i = 0;
	if (nb >= 16)
	{
		i += ft_putnbr_hex(nb / 16, x);
		i += ft_putnbr_hex(nb % 16, x);
	}
	else
	{
		if (nb < 10)
			i += ft_putchar(nb + '0');
		if (nb > 9 && x == 'X')
			i += ft_putchar(nb - 10 + 'A');
		if (nb > 9 && x == 'x')
			i += ft_putchar(nb - 10 + 'a');
	}
	return (i);
}
