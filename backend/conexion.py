import pymysql
conexion=pymysql.connect( 
 host='localhost', 
 user='root',
 password='12345678',
 database='buenosasesores')

cursor=conexion.cursor();
cursor.execute("show tables;")
cursor.execute("select * from asesor;")
respuestadBD=cursor.fetchall();

print(respuestadBD)



# Comprometer operaccioes
nombreUsuario = input("Ingrese el nombre de usuario: ")
cursor = conexion.cursor()
cursor.execute("insert into asesor(nombre, email, contrasenia, nombre_usuario,tarifa)" \
" values('Mtro.Zandy Salazar','zsalizar@gmail.com','183fhrnQ/','Zandypsala','80.57');")
conexion.commit();

for registro in respuestadBD:
    print(registro);
