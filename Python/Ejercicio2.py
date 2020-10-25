#print('Validación contraseña de usuario')
#password = input('Por favor ingrese una contraseña para validarla: ')

def ValidarTamaño(password):

	lengthPass = len(password)

	if lengthPass < 8:
		print('La contraseña debe tener más de 8 caracteres')
		respuesta = False
	else:
		respuesta = True
	return respuesta



def ValidarCracteres(password):

	mayu = password.islower()
	minu = password.isupper()
	alfn = password.isalnum()
	vaci = password.split()
	comodin = False

	for x in vaci:
		aux = x.isspace()
		if aux:
			comodin = True

	if mayu == False and minu == False and alfn == False and comodin == False:
		respuesta = True
	else: 
		print('Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico y no tener espacios')
		respuesta = False

	return respuesta


#respuestaTamaño = ValidarTamaño(password)
#respuestaCaracteres = ValidarCracteres(password)

#if respuestaTamaño and respuestaCaracteres:
#	print(True)
#else:
#	print(False)