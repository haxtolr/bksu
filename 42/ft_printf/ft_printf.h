/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/12/21 17:19:28 by heecjang          #+#    #+#             */
/*   Updated: 2022/12/22 23:17:54 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

size_t	ft_strlen(const char *s);
int		ft_printf(const char *format, ...);
void	ft_check(const char *format, va_list ap, int i, int *con);
int		ft_putchar(char c);
int		ft_putstr(char *str);
int		ft_p_hex(void *hex);
int		ft_putnbr(int nb);
int		ft_putunnbr(unsigned int nb);
int		ft_putnbr_hex(unsigned int nb, char x);
int		ft_hex(void *hex);

#endif