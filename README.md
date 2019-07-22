# floppy

> La increíble filosofía de python me cegó (No!, no es por la miopía que tengo!!!), sino el hecho de la simpleza en un solo archivo.

## Instalación y uso

```
git clone https://github.com/DtxdF/floppy
cd ./floppy
python

import floppy


email = '<Dirección de correo electrónico>'
passwd = '<Contraseña>'
smtp_server = '<Dirección del servidor>'
smtp_port = <Puerto>
to = '<Dirección de correo electrónico del destinatario>'
subject = '<Asunto>'
archivo = '<Archivo>'
message = '<Mensaje>'

smtp = floppy.smtp_interact(email, passwd, smtp_server, smtp_port)
smtp.connect()
smtp.login()
smtp.add_message(message)
smtp.add_file(open(archivo, "rb")) # Esto es opcional
smtp.sendmail(to, subject)
smtp.close()
```
