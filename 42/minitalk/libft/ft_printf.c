/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/20 01:52:43 by heecjang          #+#    #+#             */
/*   Updated: 2023/01/16 04:33:37 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int		ft_printf(const char *format, ...);
void	ft_check(const char *format, va_list ap, int i, int *con);

int	ft_printf(const char *format, ...)
{
	va_list	ap;
	int		i;
	int		con;

	con = 0;
	i = 0;
	va_start(ap, format);
	while (format[i])
	{
		if (format[i] == '%')
		{
			i++;
			ft_check(format, ap, i, &con);
		}
		else
			con += ft_putchar(format[i]);
		i++;
	}
	va_end(ap);
	return (con);
}

void	ft_check(const char *format, va_list ap, int i, int *con)
{
	if (format[i] == '%')
		*con += ft_putchar('%');
	if (format[i] == 'c')
		*con += ft_putchar(va_arg(ap, int));
	if (format[i] == 's')
		*con += ft_putstr(va_arg(ap, char *));
	if (format[i] == 'p')
		*con += ft_p_hex(va_arg(ap, void *));
	if (format[i] == 'd' || format[i] == 'i')
		*con += ft_putnbr(va_arg(ap, int));
	if (format[i] == 'u')
		*con += ft_putunnbr(va_arg(ap, int));
	if (format[i] == 'x')
		*con += ft_putnbr_hex(va_arg(ap, unsigned), 'x');
	if (format[i] == 'X')
		*con += ft_putnbr_hex(va_arg(ap, unsigned), 'X');
}
