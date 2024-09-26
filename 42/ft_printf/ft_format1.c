/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_format1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/22 18:25:32 by heecjang          #+#    #+#             */
/*   Updated: 2022/12/22 22:57:16 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putchar(char c)
{
	write(1, &c, 1);
	return (1);
}

int	ft_putstr(char *str)
{
	if (!str)
		return (ft_putstr("(null)"));
	else
		write(1, str, ft_strlen(str));
	return (ft_strlen(str));
}

int	ft_p_hex(void *hex)
{
	int	i;

	i = 0;
	if (!hex)
	{
		i += ft_putstr("0x0");
		return (i);
	}
	i += ft_putstr("0x");
	i += ft_hex(hex);
	return (i);
}

int	ft_hex(void *hex)
{
	int					i;
	unsigned long int	b;

	i = 0;
	b = (unsigned long int)hex;
	if (b >= 16)
	{
		i += ft_hex((void *)(b / 16));
		i += ft_hex((void *)(b % 16));
	}
	else
	{
		if (b < 10)
			i += ft_putchar(b + '0');
		if (b > 9)
			i += ft_putchar(b - 10 + 'a');
	}
	return (i);
}

int	ft_putnbr(int nb)
{
	long	num;
	int		i;

	i = 0;
	num = nb;
	if (num < 0)
	{
		num = -num;
		i += ft_putchar('-');
	}
	if (num >= 10)
	{
		i += ft_putnbr(num / 10);
		i += ft_putnbr(num % 10);
	}
	else
		i += ft_putchar(num + '0');
	return (i);
}
