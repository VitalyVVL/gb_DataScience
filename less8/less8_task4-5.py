from abc import ABC, abstractmethod,abstractproperty

class Warehouse:
    def __init__(self, name):
        self.__name = name
        self.__store_items = []
        self.__department_items = []

    def add_item(self, equip):
        i, res_find_el = self.find_element_in_dict(self.__store_items, equip.serial_num)
        if not res_find_el==None:
            self.__store_items[i] = equip.get_dist()
        else:
            self.__store_items.append(equip.get_dict())

    def move_item(self, equip,owner):
        i, res_find_el = self.find_element_in_dict(self.__store_items, equip.serial_num)
        if res_find_el == None:
            raise ValueError(f"{equip.__class__.__name__} нет на складе {self.__name}")
        else:
            self.__store_items.remove(self.__store_items[i])
            equip_desc = equip.get_dict()
            equip_desc['owner'] = owner
            self.__department_items.append(equip_desc)

    def show_warehouse(self):
        if len(self.__store_items)>0:
              print(f'==========Остатки на {self.__name}=============')
        for line in self.__store_items:
            print(f'{line["type"]} серийный номер {line["serial_num"]}')
            print(line)

        if len(self.__department_items) > 0:
            print(f'==========Передано под отчет=============')
        for line in self.__department_items:
             print(f"Владелец {line['owner']}  {line['type']} серийный номер {line['serial_num']}")
             print(line)

    @staticmethod
    def find_element_in_dict(user_list, user_value):
        if len(user_list)==0:
            return None, None
        for i, line in enumerate(user_list):
            if user_value in line.values():
                return i, line
        return  None,None



class Equipment(ABC):
    def __init__(self, vendor_name, serial_num):
        self._vendor_name = vendor_name
        self._serial_num = serial_num

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_dict(self):
        pass

    @property
    def serial_num(self):
        return self._serial_num


class Scanner(Equipment):
    def __init__(self, vendor_name, serial_num, paper_size):
        super().__init__(vendor_name, serial_num)
        self.__size = paper_size

    def get_dict(self):
        return {'type': self.__class__.__name__,'vendor_name':self._vendor_name, 'serial_num':self.serial_num,'size':self.__size, 'owner':''}

    def get_info(self, warehouse):
            owner = Warehouse.get_owner(self)

            if not owner ==None:
                owner_str = 'оргтехника выдата в пользование '+owner
            return f'Оборудование {self.__class__.__name__} производитель {self._vendor_name} серийный номер {self.serial_num} размер листа сканирования {self.__size} {owner_str}'


class Printer(Equipment):
    def __init__(self, vendor_name, serial_num, device_type, paper_size, is_color):
        super().__init__(vendor_name, serial_num)
        self.__type = device_type
        self.__size = paper_size
        self.__is_color = is_color

    def get_dict(self):
        return {'type': self.__class__.__name__,'type':self.__type, 'size':self.__size, 'serial_num':self.serial_num, 'is_color':self.__is_color, 'owner':''}

    def get_info(self, warehouse):
        owner = Warehouse.get_owner(self)
        if not owner == None:
            owner_str = 'оргтехника выдата в пользование ' + owner
        return f'Оборудование {self.__class__.__name__} производитель {self._vendor_name} серийный номер {self.serial_num} тип устройства {self.__type}  размер бумаги {self.__size} принтер цветной {self.__is_color} {owner_str}'


class Xerox(Equipment):
    def __init__(self, vendor_name, serial_num, paper_size, speed_copy):
        super().__init__(vendor_name, serial_num)
        self.__size = paper_size
        self.__speed_copy= speed_copy

    def get_dict(self):
        return {'type': self.__class__.__name__,'vendor_name':self._vendor_name, 'serial_num':self.serial_num,'size':self.__size, 'speed_copy':self.__speed_copy, 'owner':''}

    def get_info(self, warehouse):
        owner = Warehouse.get_owner(self)
        if not owner == None:
            owner_str = 'оргтехника выдата в пользование ' + owner
        return f'Оборудование {self.__class__.__name__} производитель {self._vendor_name} серийный номер {self.serial_num}  размер бумаги {self.__size} скорость печати {self.__speed_copy} {owner_str}'



store = Warehouse("Основной склад")
printer_1 = Printer("HP", "123", "Laser", "A3", False)
printer_2 = Printer("Dell", "456", "Laser", "A4", True)
scaner_1 = Scanner("Konica", "789", "A4")
xerox_1 = Xerox("Xerox", "001", "A3", 200)

store.add_item(printer_1)
store.add_item(printer_2)
store.add_item(scaner_1)
store.add_item(xerox_1)
store.show_warehouse()
print("\n"
      "\n"
      "\n")
store.move_item(printer_2, "Иванов Иван Иванович")
store.show_warehouse()


