import os

# función que limpia la terminal para mejorar la experiencia de usuario
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# valor inicial de la opción del menú
option = None

# lista inicial de productos
products = [
    [
        1,
        "Monitor 24'",
        197000,
        10
    ],
    [
        2,
        "Gabinete PC",
        77000,
        12,
    ],
    [
        3,
        "Teclado y Mouse",
        52000,
        20
    ]
]

# bucle principal que muestra el menú
while option != "3":
    
    clear()
    # si la opción es 1, el sistema gestiona agregar un producto
    if(option == "1"):  
        # valor inicial de la variable que luego se utiliza para verificar los datos del producto
        confirm = None

        # bucle que muestra carga el producto, hasta que no se confirme la verificación
        while confirm != "s" :
            clear()
            confirm = ""
            print("*"*16)
            print("AGREGAR PRODUCTO")
            print("*"*16 + "\n")
            
            # solicitud de datos del producto
            product = input("Ingrese la descripción del producto: ")
            price = None
            # valida que el precio sea un valor numérico (decimal)
            while type(price) != float:
                try:
                    price = float(input("Ingrese el precio por unidad: "))
                except :         
                    print("\nERROR: Debe ingresar un valor válido (para separar decimales, utilice un punto .)\n")
            stock = 0
            # valida que el stock debe ser mayor a 0
            while stock <= 0 :
                try:
                    stock = int(input("Ingrese la cantidad: "))
                except :         
                    print("\nERROR: Debe ingresar un valor numérico\n")
                    continue
                
                if(stock <= 0):
                    print("\nERROR: Debe ingresar una cantidad válida\n")
            
            clear()
            print("*"*16)
            print("AGREGAR PRODUCTO")
            print("*"*16 + "\n")
            
            # muestra los datos ingresados
            print("Ha ingresado los siguientes datos:\n")
            print("PRODUCTO: " + product)
            print(f"PRECIO: {price}" )
            print(f"STOCK: {stock}")
            
            # confirma los datos ingresados
            while confirm.lower() != "s" and confirm.lower() != "n" :
                confirm = input("Los datos son correctos? S/N ")
                if(confirm.lower() != "s" and confirm.lower() != "n"):
                    continue
        # obtiene el último ID
        lastIndex = products[len(products) - 1][0]
        # agrega el producto a la lista
        products.append([
            lastIndex + 1,
            product,
            price,
            stock
        ])
        # muestra un mensaje de éxito
        print("\nMENSAJE: Producto agregado con éxito")
        input("\nPresione una tecla...")
    # si la opción es 2, el sistema gestiona listar los productos por terminal.
    elif(option == "2"):
        print("*"*20)
        print("LISTADO DE PRODUCTOS")
        print("*"*20 + "\n")
        index = 0
        # establece el espacio en el tabulador de los títulos y lo imprime por terminal
        print("ID\t" + "PRODUCTO\t".expandtabs(30) + "PRECIO\t".expandtabs(20) + "STOCK")
        # recorre la lista y muestra los productos
        while index < len(products) :
            # establece el espacio en el  tabulador de cada registro y lo imprime por terminal
            print(f"{products[index][0]}\t" + f"{products[index][1]}\t".expandtabs(30) + f"$ {products[index][2]:,.2f}\t".expandtabs(20) + f"{products[index][3]}")
            index += 1
        input("\nPresione una tecla...")
    # si es cualquiera otra opción distinta a la inicial, muestra un mensaje de error
    elif(option != None):
        print("\nERROR: Opción no válida")   
        input("\nPresione una tecla...")
    # menú interactivo
    clear()
    print("*"*16)
    print("MENÚ INTERACTIVO")
    print("*"*16)
    print("1. AGREGAR PRODUCTOS")
    print("2. LISTAR PRODUCTO")
    print("3. SALIR\n")
    option = input("Seleccione una opción: ")
# mensaje de salida
print("\nGRACIAS POR UTILIZAR NUESTRO SISTEMA!!!")
