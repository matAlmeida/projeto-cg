# projeto-cg
Projeto da matéria de Computação Gráfica utilizando OpenGL e Python

# [`Site com Documentação`](https://matalmeida.github.io/projeto-cg/index.html)

## Instalação
### Ubuntu/Debian
> `Instala o pip que gerencia os modulos no Python3.x` </br>
> $ sudo apt-get install python3-pip </br>

> `Instala e testa o Pygame no Python 3.x` </br>
> $ python3 -m pip install pygame --user </br>
> $ python3 -m pygame.examples.aliens </br>

> `Instala o PyOpenGL no Python 3.x` </br>
> $ pip3 install PyOpenGL PyOpenGL_accelerate </br>

> `Instala o pacote freeglut` </br>
> `Este pacote tem a mesma finalidade do pygame, ele está sendo utilizado no projeto. O pygame foi só para teste.` </br>
> $ sudo apt-get install freeglut3-dev </br>

> `Instala a biblioteca PIL, para manipular imagens` <br>
> $ pip3 install Pillow <br>

### Windows
> `Baixe e instale o Python3.x no site abaixo de acordo com a arquitetura do seu computador:` </br>
> [`Python3.x`](https://www.python.org/downloads/windows/) </br>

> `Baixe o PyOpenGL e o Pygame no site abaixo, de acordo com a sua arquitetura e com a versão do Python. (onde cp3x corresponde à versão do Python, no caso, Python 3.x).` </br>
> `Como o site é muito grande, é aconselhável pesquisar o PyOpenGL e o Pygame pelo ctrl+f.` </br>
> [`PyOpenGL e Pygame`](http://www.lfd.uci.edu/~gohlke/pythonlibs/) </br>

> `Abra o CMD do Windows e navegue até a pasta em que está os arquivos que você baixou com o comando 'cd', exemplo:` </br>
> $ cd Downloads </br>
> `Agora para instalar o PyOpenGL e o Pygame, utiliza-se o comando pip install 'nomeDoModulo', exemplo:` </br>
> $ pip install PyOpenGL-3.1.1-cp3x-cp3xm-win_amd64.whl </br>
> `E depois de instalado o PyOpenGL, instala o Pygame:` </br>
> $ pip install pygame-1.9.3-cp3x-cp3xm-win_amd64.whl </br>

> `Instala a biblioteca PIL, para manipular imagens` <br>
> $ pip install Pillow <br>
> `ou` <br>
> $ easy_install Pillow <br>

> `Agora com os módulos já instalados, baixe e instale uma IDE. O link abaixo é da IDE PyCharm:` </br>
> [`PyCharm`](https://www.jetbrains.com/pycharm/download/#section=windows) </br>

## Usando no codigo
```python
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
```
## OBJETIVO
> `Refazer os primeiros 36 projetos do site abaixo utilizando a versão 3 do Python e os pacotes PyOpenGL e o Pygame e fazer a documentação dos mesmos:`
>[Tutorial OpenGL](http://lazyfoo.net/tutorials/SDL/index.php)

## Tutorial (em inglês)
> [`Aqui`](https://pythonprogramming.net/opengl-pyopengl-python-pygame-tutorial/)
