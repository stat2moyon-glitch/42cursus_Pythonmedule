# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/23 13:33:19 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/23 13:40:52 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age() -> None:
	days = int(input("Enter plant age in days: "))
	if days > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
