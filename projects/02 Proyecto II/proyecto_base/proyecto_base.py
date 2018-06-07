import instaintro_gui


def tarea():
	# Aqui empieza tu tarea
	import
	while(True) :
    		acción = instaintro_gui.esperar_click()
    		if accion == "gris" :
        		imagen = instaintro.gui.obetener pixeles()
        		for i in imagen :
            			for j in i :
                			print(j)
    	return
	


app = instaintro_gui.Application("tarea")
app.title('InstaIntro')
app.loadProgram(tarea)
app.start()
