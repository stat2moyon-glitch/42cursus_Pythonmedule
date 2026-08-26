# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/24 20:37:22 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/26 18:47:46 by ttatsuno         ###   ########.fr        #
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
	rose.height = 25
	rose.age_days = 30

	sunflower = Plant()
	sunflower.name = "Sunflower"
	sunflower.height = 80
	sunflower.age_days = 45

	cactus = Plant()
	cactus.name = "Cactus"
	cactus.height = 15
	cactus.age_days = 120

	print("=== Garden Plant Registry ===")
	rose.show()
	sunflower.show()
	cactus.show()
