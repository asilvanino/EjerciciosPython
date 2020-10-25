#print('Validación nombre de usuario')
#NombreUsuario = input('Por favor ingrese un nombre para validarlo: ')

def ValidarTamaño(Nombre):

	lengthNombre = len(Nombre)
	respuesta = 1

	if lengthNombre < 6:
		print('El nombre de usuario debe contener al menos 6 caracteres')
		respuesta = 0
	if lengthNombre > 12:
		print('El nombre de usuario no puede contener más de 12 caracteres')
		respuesta = 0

	return respuesta



def ValidarAlfanumerico(Nombre):
	respuesta = 0
	validate = Nombre.isalnum()

	if validate:
		respuesta = 1
		return respuesta
	else:
		print('El nombre de usuario puede contener solo letras y números')
		return respuesta


#respuestaTamaño = ValidarTamaño(NombreUsuario)
#respuestaAlfanum = ValidarAlfanumerico(NombreUsuario)

#if respuestaTamaño == 1 and respuestaAlfanum == 1:
#	print(True)
#else:
#	print(False)
