/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42seoul.>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/12 17:45:19 by heecjang          #+#    #+#             */
/*   Updated: 2022/07/12 17:54:27 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	print_nbr(char c, int fd);

void	ft_putnbr_fd(int n, int fd)
{
	if (n == -2147483648)
		write(fd, "-2147483648", 11);
	if (n >= 10)
	{
		ft_putnbr_fd(n / 10, fd);
		ft_putnbr_fd(n % 10, fd);
	}
	if (n < 10 && n >= 0)
	{
		n = 48 + n;
		print_nbr(n, fd);
	}
	if (n < 0 && n > -2147483648)
	{
		print_nbr('-', fd);
		ft_putnbr_fd(n * -1, fd);
	}
}

void	print_nbr(char c, int fd)
{
	write(fd, &c, 1);
}
