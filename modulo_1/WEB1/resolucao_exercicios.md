## Resolução dos Exercícios

**Exercício 1 - Criando um Parágrafo:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 1</title>
</head>
<body>
    <p>Este é um parágrafo de texto simples.</p>
</body>
</html>
```

**Exercício 2 - Adicionando uma Imagem:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 2</title>
</head>
<body>
    <p>Esta é uma imagem:</p>
    <img src="caminho_da_sua_imagem.jpg" alt="Descrição da imagem">
</body>
</html>
```

**Exercício 3 - Lista de Itens:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 3</title>
</head>
<body>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
</body>
</html>
```

**Exercício 4 - Links Internos:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 4</title>
</head>
<body>
    <a href="#secao1">Ir para Seção 1</a>
    <a href="#secao2">Ir para Seção 2</a>

    <h2 id="secao1">Seção 1</h2>
    <p>Conteúdo da Seção 1</p>

    <h2 id="secao2">Seção 2</h2>
    <p>Conteúdo da Seção 2</p>
</body>
</html>
```

**Exercício 5 - Formulário Simples:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 5</title>
</head>
<body>
    <form action="processar_formulario.php" method="post">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="mensagem">Mensagem:</label><br>
        <textarea id="mensagem" name="mensagem" rows="4" cols="50" required></textarea><br><br>

        <input type="submit" value="Enviar">
    </form>
</body>
</html>
```

**Exercício 6 - Tabelas Básicas:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 6</title>
</head>
<body>
    <table border="1">
        <tr>
            <th>Nome</th>
            <th>Idade</th>
            <th>Cidade</th>
        </tr>
        <tr>
            <td>João</td>
            <td>30</td>
            <td>São Paulo</td>
        </tr>
        <tr>
            <td>Maria</td>
            <td>25</td>
            <td>Rio de Janeiro</td>
        </tr>
    </table>
</body>
</html>
```

**Exercício 7 - Estilo com CSS:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 7</title>
    <style>
        body {
            background-color: lightblue;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: darkblue;
        }
    </style>
</head>
<body>
    <h1>Exercício 7</h1>
    <p>Este é um parágrafo estilizado com CSS.</p>
</body>
</html>
```

**Exercício 8 - Página de Vídeo:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 8</title>
</head>
<body>
    <h1>Vídeo de Exemplo</h1>
    <video controls>
        <source src="video.mp4" type="video/mp4">
        Seu navegador não suporta o elemento de vídeo.
    </video>
</body>
</html>
```

**Exercício 9 - Validação de Formulário:** (Adicione os atributos `required` e `type` aos elementos de entrada conforme necessário)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 9</title>
</head>
<body>
    <form action="processar_formulario.php" method="post">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="mensagem">Mensagem:</label><br>
        <textarea id="mensagem" name="mensagem" rows="4" cols="50" required></textarea><br><br>

        <input type="submit" value="Enviar">
    </form>
</body>
</html>
```

**Exercício 10 - HTML Semântico:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Exercício 10</title>
</head>
<body>
    <header>
        <h1>Cabeçalho da Página</h1>
    </header>
    
    <nav>
        <ul>
            <li><a href="#">Início</a></li>
            <li><a href="#">Sobre</a></li>
            <li><a href="#">Contato</a></li>
        </ul>
    </nav>
    
    <article>
        <h2>Título do Artigo</h2>
        <p>Este é um artigo sobre HTML5 semântico.</p>
    </article>
    
    <footer>
        <p>Rodapé da Página</p>
    </footer>
</body>
</html>
```

Essas são as soluções para os 10 exercícios progressivos de HTML5. Lembre-se de personalizar os caminhos das imagens, os URLs dos formulários, os estilos CSS e outros detalhes conforme necessário para atender às suas necessidades específicas.