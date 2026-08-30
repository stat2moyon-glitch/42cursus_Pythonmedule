# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ttatsuno <ttatsuno@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/30 15:08:36 by ttatsuno          #+#    #+#              #
#    Updated: 2026/08/30 20:47:15 by ttatsuno         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name: str, height :float, age_days: int) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        self.set_height(height)
        self.set_age(age_days)

    def set_height(self, height: float) -> bool:
        if height < 0:
               print(f"{self._name}: Error, height can't be negative")
               return False
        self._height = float(height)
        return True

    def set_age_days(self, age_days: int) -> bool:
         if age_days < 0:
              print(f"{self._name}: Error, height can't be negative")
              return False
         self._height = int(age_days)
         return True

    def get_height(self) -> float:
         return self._height

    def get_age(self) -> None:
         return self._age_days

    def show(self) -> None:
         print(
              f"{self._name}: {self._height:.1f}cm, "
              f"{self._age_days} dats old"
		 )

if __name__ == "__main__":
    rose = Plant("Rose, 15.0, 10")

    print("=== Garden Security System ===")
    print("Plant cleated: ", end="")
    rose.show()
    print()

    if rose.set_height(25.0):
        print(f"Height updated: {rose.get_height():g}cm")
    if rose.set_age(30):
       print(f"Age updated: {rose.get_age()} days")
    print()

    if not rose.set_height(-5.0):
         print("Height update rejected")
    if not rose.set_age(-2):
         print("Age update rejected")
    print()

    print("Current state: ", end="")
    rose.show()
