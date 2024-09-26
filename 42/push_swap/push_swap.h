/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: heecjang <heecjang@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/02/28 19:26:12 by heecjang          #+#    #+#             */
/*   Updated: 2023/03/09 02:50:05 by heecjang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <unistd.h>
# include <stdlib.h>

typedef struct s_node
{
	int				content;
	int				index;
	int				pos;
	int				target_pos;
	int				cost_a;
	int				cost_b;
	struct s_node	*next;
}	t_node;

int			ft_empty(char *av);
int			ft_two(char **av);
int			check_av(char **av);
int			ft_nbabs(int nb);
int			nb_check(char *s1, char *s2);
int			ft_nbr(char *av);
int			ft_zero(char *av);
t_node		*fill_stack(int ac, char **av);
void		init_index(t_node *stack_a, int size);
void		push_swap(t_node **stack_a, t_node **stack_b, int stack_size);
int			check_sort(t_node *stack);
void		check_target(t_node **a, t_node **b);
void		check_target_wh(t_node **stack);
int			check_target_sel(t_node **a, int b_idx, int tar_idx, int tar_pos);
int			check_low_index_pos(t_node **stack);
void		ft_sort(t_node **stack_a, t_node **stack_b);
void		ft_cut_three(t_node **stack_a, t_node **stack_b);
int			hi_index(t_node *stack);
void		ft_small_sort(t_node **stack);
void		move_stack(t_node **stack_a);
void		ft_rotate_both(t_node **stack_a, t_node **stack_b, \
	int *cost_a, int *cost_b);
void		ft_rotate_a(t_node **stack_a, int *cost);
void		ft_rotate_b(t_node **stack_a, int *cost);
void		ft_rev_rotate_both(t_node **stack_a, t_node **stack_b, \
	int *cost_a, int *cost_b);
void		move(t_node **stack_a, t_node **stack_b, int cost_a, int cost_b);
int			ft_stack_size(t_node *stack);
t_node		*stack_new(int content);
t_node		*ft_stack_last(t_node *stack);
t_node		*ft_stack_before_last(t_node *stack);
void		ft_stack_add_back(t_node **stack, t_node *lnew);
void		ft_rrotae(t_node **stack, char *str);
void		ft_rrr(t_node **stack_a, t_node **stack_b);
void		ft_rotate(t_node **stack, char *str);
void		ft_rr(t_node **stack_a, t_node **stack_b);
void		ft_swap(t_node **stack, char *str);
void		ft_ss(t_node **stack_a, t_node **stack_b);
void		ft_push(t_node **stack, t_node **dst, char *str);
char		**check_tab(char **av, int *size, int ac);
void		ft_error(t_node **stack_a, t_node **stack_b);
void		ft_sfree(t_node **stack);
void		ft_get_cost(t_node **stack_a, t_node **stack_b);
void		ft_cal(t_node **stack_a, t_node **stack_b);
long int	ft_atoi(const char *str);
int			is_digit(char c);
int			is_sign(char c);
void		ft_putstr(char *str);
char		*str_ndup(char *str, unsigned int n);
char		**ft_split(char *str, char c, int *size);
size_t		ft_strlen(const char *s);
char		*ft_strjoin(char *s1, char *s2);

#endif