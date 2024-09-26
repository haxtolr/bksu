/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_com2.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/09 00:33:09 by heecjang          #+#    #+#             */
/*   Updated: 2023/03/09 01:09:07 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_rrotae(t_node **stack, char *str);
void	ft_rrr(t_node **stack_a, t_node **stack_b);

void	ft_rrotae(t_node **stack, char *str)
{
	t_node	*temp;
	t_node	*be_last;

	if (ft_stack_size(*stack) < 2)
		return ;
	temp = ft_stack_last(*stack);
	be_last = ft_stack_before_last(*stack);
	be_last->next = NULL;
	temp->next = *stack;
	*stack = temp;
	if (str)
		ft_putstr(str);
}

void	ft_rrr(t_node **stack_a, t_node **stack_b)
{
	ft_rrotae(stack_a, 0);
	ft_rrotae(stack_b, 0);
	ft_putstr("rrr");
}
