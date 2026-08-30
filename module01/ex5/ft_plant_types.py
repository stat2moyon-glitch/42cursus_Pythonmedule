# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/30 21:28:35 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/30 23:00:45 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name: str, height: float, age_days: int) -> None:
		self._name = name
	    self._height = 0.0
	    self._age_days = 0
	    self.set_height(height)
	    self.set_age(age_days)

	def set_height(self, height: float) -> bool:
       if height < 0
