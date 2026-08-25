# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/23 17:04:28 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/23 17:40:14 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	seed_name = seed_type.capitalize()
	if unit == "packets":
		print(f"{seed_type} seeds: {quantity} packets available")
	elif unit == "grams":
		print(f"{seed_name} seeds: {quantity} grams total")
	elif unit == "area":
		print(f"{seed_name} seeds: covers {quantity} square meters")
	else:
		print("Unknown unit type")
