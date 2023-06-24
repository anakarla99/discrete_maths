import subprocess
import random

args_sol = ["python", "Monitor.py"]
args_gen = ["python", "Generador.py"]



process_sol = subprocess.Popen(args_sol, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
process_gen = subprocess.Popen(args_gen, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
exist_err_1 = False
for i in range(30):
    try:
        n, error = process_gen.communicate()
        insandouts = list(n.decode().split("\r\n"))
        try:
            str_solucion , err_solucion = process_sol.communicate(insandouts[0].encode())
            print(insandouts[0] +"\n \nSolucion del generador = " + insandouts[1] + "\n \nSolucion eficiente = " + str_solucion.decode() + "\n \nRespuesta Acertada = " + str((insandouts[1] + '\r\n')==str_solucion.decode()) + '\n')
        except:
            print("Error en la solución del código eficiente")
    except:
        print('generator error')
        exist_err_1 = True
    process_gen = subprocess.Popen(args_gen, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process_sol = subprocess.Popen(args_sol, stdin=subprocess.PIPE, stdout=subprocess.PIPE)