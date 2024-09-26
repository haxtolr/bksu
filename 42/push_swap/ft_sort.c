/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/02/28 22:37:54 by heecjang          #+#    #+#             */
/*   Updated: 2023/03/09 01:45:21 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_sort(t_node **stack_a, t_node **stack_b);
void	ft_cut_three(t_node **stack_a, t_node **stack_b);
int		hi_index(t_node *stack);
void	ft_small_sort(t_node **stack);
void	move_stack(t_node **stack_a);

void	ft_sort(t_node **stack_a, t_node **stack_b)
{
	ft_cut_three(stack_a, stack_b);
	ft_small_sort(stack_a);
	while (*stack_b)
	{
		check_target(stack_a, stack_b);
		ft_get_cost(stack_a, stack_b);
		ft_cal(stack_a, stack_b);
	}
	if (!check_sort(*stack_a))
		move_stack(stack_a);
}

void	ft_cut_three(t_node **stack_a, t_node **stack_b)
{
	int	stack_size;
	int	push;
	int	i;

	stack_size = ft_stack_size(*stack_a);
	push = 0;
	i = 0;
	while (stack_size > 6 && i < stack_size && push < stack_size / 2)
	{
		if ((*stack_a)->index <= stack_size / 2)
		{
			ft_push(stack_a, stack_b, "pb");
			push++;
		}
		else
			ft_rotate(stack_a, "ra");
		i++;
	}
	while (stack_size - push > 3)
	{
		ft_push(stack_a, stack_b, "pb");
		push++;
	}
}

void	ft_small_sort(t_node **stack)
{
	int	hi;

	if (check_sort(*stack))
		return ;
	hi = hi_index(*stack);
	if ((*stack)->index == hi)
		ft_rotate(stack, "ra");
	else if ((*stack)->next->index == hi)
		ft_rrotae(stack, "rra");
	if ((*stack)->index > (*stack)->next->index)
		ft_swap(stack, "sa");
}

int	hi_index(t_node *stack)
{
	int	i;

	i = stack->index;
	while (stack)
	{
		if (stack->index > i)
			i = stack->index;
		stack = stack->next;
	}
	return (i);
}

void	move_stack(t_node **stack_a)
{
	int	low_pos;
	int	stack_size;

	stack_size = ft_stack_size(*stack_a);
	low_pos = check_low_index_pos(stack_a);
	if (low_pos > stack_size / 2)
	{
		while (low_pos < stack_size)
		{
			ft_rrotae(stack_a, "rra");
			low_pos++;
		}
	}
	else
	{
		while (low_pos > 0)
		{
			ft_rotate(stack_a, "ra");
			low_pos--;
		}
	}
}
