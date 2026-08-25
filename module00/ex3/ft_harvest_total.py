# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/23 13:23:04 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/23 13:31:43 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total() -> None:
	day_1 = int(input("Day 1 harvest: "))
	day_2 = int(input("Day 2 harvest: "))
	day_3 = int(input("Day 3 harvest: "))
	total = day_1 + day_2 + day_3
	print(f"Total harvest: {total}")
