# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/23 14:35:07 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/23 16:54:48 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(days) -> None:
	days = int(input("Days until harvest: "))

	def print_day(day: int) -> None:
		if day > days:
			return
		print(f"days: {day}")
		print_day(day + 1)

	print_day(1)
	print("Harvest time!")
