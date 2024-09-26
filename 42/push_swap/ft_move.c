/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_move.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/09 00:42:33 by heecjang          #+#    #+#             */
/*   Updated: 2023/03/09 01:41:11 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_rotate_both(t_node **stack_a, t_node **stack_b, \
	int *cost_a, int *cost_b);
void	ft_rotate_a(t_node **stack_a, int *cost);
void	ft_rotate_b(t_node **stack_a, int *cost);
void	ft_rev_rotate_both(t_node **stack_a, t_node **stack_b, \
	int *cost_a, int *cost_b);
void	move(t_node **stack_a, t_node **stack_b, int cost_a, int cost_b);

void	move(t_node **stack_a, t_node **stack_b, int cost_a, int cost_b)
{
	if (cost_a < 0 && cost_b < 0)
		ft_rev_rotate_both(stack_a, stack_b, &cost_a, &cost_b);
	else if (cost_a > 0 && cost_b > 0)
		ft_rotate_both(stack_a, stack_b, &cost_a, &cost_b);
	ft_rotate_a(stack_a, &cost_a);
	ft_rotate_b(stack_b, &cost_b);
	ft_push(stack_b, stack_a, "pa");
}

void	ft_rotate_both(t_node **stack_a, t_node **stack_b, \
int *cost_a, int *cost_b)
{
	while (*cost_a > 0 && *cost_b > 0)
	{
		(*cost_a)--;
		(*cost_b)--;
		ft_rr(stack_a, stack_b);
	}
}

void	ft_rev_rotate_both(t_node **stack_a, t_node **stack_b, \
int *cost_a, int *cost_b)
{
	while (*cost_a < 0 && *cost_b < 0)
	{
		(*cost_a)++;
		(*cost_b)++;
		ft_rrr(stack_a, stack_b);
	}
}

void	ft_rotate_a(t_node **stack_a, int *cost)
{
	while (*cost)
	{
		if (*cost > 0)
		{
			ft_rotate(stack_a, "ra");
			(*cost)--;
		}
		else if (*cost < 0)
		{
			ft_rrotae(stack_a, "rra");
			(*cost)++;
		}
	}
}

void	ft_rotate_b(t_node **stack_b, int *cost)
{
	while (*cost)
	{
		if (*cost > 0)
		{
			ft_rotate(stack_b, "rb");
			(*cost)--;
		}
		else if (*cost < 0)
		{
			ft_rrotae(stack_b, "rrb");
			(*cost)++;
		}
	}
}
