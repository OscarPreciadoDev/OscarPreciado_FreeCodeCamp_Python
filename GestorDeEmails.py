# RESUMEN DE PROYECTO ACADEMICO DE INTRODUCCION DE PROGRAMACION ORIENTADA A OBJETOS UTILIZANDO UN 
# GESTOR DE CORREOS COMO EJEMPLO :)

# Se utilizara la libreria datetime, para gestionar un uso preciso en las horas de envio/recepcion de emails reales
import datetime


# Primer se define como se comportara un objeto tipo email
# Este disponde de los atributos : sender (quien lo envia), receiver (quien lo recibe), subject (asunto), body (cuerpo del correo)
class Email:

    # Constructor de un objeto clase Email
    def __init__(self, sender, receiver, subject, body):

        # Asignacion de los atributos requeridos por el constructor a sus correspondientes variables
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

        # Se asigna el atributo de la hora correspondiente al momento del envio del correo
        self.timestamp = datetime.datetime.now()

        # Por defecto todos los correos se marcaran como no leidos en el momento de ser creados
        self.read = False


    # Un metodo que tiene cada correo que cambiara el estado de no leido a leido cuando sea invocado
    def mark_as_read(self):
        self.read = True


    # Un metodo para formatear la impresion completa de un email en consola
    def display_full_email(self):

        # Se marca como leido (cambia el valor del atributo del email)
        self.mark_as_read()

        # impresion usando cada uno de los atributos del email de instancia
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        # Se formatea la fecha en un formato especifico 
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')


    # Se sobre escribe el metodo de impresion, cuando el correo se quiera imprimir, se imprimira en este formato
    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"



# Dentro del gestor de correos se creara una clase para Usuarios, representa las entidades de diferentes usuarios a los cuales estos tendran como parametros de entrada su nombre unicamente, y se le creara un inbox (definido mas adelante)

class User:
    def __init__(self, name):
        self.name = name
        # Se invoca un inbox cuando se cree un usuario y se le asignara
        self.inbox = Inbox()

    # Un usuario tiene el metodo para enviar correos, para esto debe agregar, el destinatario, el asunto y el cuerpo del correo como parametros al invocar la funcion

    def send_email(self, receiver, subject, body):

        # Se crea un objeto email con los datos recibidos
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)

        # Se envia el correo al inbox del destinatario
        receiver.inbox.receive_email(email)

        # Se imprime un mensaje en consola confirmando el envio del correo 
        print(f"Email sent from [{self.name}] to [{receiver.name}]!\n")

            # Un metodo para consultar la bandeja de entrada del usuario
    def check_inbox(self):

        # Se imprime el nombre del usuario y posteriormente se listan sus correos
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()


    # Un metodo que permite leer un correo indicando su posicion en la bandeja
    def read_email(self, index):

        # Se delega la responsabilidad al inbox del usuario
        self.inbox.read_email(index)


    # Un metodo que permite eliminar un correo indicando su posicion
    def delete_email(self, index):

        # Se delega la responsabilidad al inbox del usuario
        self.inbox.delete_email(index)


# Dentro del gestor de correos como se vio arriba cada usuario tendra un Inbox, que representa el espacio donde se gestionaran sus correos recibidos
class Inbox:
    def __init__(self):

        # El email es una lista donde cada espacio corresponde a un correo, este se inicia vacio
        self.emails = []

    # Una funcion que recibe emails, el unico parametro que recibe es un objeto tipo Email
    def receive_email(self, email):
        # Se agrega el email a la lista de emails
        self.emails.append(email)

    # Un metodo para listar los emails actuales en el inbox
    def list_emails(self):

        # Si no hay emails
        if not self.emails:

            # Imprime un mensaje indicando que no hay emails en bandeja
            print('Your inbox is empty.\n')
            return

        # Sino, (es decir que hay emails), imprime los emails (formateados) con un enumerate 
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')


    # Un metodo que lee un email de la bandeja, recibe como parametro el index visual del correo
    def read_email(self, index):

        # Si no hay emails
        if not self.emails:
            print('Inbox is empty.\n')
            return

        # Sino (ajusta el index restando uno, ya que el visual suma 1 siempre)
        actual_index = index - 1

        # Verifica que el index este dentro del rango real de la lista de emails
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        # Si todo esta en orden, usa el metodo full email para desplegarlo en consola
        self.emails[actual_index].display_full_email()

    # Un metodo que elimina un email, recibiendo un index como parametro unicamente
    def delete_email(self, index):

        # Si no hay emails
        if not self.emails:
            print('Inbox is empty.\n')
            return

        # Ajusta el index
        actual_index = index - 1

        # Verifica que el index este dentro del rango real de la lista de emails
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        
        del self.emails[actual_index]
        print('Email deleted.\n')


# Funcion principal del programa
# Aqui se crean algunos usuarios y se simula el envio de correos
def main():

    # Se crean dos usuarios
    tory = User('Tory')
    ramy = User('Ramy')

    # Se envian algunos correos de prueba
    tory.send_email(
        ramy,
        'Hello',
        'Hi Ramy, just saying hello!'
    )

    ramy.send_email(
        tory,
        'Re: Hello',
        'Hi Tory, hope you are fine.'
    )

    # Se consulta la bandeja de entrada de ambos usuarios
    tory.check_inbox()
    ramy.check_inbox()

    # Se hacen algunas pruebas adicionales, de leer un email, eliminar un email, chequear el inbox etc...
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()


# Punto de entrada del programa
# Solo ejecuta main() cuando este archivo se ejecuta directamente
if __name__ == '__main__':
    main()


# SALIDA DEL PROGRAMA

# Email sent from Tory to Ramy!
#
# Email sent from Ramy to Tory!
#
# Ramy's Inbox:
#
# Your Emails:
# 1. [Unread] From: Tory | Subject: Hello | Time: 2026-07-30 18:26
#
# --- Email ---
# From: Tory
# To: Ramy
# Subject: Hello
# Received: 2026-07-30 18:26
# Body: Hi Ramy, just saying hello!
# ------------
#
# Email deleted.
#
# Ramy's Inbox:
# Your inbox is empty.