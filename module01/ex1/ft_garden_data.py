# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/24 20:37:22 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/24 21:13:58 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	name: str
	height: int
	age: int

	def show(self) -> None:
		print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
	rose = Plant()
	name = "Rose"
