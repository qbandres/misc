from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/invert',methods = [ 'GET','POST'])
def caracter():
    texto = request.form['invert']
    invert=texto[::-1]
    return render_template('index.html',invert_print = invert, code_invert = 'name=texto[::-1]')

@app.route('/letter', methods = ['GET','POST'])
def mayuscula():
    texto = request.form['letra']
    invert=texto[::-1]
    all_cap = texto.upper()
    all_min = texto.lower()
    first_cap = texto.capitalize()
    first = texto[0]
    third = texto[2]
    last_l = texto[-1]
    long = len(texto)
    wth_sp = texto.strip()
    wth_all_sp = texto.replace(' ','')
    replace = texto.replace('o','a')
    until = texto[:5]
    m_ex = texto[1:-1:2]
    m_exf =  texto[1::3]

    return render_template('index.html',letras = texto
                                        ,invert = invert, code_invert = 'name=texto[::-1]'
                                        ,all_cap = all_cap, code_all_cap = 'name = texto.upper()'
                                        ,all_min = all_min, code_all_min = 'name = texto.lower()'
                                        ,first_cap = first_cap, code_first_cap = 'name = texto.capitalize()'
                                        ,select_letter = f'The first {first} Third {third} the last {last_l}', code_select_letter = 'name[0] & name[2]'
                                        ,len_letter = f' The len is {long}', code_len_letter = 'len(texto)'
                                        ,wth_sp = wth_sp, code_wth_sp = 'name = texto.strip()'
                                        ,wth_all_sp = wth_all_sp, code_wth_all_sp = 'name = texto.replace(' ','')'
                                        ,replace = replace, code_replace = 'name = texto.replace(''o,''a)'
                                        ,until = until, code_until = 'name = texto[:5]'
                                        ,m_ex = m_ex, code_m_ex = 'name = texto[1:-1:2]'
                                        ,m_exf = m_exf ,code_m_exf = 'name = texto[1::3]')

if __name__ == '__main__':
    app.run(debug=True)