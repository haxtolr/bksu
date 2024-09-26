/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ps_utils.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/02/28 19:45:52 by heecjang          #+#    #+#             */
/*   Updated: 2023/03/09 02:39:34 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

char	**check_tab(char **av, int *size, int ac);
void	ft_error(t_node **stack_a, t_node **stack_b);
void	ft_sfree(t_node **stack);
void	ft_get_cost(t_node **stack_a, t_node **stack_b);
void	ft_cal(t_node **stack_a, t_node **stack_b);

char	**check_tab(char **av, int *size, int ac)
{
	char	*join;
	char	**tab;
	int		i;

	i = 1;
	join = NULL;
	if (av[i] == NULL || ac <= 1)
		exit(0);
	while (av[i])
	{
		if (!ft_empty(av[i]))
			ft_error(NULL, NULL);
		join = ft_strjoin(join, av[i]);
		i++;
	}
	tab = ft_split(join, ' ', size);
	free(join);
	return (tab);
}

void	ft_error(t_node **stack_a, t_node **stack_b)
{
	if (stack_a == NULL || *stack_a != NULL)
		ft_sfree(stack_a);
	if (stack_b == NULL || *stack_b != NULL)
		ft_sfree(stack_b);
	write(2, "Error\n", 6);
	exit(1);
}

void	ft_sfree(t_node **stack)
{
	t_node	*tmp;

	if (!stack || !*stack)
		return ;
	while (*stack)
	{
		tmp = (*stack)->next;
		free(*stack);
		*stack = tmp;
	}
	*stack = NULL;
}

void	ft_get_cost(t_node **stack_a, t_node **stack_b)
{
	t_node	*temp_a;
	t_node	*temp_b;
	int		size_a;
	int		size_b;

	temp_a = *stack_a;
	temp_b = *stack_b;
	size_a = ft_stack_size(temp_a);
	size_b = ft_stack_size(temp_b);
	while (temp_b)
	{
		temp_b->cost_b = temp_b->pos;
		if (temp_b->pos > size_b / 2)
			temp_b->cost_b = (size_b - temp_b->pos) * -1;
		temp_b->cost_a = temp_b->target_pos;
		if (temp_b->target_pos > size_a / 2)
			temp_b->cost_a = (size_a - temp_b->target_pos) * -1;
		temp_b = temp_b->next;
	}
}

void	ft_cal(t_node **stack_a, t_node **stack_b)
{
	t_node	*temp;
	int		cal;
	int		cost_a;
	int		cost_b;

	temp = *stack_b;
	cal = 2147483647;
	while (temp)
	{
		if (ft_nbabs(temp->cost_a) + ft_nbabs(temp->cost_b) < ft_nbabs(cal))
		{
			cal = ft_nbabs(temp->cost_b) + ft_nbabs(temp->cost_a);
			cost_a = temp->cost_a;
			cost_b = temp->cost_b;
		}
		temp = temp->next;
	}
	move(stack_a, stack_b, cost_a, cost_b);
}
