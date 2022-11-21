from flask import Flask,render_template


app = Flask(__name__)
@app.route('/')
@app.route('/<int:num>')
@app.route('/<int:num>/<int:num2>')
@app.route('/<int:num>/<int:num2>/<color>')
@app.route('/<int:num>/<int:num2>/<color>/<color2>')
@app.route('/<color>/<color2>') #Agregue esta ruta por si el usuario solo quiere modificar color
def checker(num=8,num2=8,color='#9fc5f8',color2='black'):
    #num = int(num)
    return render_template("checker.html", num = num,num2=num2,color=color,color2=color2)  # Devuelve la cadena '¡Hola Mundo!' como respuesta



if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente  
    app.run(debug=True)