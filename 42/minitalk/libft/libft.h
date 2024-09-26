/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/06 12:35:32 by heecjang          #+#    #+#             */
/*   Updated: 2023/01/16 05:31:32 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H
# define LIBFT_H

# include <stdarg.h>
# include <stdlib.h>
# include <unistd.h>

char	*ft_strjoin(char const *s1, char const *s2);
int		ft_atoi(const char *str);
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
