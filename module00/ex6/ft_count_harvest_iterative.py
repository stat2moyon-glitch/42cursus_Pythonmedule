# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/23 13:55:43 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/23 14:18:08 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative() -> None:
	days = int(input("Days until harvest: "))
	for i in range(1, days + 1):
		print(f"day {i}")
	print("Harvest time!")
