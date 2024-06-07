import pynput.mouse as mouse
import pynput.keyboard as keyboard
import threading

# Controladores 
mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()


control_activo = False

#funciones
def mover_arriba():
    mouse_controller.move(0, -15)

def mover_abajo():
    mouse_controller.move(0, 15)

def mover_izquierda():
    mouse_controller.move(-15, 0)

def mover_derecha():
    mouse_controller.move(15, 0)

def click_izquierdo():
    mouse_controller.click(mouse.Button.left, 1)

def click_derecho():
    mouse_controller.click(mouse.Button.right, 1)

# switch control_activo
def toggle_control():
    global control_activo
    control_activo = not control_activo
    # if control_activo:
    #     print("Control de ratón activado")
    # else:
    #     print("Control de ratón desactivado")

# escucha las teclas
def on_press(key):
    if control_activo:
        try:
            if key == keyboard.Key.up:
                mover_arriba()
            elif key == keyboard.Key.down:
                mover_abajo()
            elif key == keyboard.Key.left:
                mover_izquierda()
            elif key == keyboard.Key.right:
                mover_derecha()
            elif key.char == '-':
                click_izquierdo()
            elif key.char == '´':
                click_derecho()
        except AttributeError:
            pass

def on_release(key):
    # Activar/desactivar el control del ratón con la tecla 'esc'
    if key == keyboard.Key.esc:
        toggle_control()

# Iniciar el listener del teclado
def iniciar_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Iniciar el listener en un hilo separado
listener_thread = threading.Thread(target=iniciar_listener)
listener_thread.start()

# Mantener el programa en ejecución
listener_thread.join()


"""
Esto es un miniprograma para sacarme de apuros, se me rompio el mouse... 
Tiene mil defectos, se que se le puede seguir agregando funcionalidad y que sea mejor y mas facil de usar. 
Para matar el thread hay que hacerlo manualmente. No es lo mejor del mundo. Pero bueno soluciona un problema de urgencia.
"""
