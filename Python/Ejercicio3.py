import Ejercicio1
import Ejercicio2

print('Validación credenciales de usuario')
NombreUsuario = input('Por favor ingrese un nombre para validarlo: ')
password = input('Por favor ingrese una contraseña para validarla: ')

respuestaTamaño = Ejercicio1.ValidarTamaño(NombreUsuario)
respuestaAlfanum = Ejercicio1.ValidarAlfanumerico(NombreUsuario)
respuestaTamañoPass = Ejercicio2.ValidarTamaño(password)
respuestaCaracteres = Ejercicio2.ValidarCracteres(password)

if respuestaTamaño and respuestaAlfanum and respuestaTamañoPass and respuestaCaracteres:
	print(True)
else:
	print(False)