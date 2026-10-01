import re

# HTML original
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Aprendiendo Expresiones Regulares</title>
</head>
<body>

<h1>Introducción a las Expresiones Regulares</h1>

<p>Las expresiones regulares, también conocidas como
regex, son una herramienta poderosa para buscar, validar
y transformar texto. Se utilizan en una amplia variedad
de lenguajes de programación, como Python, JavaScript y Java.</p>

<h2>Usos Comunes</h2>

<ul>
    <li>Validar formatos de correo electrónico.</li>
    <li>Buscar patrones específicos en grandes volúmenes de texto.</li>
    <li>Reemplazar palabras o frases automáticamente.</li>
</ul>

<h2>Ejemplo en Python</h2>

<p>En Python, el módulo <code>re</code> permite
trabajar fácilmente con expresiones regulares. Por ejemplo:</p>

<pre><code>import re
texto = "Hola mundo"
resultado = re.sub(r"mundo", "Python", texto)
print(resultado)
</code></pre>

<h3>Conclusión</h3>

<p>Dominar las expresiones regulares puede ahorrarte
horas de trabajo en limpieza de datos y procesamiento de
texto. Practica con ejemplos y experimenta con tus propios
patrones.</p>

</body>
</html>
"""

# Encabezados: h1 → #, h2 → ##, h3 → ###
html = re.sub(r'<h1>(.*?)</h1>', r'# \1', html, flags=re.DOTALL)
html = re.sub(r'<h2>(.*?)</h2>', r'## \1', html, flags=re.DOTALL)
html = re.sub(r'<h3>(.*?)</h3>', r'### \1', html, flags=re.DOTALL)

# Párrafos: elimina las etiquetas <p>
html = re.sub(r'<p>(.*?)</p>', r'\1', html, flags=re.DOTALL)

# Listas: li → -
html = re.sub(r'<li>(.*?)</li>', r'- \1', html, flags=re.DOTALL)
html = re.sub(r'</?ul>', '', html)

# Bloques de código: pre + code → ```python
html = re.sub(
    r'<pre>\s*<code>(.*?)</code>\s*</pre>',
    r'```python\n\1\n```',
    html,
    flags=re.DOTALL
)

# Código en línea: code → ``
html = re.sub(r'<code>(.*?)</code>', r'`\1`', html, flags=re.DOTALL)

# Eliminar etiquetas HTML que no necesitamos
html = re.sub(r'<!DOCTYPE html>', '', html)
html = re.sub(r'<title>.*?</title>', '', html, flags=re.DOTALL)
html = re.sub(r'</?(html|head|body)>', '', html)

# Limpiar espacios y saltos de línea
html = re.sub(r'\n\s*\n\s*\n+', '\n\n', html)

# Resultado final
markdown = html.strip()

print("========== MARKDOWN ==========\n")
print(markdown)