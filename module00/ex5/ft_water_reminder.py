# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/23 13:42:15 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/23 13:53:31 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder() -> None:
	days = int(input("Days since last watering: "))
	if days < 3:
		print("Plants are fine")
	else:
		print("Water the plants!")
