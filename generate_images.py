#!/usr/bin/env python3
"""Gera imagens de produtos para Dudota Doces usando Pillow."""

from PIL import Image, ImageDraw, ImageFont
import os

# Configurações
WIDTH, HEIGHT = 800, 600
OUTPUT_DIR = "assets"

# Produtos com cores temáticas
PRODUCTS = [
    {
        "filename": "bananitas.jpeg",
        "title": "Bananitas",
        "subtitle": "Pacote com 50 unidades",
        "description": "Doces sabor banana com textura\nmacia e toque açucarado",
        "emoji": "🍌",
        "bg_top": (255, 235, 100),      # amarelo banana
        "bg_bottom": (255, 200, 50),
        "accent": (180, 140, 0),
    },
    {
        "filename": "doce_leite.jpeg",
        "title": "Doce de Leite",
        "subtitle": "Pacote com 50 unidades",
        "description": "Doce em barra com sabor suave\ne cremoso, ótimo para mesas",
        "emoji": "🥛",
        "bg_top": (210, 170, 120),      # marrom dourado
        "bg_bottom": (180, 130, 80),
        "accent": (120, 80, 40),
    },
    {
        "filename": "fondant_leite_po.jpeg",
        "title": "Fondant de Leite em Pó",
        "subtitle": "Pacote com 50 unidades",
        "description": "Doce em barra delicado, com sabor\nmarcante de leite em pó",
        "emoji": "🍼",
        "bg_top": (255, 250, 240),      # creme
        "bg_bottom": (240, 230, 210),
        "accent": (160, 140, 100),
    },
    {
        "filename": "fondant_chocolate.jpeg",
        "title": "Fondant Leite em Pó\ncom Chocolate",
        "subtitle": "Pacote com 50 unidades",
        "description": "Combinação de leite em pó com\nchocolate, cremosidade e sabor",
        "emoji": "🍫",
        "bg_top": (120, 80, 60),        # chocolate
        "bg_bottom": (80, 50, 30),
        "accent": (255, 220, 180),
    },
    {
        "filename": "pacoca_rolha_choc.jpeg",
        "title": "Paçoca Rolha\ncom Chocolate",
        "subtitle": "Pote",
        "description": "Paçoca rolha com cobertura\nsabor chocolate, prática e querida",
        "emoji": "🥜",
        "bg_top": (160, 110, 70),       # amendoim + chocolate
        "bg_bottom": (120, 80, 50),
        "accent": (255, 230, 200),
    },
    {
        "filename": "pacoca_rolha_trad.jpeg",
        "title": "Paçoca Rolha\nTradicional",
        "subtitle": "Pote",
        "description": "Versão tradicional da paçoca rolha,\nleve, saborosa e com gostinho de infância",
        "emoji": "🥜",
        "bg_top": (230, 200, 150),      # amendoim claro
        "bg_bottom": (200, 170, 120),
        "accent": (120, 90, 50),
    },
    {
        "filename": "pe_moleque_crocante.jpeg",
        "title": "Pé de Moleque\nCrocante",
        "subtitle": "Tamanho G",
        "description": "Pé de moleque crocante em versão maior,\ncom amendoins inteiros e visual atraente",
        "emoji": "🍯",
        "bg_top": (180, 120, 50),       # caramelo escuro
        "bg_bottom": (140, 90, 30),
        "accent": (255, 240, 200),
    },
]

def hex_to_rgb(hex_color):
    """Converte tupla RGB para uso no Pillow."""
    return hex_color

def draw_gradient(draw, width, height, color_top, color_bottom):
    """Desenha um gradiente vertical."""
    for y in range(height):
        ratio = y / height
        r = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
        g = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
        b = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def get_font(size, bold=False):
    """Tenta carregar uma fonte do sistema."""
    font_names = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for name in font_names:
        if os.path.exists(name):
            try:
                return ImageFont.truetype(name, size)
            except:
                pass
    return ImageFont.load_default()

def create_product_image(product):
    """Cria uma imagem de produto."""
    img = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Fundo gradiente
    draw_gradient(draw, WIDTH, HEIGHT, product["bg_top"], product["bg_bottom"])
    
    # Faixa decorativa no topo
    draw.rectangle([(0, 0), (WIDTH, 12)], fill=product["accent"])
    
    # Círculo central para o emoji
    cx, cy = WIDTH // 2, HEIGHT // 2 - 40
    radius = 140
    # Sombra do círculo
    draw.ellipse(
        [(cx - radius + 8, cy - radius + 8), (cx + radius + 8, cy + radius + 8)],
        fill=(0, 0, 0, 30)
    )
    # Círculo principal
    draw.ellipse(
        [(cx - radius, cy - radius), (cx + radius, cy + radius)],
        fill=(255, 255, 255, 200)
    )
    
    # Emoji
    emoji_font = get_font(120)
    bbox = draw.textbbox((0, 0), product["emoji"], font=emoji_font)
    emoji_w = bbox[2] - bbox[0]
    emoji_h = bbox[3] - bbox[1]
    draw.text((cx - emoji_w // 2, cy - emoji_h // 2 - 10), product["emoji"], font=emoji_font, fill=(50, 50, 50))
    
    # Título
    title_font = get_font(42, bold=True)
    lines = product["title"].split("\n")
    y_title = cy + radius + 30
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=title_font)
        tw = bbox[2] - bbox[0]
        draw.text((WIDTH // 2 - tw // 2, y_title), line, font=title_font, fill=product["accent"])
        y_title += 50
    
    # Subtítulo
    sub_font = get_font(22)
    bbox = draw.textbbox((0, 0), product["subtitle"], font=sub_font)
    sw = bbox[2] - bbox[0]
    draw.text((WIDTH // 2 - sw // 2, y_title + 5), product["subtitle"], font=sub_font, fill=(100, 100, 100))
    
    # Descrição
    desc_font = get_font(18)
    desc_lines = product["description"].split("\n")
    y_desc = y_title + 50
    for line in desc_lines:
        bbox = draw.textbbox((0, 0), line, font=desc_font)
        dw = bbox[2] - bbox[0]
        draw.text((WIDTH // 2 - dw // 2, y_desc), line, font=desc_font, fill=(80, 80, 80))
        y_desc += 28
    
    # Marca no rodapé
    brand_font = get_font(16)
    brand_text = "Dudota Doces • Tradição há mais de 40 anos"
    bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    bw = bbox[2] - bbox[0]
    draw.text((WIDTH // 2 - bw // 2, HEIGHT - 50), brand_text, font=brand_font, fill=product["accent"])
    
    # Salvar
    output_path = os.path.join(OUTPUT_DIR, product["filename"])
    img.save(output_path, "JPEG", quality=90)
    print(f"✓ Gerado: {output_path}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for product in PRODUCTS:
        create_product_image(product)
    print("\n✅ Todas as imagens foram geradas com sucesso!")

if __name__ == "__main__":
    main()