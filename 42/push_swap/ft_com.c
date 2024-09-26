/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_com.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/01 02:42:07 by heecjang          #+#    #+#             */
/*   Updated: 2023/03/09 01:41:26 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_rotate(t_node **stack, char *str);
void	ft_rr(t_node **stack_a, t_node **stack_b);
void	ft_swap(t_node **stack, char *str);
void	ft_ss(t_node **stack_a, t_node **stack_b);
void	ft_push(t_node **stack, t_node **dst, char *str);

void	ft_swap(t_node **stack, char *str)
{
	int	temp;

	if (ft_stack_size(*stack) > 1)
	{
		temp = (*stack)->content;
		(*stack)->content = (*stack)->next->content;
		(*stack)->next->content = temp;
		temp = (*stack)->index;
		(*stack)->index = (*stack)->next->index;
		(*stack)->next->index = temp;
		if (str)
			ft_putstr(str);
	}
}

void	ft_ss(t_node **stack_a, t_node **stack_b)
{
	ft_swap(stack_a, 0);
	ft_swap(stack_b, 0);
	ft_putstr("ss");
}

void	ft_push(t_node **stack, t_node **dst, char *str)
{
	t_node	*temp;

	if ((*stack) == NULL)
		return ;
	temp = (*stack)->next;
	(*stack)->next = *dst;
	*dst = *stack;
	*stack = temp;
	if (str)
		ft_putstr(str);
}

void	ft_rotate(t_node **stack, char *str)
{
	t_node	*temp;
	t_node	*last;

	if (ft_stack_size(*stack) < 2)
		return ;
	temp = *stack;
	*stack = (*stack)->next;
	last = ft_stack_last(*stack);
	temp->next = NULL;
	last->next = temp;
	if (str)
		ft_putstr(str);
}

void	ft_rr(t_node **stack_a, t_node **stack_b)
{
	ft_rotate(stack_a, 0);
	ft_rotate(stack_b, 0);
	ft_putstr("rr");
}
