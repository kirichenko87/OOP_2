class Potion:
    def __init__(self, potion: str,
                 lst_potion: list,
                 lvl_hard: int, 
                 efect: str                 
                 ):
        
        self.make_potion(potion, lst_potion, lvl_hard, efect)    

        
    def set_status(self, new_status: bool):
        self.__status = new_status
        
    def add_component(self, new_component: str):
        if  new_component in self.__lst_potion:
            return(f"Компонент {new_component} уже присутствует в списке")
        else:
            self.__lst_potion.append(new_component)
        
    def remove_component(self, component: str):
        if not component in self.__lst_potion:
            return(f"Вы ошиблись с компонентом {component} его нет в списке")
        else:
            self.__lst_potion.remove(component)
    
    def set_lvl_hard(self,new_lvl: int):
        if not isinstance(new_lvl, int):
            return f"Type Error {new_lvl}"
        
        if new_lvl < 0 or new_lvl > 10:
            return f"Вы выбрали не допустимый уровень сложности зелья"
        
        self.__lvl_hard = new_lvl
        
    def __cast_potion(self, potion, lst_potion, lvl_hard, efect):
        self.__potion = potion
        self.__lst_potion = lst_potion
        self.set_lvl_hard(lvl_hard) # Попробовал создать поле через метод
        self.__efect = efect
        self.__status = False
    
    def make_potion(self, potion, lst_potion, lvl_hard, efect): # решил попробовать спрятать метод
        self.__cast_potion(potion, lst_potion, lvl_hard, efect)
    
    def get_lst_potion(self):
        lst = ", ".join(self.__lst_potion)
        return lst
    
    def __str__(self):
        return f"Наше чудо зедья называется {self.__potion}, уровень сложности приготовления {self.__lvl_hard}, ингридиенты {self.__lst_potion}, имеет эфект {self.__efect}"

class Program:
    @staticmethod
    
    def main():
        poison = Potion("Отвар бабушки Фарамуж", ["Свежее молоко", "Соленые огурцы", "Селедка под шубой"], 10, "Гарантированный!!!")
        poison.add_component("Кефир")
        poison.add_component("Морковь")
        poison.remove_component("Кефир")
        poison.set_lvl_hard(6)
        print(poison.get_lst_potion())
        print(poison)

Program.main()