/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_where.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/08 23:12:36 by heecjang          #+#    #+#             */
/*   Updated: 2023/03/09 03:05:58 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	check_target(t_node **a, t_node **b);
void	check_target_wh(t_node **stack);
int		check_target_sel(t_node **a, int b_idx, int tar_idx, int tar_pos);
int		check_low_index_pos(t_node **stack);

void	check_target(t_node **a, t_node **b)
{
	t_node	*temp_b;
	int		i;

	temp_b = *b;
	check_target_wh(a);
	check_target_wh(b);
	i = 0;
	while (temp_b)
	{
		i = check_target_sel(a, temp_b->index, 2147483647, i);
		temp_b->target_pos = i;
		temp_b = temp_b->next;
	}
}

int	check_target_sel(t_node **a, int b_idx, int tar_idx, int tar_pos)
{
	t_node	*temp_a;

	temp_a = *a;
	while (temp_a)
	{
		if (temp_a->index > b_idx && temp_a->index < tar_idx)
		{
			tar_idx = temp_a->index;
			tar_pos = temp_a->pos;
		}
		temp_a = temp_a->next;
	}
	if (tar_idx != 2147483647)
		return (tar_pos);
	temp_a = *a;
	while (temp_a)
	{
		if (temp_a->index < tar_idx)
		{
			tar_idx = temp_a->index;
			tar_pos = temp_a->pos;
		}
		temp_a = temp_a->next;
	}
	return (tar_pos);
}

void	check_target_wh(t_node **stack)
{
	t_node	*temp;
	int		i;

	temp = *stack;
	i = 0;
	while (temp)
	{
		temp->pos = i;
		temp = temp->next;
		i++;
	}
}

int	check_low_index_pos(t_node **stack)
{
	t_node	*temp;
	int		low_i;
	int		low_p;

	temp = *stack;
	low_i = 2147483647;
	check_target_wh(stack);
	low_p = temp->pos;
	while (temp)
	{
		if (temp->index < low_i)
		{
			low_i = temp->index;
			low_p = temp->pos;
		}
		temp = temp->next;
	}
	return (low_p);
}
