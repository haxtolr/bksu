/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/02/28 02:46:22 by heecjang          #+#    #+#             */
/*   Updated: 2023/03/09 03:10:35 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_node	*fill_stack(int ac, char **av);
void	init_index(t_node *stack_a, int size);
void	push_swap(t_node **stack_a, t_node **stack_b, int stack_size);
int		check_sort(t_node *stack);

int	main(int ac, char **av)
{
	t_node	*stack_a;
	t_node	*stack_b;
	int		size;
	char	**tab;

	tab = check_tab(av, &size, ac);
	if (!check_av(tab))
		ft_error(NULL, NULL);
	stack_a = fill_stack(size, tab);
	stack_b = NULL;
	size = ft_stack_size(stack_a);
	init_index(stack_a, size + 1);
	push_swap(&stack_a, &stack_b, size);
	ft_sfree(&stack_a);
	ft_sfree(&stack_b);
	return (0);
}

int	check_sort(t_node *stack)
{
	while (stack->next)
	{
		if (stack->content > stack->next->content)
			return (0);
		stack = stack->next;
	}
	return (1);
}

void	push_swap(t_node **stack_a, t_node **stack_b, int stack_size)
{
	if (stack_size == 2 && !check_sort(*stack_a))
		ft_swap(stack_a, "sa");
	else if (stack_size == 3)
		ft_small_sort(stack_a);
	else if (stack_size > 3 && !check_sort(*stack_a))
		ft_sort(stack_a, stack_b);
}

void	init_index(t_node *stack_a, int size)
{
	t_node	*ptr;
	t_node	*hi;
	int		content;

	while (--size > 0)
	{
		ptr = stack_a;
		content = -2147483648;
		hi = NULL;
		while (ptr)
		{
			if (ptr->content == -2147483648 && ptr->index == 0)
				ptr->index = 1;
			if (ptr->content > content && ptr->index == 0)
			{
				content = ptr->content;
				hi = ptr;
				ptr = stack_a;
			}
			else
				ptr = ptr->next;
		}
		if (hi != NULL)
			hi->index = size;
	}
}

t_node	*fill_stack(int ac, char **av)
{
	t_node		*stack_a;
	long int	nb;
	int			i;

	stack_a = NULL;
	nb = 0;
	i = 0;
	while (i < ac)
	{
		nb = ft_atoi(av[i]);
		if (nb > 2147483647 || nb < -2147483648)
			ft_error(NULL, NULL);
		if (i == 0)
			stack_a = stack_new((int)nb);
		else
			ft_stack_add_back(&stack_a, stack_new((int)nb));
		i++;
	}
	return (stack_a);
}
