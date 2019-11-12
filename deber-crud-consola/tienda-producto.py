class Controller:
    filename="./"

    def __init__(self, filename):
        self.filename = filename
    
    def select(self, id):
        f = open(self.filename, "r")
        records = f.readlines()
        toReturn = []
        if(id == ""):
            for record in records:
                toReturn.append(record.rstrip().split(", "))
            return toReturn
        for record in records:
            toReturn = record.rstrip().split(", ")
            current_id = toReturn[0]
            if(current_id == id):
                return toReturn
        return []
    
    def insert(self, toWrite):
        text = ', '.join(str(value) for value in toWrite)
        f = open(self.filename, "a")
        f.write(text + "\n")

    def delete(self, id):
        f = open(self.filename, "r")
        records = f.readlines()
        f = open(self.filename, "w")
        for record in records:
            currentId = record.rstrip().split(", ")[0]
            if(currentId != id):
                f.write(record)

    def update(self, id, content):
        self.delete(id)
        self.insert(content)

class Store(Controller):

    id = 0
    name = ""
    address = ""
    filename = "stores.txt"

    def __init__(self, id = 0, name = "", address = ""):
        super().__init__(self.filename)
        self.id = id
        self.name = name
        self.address = address
    
    def select(self, id):
        result = super().select(id)
        if(id == ""):
            toReturn = []
            for value in result:
                toReturn.append(Store(value[0], value[1], value[2]))
        else:
            toReturn = Store(result[0], result[1], result[2])
        return toReturn

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.name}, Dirección: {self.address}"

class Product(Controller):

    id = 0
    store = 0
    name = ""
    price = 0.0
    filename = "products.txt"

    def __init__(self, id = 0, store = 0, name = "", price = 0.0):
        super().__init__(self.filename)
        self.id = id
        self.store = store
        self.name = name
        self.price = price
    
    def select(self, id, store):
        result = super().select(id)
        if(id == ""):
            toReturn = []
            for value in result:
                toReturn.append(Product(value[0], value[1], value[2], value [3]))
            toReturn = self.filter(toReturn, store)
        else:
            if(result[1] == store):
                toReturn = Product(result[0], result[1], result[2], result[3])
        return toReturn
    
    def filter(self, products_list, store):
        toReturn = []
        for product in products_list:
            if(product.store == store):
                toReturn. append(product)
        return toReturn
    
    def __str__(self):
        return f"ID: {self.id}, Tienda: {self.store}, Nombre: {self.name}, Precio: {self.price}"

#consola
def max_id(items):
    max_value = 0
    for item in items:
        if(int(item.id) > max_value):
            max_value = int(item.id)
    return max_value


option = 0
stores_list = Store().select("")

while(option != "5"):
    print("Bienvenido al sistema")
    print("1. Administrar tienda")
    print("2. Ingresar tienda")
    print("3. Eliminar tienda")
    print("4. Mostrar tiendas")
    print("5. Salir")

    option = input("Seleccione una opción: ")
    if(option == "1"):

        store_option = 0
        store_id = input("Ingrese el ID de la tienda: ")
        products_list = Product().select("", store_id)

        while(store_option != "7"):
            print("1. Editar tienda")
            print("2. Ver productos")
            print("3. Eliminar producto")
            print("4. Buscar producto")
            print("5. Insertar producto")
            print("6. Editar producto")
            print("7. Atras")
            store_option = input("Seleccione una opción: ")
            if(store_option == "1"):
                name = input("Ingrese el nuevo nombre de la tienda: ")
                address = input("Ingrese la nueva dirección: ")
                stores_list[0].update(store_id, [store_id, name, address])
            elif(store_option == "2"):
                products_list = Product().select("", store_id)
                for product in products_list:
                    print(product)
            elif(store_option == "3"):
                to_delete = input("Ingrese el ID del producto: ")
                products_list[0].delete(to_delete)
            elif(store_option == "4"):
                to_select = input("Ingrese el ID del producto: ")
                product = products_list[0].select(to_select, store_id)
                print(product)
            elif(store_option == "5"):
                new_id = str(max_id(products_list) + 1)
                name = input("Ingrese el nombre del nuevo producto: ")
                price = input("Ingrese el precio del nuevo producto: ")
                Product().insert([new_id, store_id, name, price])
            elif(store_option == "6"):
                product_id = input("Ingrese el ID del producto: ")
                name = input("Ingrese el nuevo nombre del producto: ")
                price = input("Ingrese el nuevo precio del producto: ")
                products_list[0].update(product_id, [product_id, store_id, name, price])
    elif(option == "2"):
        store_id = str(max_id(stores_list) + 1)
        name = input("Ingrese el nombre de la nueva tienda: ")
        address = input("Ingrese la dirección: ")
        stores_list[0].insert([store_id, name, address])
        stores_list = stores_list[0].select("")
    elif(option == "3"):
        store_id = input("Ingrese el ID de la tienda: ")
        stores_list[0].delete(store_id)
        stores_list = stores_list[0].select("")
    elif(option == "4"):
        for store in stores_list:
            print(store)



