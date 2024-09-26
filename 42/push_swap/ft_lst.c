/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lst.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/08 20:55:12 by heecjang          #+#    #+#             */
/*   Updated: 2023/03/09 02:45:18 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int		ft_stack_size(t_node *stack);
t_node	*stack_new(int content);
t_node	*ft_stack_last(t_node *stack);
t_node	*ft_stack_before_last(t_node *stack);
void	ft_stack_add_back(t_node **stack, t_node *lnew);

t_node	*ft_stack_last(t_node *stack)
{
	if (!stack)
		return (NULL);
	while (stack->next)
		stack = stack->next;
	return (stack);
}

t_node	*ft_stack_before_last(t_node *stack)
{
	if (!stack)
		return (NULL);
	while (stack->next && stack->next->next)
		stack = stack->next;
	return (stack);
}

t_node	*stack_new(int content)
{
	t_node	*lnew;

	lnew = malloc(sizeof(t_node));
	if (!lnew)
		return (NULL);
	lnew -> content = content;
	lnew->index = 0;
	lnew->cost_a = -1;
	lnew->cost_b = -1;
	lnew->pos = -1;
	lnew->target_pos = -1;
	lnew -> next = NULL;
	return (lnew);
}

void	ft_stack_add_back(t_node **stack, t_node *lnew)
{
	t_node	*tail;

	if (!lnew)
		return ;
	if (!*stack)
	{
		*stack = lnew;
		return ;
	}
	tail = ft_stack_last(*stack);
	tail->next = lnew;
}

int	ft_stack_size(t_node *stack)
{
	int	size;

	size = 0;
	if (!stack)
		return (0);
	while (stack)
	{
		stack = stack->next;
		size++;
	}
	return (size);
}
