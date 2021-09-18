# Palindrome, palabra que se lee igual al escribir al reves
# La aplicación te indica verdero o falso
m = input('Ingrese la palabra u oración  ')
m_M = m.upper()
m_0 = m[0]
m_3 = m[3]
m_f = m[-1]
num = len(m)
m_C = m.capitalize()
m_L = m.lower()
m_S = m.strip()
m_R = m.replace('o','a')
m_SE = m.replace(' ','')
palindrome = lambda string:string == string[::-1]
m_RE = m_SE[::-1]
b = palindrome(m_SE)

m_s5 = m[:5]
m_ex = m[1:-1:2]
m_exf =  m[1::3]

print(f'El nombre {m} en mayuscula es {m_M}')
print(f'El nombre {m} con la primera mayuscula es {m_C}')
print(f'El nombre {m} la primera letra es {m_0} la Cuarta letra es {m_3} y la última letra es {m_f}')
print(f'El nombre {m} tiene la siguient longitud = {num}' )
print(f'El nombre {m} en minnuscula es {m_L}')
print(f'La palabra {m} sin espacios iniciales y finales es {m_S}')
print(f'La palabra {m} cambiando o x a {m_R}')
print(f'La palabra {m} sin espacios es {m_SE}')
print(f'La palabra {m} sin espacios y al reves es {m_RE}')
print(f'La palabra {m} su analisis de palindorme es {b}')
print(f'La palabra {m} hasta el caracter 5 = {m_s5}')
print(f'La palabra {m} del 1 al final con pasos de 2 es {m_ex}')
print(f'La palabra {m} del 1 al final con pasos de 3 metodo 2 es {m_exf}')
