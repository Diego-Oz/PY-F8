#Estructura del Proyecto
El proyecto está estructurado de la siguiente manera:
main.py: Contiene la lógica para la gestión de contactos.
Login.py: Contiene la lógica para la autenticación de usuarios.
contactModel.py: Define la clase ContactModel para la gestión de contactos.
test_main.py: Archivo de pruebas unitarias para el módulo de gestión de contactos.
test_login.py: Archivo de pruebas unitarias para el módulo de autenticación de usuarios.

Funcionalidades del Código
login.py
login(user, password): Esta función verifica las credenciales del usuario y devuelve True si son válidas, de lo contrario, devuelve False.

main.py
ContactModel.get_contacts(): Método estático que devuelve una lista de contactos.
ContactModel.get_contact_by_id(id): Método estático que devuelve un contacto basado en su ID.

Pruebas Unitarias
test_login.py
test_login_pass(): Verifica que la función de autenticación devuelve True con credenciales válidas.
test_login_fail_wrong_user(): Verifica que la función de autenticación no tenga el usuario incorrecto.
test_login_fail_wrong_password(): Verifica que la función de autenticación no tenga la clave incorrecta.

test_login_fail_wrong_user_and_password(): Verifica que la función de autenticación no tenga el usuario y la clave incorrectos.

test_main.py
test_get_contacts_not_none(): Verifica que la lista de contactos no sea nula.
test_get_contacts_has_elements(): Verifica que la lista de contactos contenga al menos un elemento.
test_get_contact_by_id_not_none(): Verifica que la función para obtener un contacto por ID no devuelva None.
test_get_contact_by_id_has_correct_id(): Verifica que la función para obtener un contacto por ID devuelva el contacto correcto basado en su ID.

Ejecución de Pruebas Unitarias
Para ejecutar las pruebas unitarias, se debe utilizar la biblioteca Pytest. Desde la línea de comandos, se puede ejecutar el comando pytest -v en el directorio raíz del proyecto. Pytest buscará automáticamente todos los archivos de pruebas en el proyecto y ejecutará todas las funciones de prueba que encuentre.
