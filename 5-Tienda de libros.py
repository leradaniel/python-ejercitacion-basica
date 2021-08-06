# 5) Tienda de libros
# Pedir al usuario que proporcione información de un libro
# "Proporcione el nombre: " 
# "Proporcione el ID: " (Debe ser entero)
# "Proporcione el precio: " (Debe ser flotante)
# "Indica si  el envío es gratuito (True/False): "
# Mostrar el resultado de la siguiente manera
# "Nombre: "
# "ID: "
# "Precio: "
# "Envio gratuito?: "
print("Proporcione información de un libro:")
nombre = input("Proporcione el nombre: " )
id = int(input("Proporcione el ID: "))
precio = float(input("Proporcione el precio: "))
envio_gratuito = input("Indica si  el envío es gratuito (True/False): ")

if envio_gratuito == "True":
    envio_gratuito = True
elif envio_gratuito == "False":
    envio_gratuito = False
else:
    print("Hubo un error, debe ingresar True o False")

print("La información ingresada es:")
print(f"Nombre: {nombre}")
print(f"ID: {id}")
print(f"Precio: {precio}")
print(f"Envio gratuito?: {envio_gratuito}")