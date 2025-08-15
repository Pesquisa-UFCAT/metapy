# Tutorial: Documentação de Funções Python com Geração Automática de Arquivos Markdown

Este tutorial irá guiá-lo através do processo de utilização de um script Python para documentar suas funções Python automaticamente e gerar arquivos Markdown.

## Passos para Executar o Script

### 1. Preparar o Ambiente

Certifique-se de que você tenha o Python instalado em sua máquina. Você pode verificar a instalação do Python com o seguinte comando no terminal:

```bash
python --version
```

### 2. Estrutura do Projeto

Crie a seguinte estrutura de diretórios para organizar seus arquivos:

```
/seu_projeto
    ├── pasta/
    │   └── exemplo.py
    └── documentador.py
```

- `pasta/`: Pasta onde você colocará seus arquivos Python que deseja documentar.
- `documentador.py`: Arquivo Python que contém o script de documentação.

### 3. Script de Documentação

O arquivo `documentador.py` contém o script que irá ler os arquivos Python na pasta `pasta/`, extrair informações sobre as funções e gerar arquivos Markdown para documentação.

### 4. Executando o Script

Para executar o script, abra um terminal, navegue até a pasta do projeto e execute o comando:

```bash
python documentador.py
```

### 5. Verificando a Saída

Após a execução do script, a estrutura do projeto será expandida para incluir a pasta `docs/` que conterá os arquivos Markdown gerados:

```
/seu_projeto
    ├── pasta/
    │   └── exemplo.py
    ├── docs/
    │   └── exemplo/
    │       └── funcao.md
    └── documentador.py
```

### Exemplo de Entrada

Aqui está um exemplo de um arquivo Python (`exemplo.py`) que você pode colocar na pasta `pasta/`:

```python
def soma(a, b):
    """
    Esta função retorna a soma de dois números.

    Args:
        a (int): O primeiro número.
        b (int): O segundo número.

    Returns:
        int: A soma dos dois números.
    """
    return a + b
```

### Verificando o Arquivo Markdown Gerado

Após executar o script, o arquivo Markdown gerado (`soma.md`) estará localizado em `docs/exemplo/` e conterá a documentação da função `soma`.
