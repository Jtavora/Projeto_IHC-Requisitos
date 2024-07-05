import os
from PIL import Image, ImageDraw, ImageFont
from datetime import date

hoje = date.today()

def gerar_certificado(dados, nome_aluno):
    print(f'Gerando pdf...')
    image = Image.open(os.path.join(os.path.dirname(__file__), 'Model.png'))
    draw = ImageDraw.Draw(image)  

    #NOME DO ALUNO
    font_size = 70 
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)  
    y_position = 990  
    draw.text((450, y_position), nome_aluno, font=font, fill=(0, 0, 0, 255))

    #NOME DO COORDENADOR
    font_size = 50  # Tamanho da fonte
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)  
    y_position = 1425  
    x_position = 1130
    draw.text((x_position, y_position), f"{dados['nome_coordenador']}", font=font, fill=(0, 0, 0, 255))

    #NOME DO PROFESSOR
    font_size = 50  
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)  
    y_position = 1425  
    x_position = 540
    draw.text((x_position, y_position), f"{dados['nome_professor']}", font=font, fill=(0, 0, 0, 255))

    #DIA
    font_size = 40
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)  
    y_position = 1300
    x_position = 900
    draw.text((x_position, y_position), f"{hoje}", font=font, fill=(0, 0, 0, 255))

    #CURSO
    font_size = 100
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size) 
    y_position = 750  
    x_position = 625
    draw.text((x_position, y_position), f"{dados['nome_curso']}", font=font, fill=(0, 0, 0, 255))

    #CURSO DESCRICAO
    font_size = 40
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)  
    y_position = 1080  
    x_position = 1105
    draw.text((x_position, y_position), f"{dados['nome_curso']}", font=font, fill=(0, 0, 0, 255))

    #CARGA HORARIA
    font_size = 40
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)  
    y_position = 1143 
    x_position = 810
    draw.text((x_position, y_position), f"{dados['carga_horaria']}h", font=font, fill=(0, 0, 0, 255))

    #SALVA PDF
    certificado_path = os.path.join(os.path.dirname(__file__), "certificados", f"{nome_aluno}.png")
    image.save(certificado_path)