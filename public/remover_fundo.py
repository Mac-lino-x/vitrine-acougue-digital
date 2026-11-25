#!/usr/bin/env python3
"""
Remove o fundo branco das imagens PNG da pasta public/assets/carnes
e deixa só a carne, com fundo transparente.

COMO USAR (no terminal do VS Code, na pasta do projeto):

  pip install pillow numpy scipy
  python remover_fundo.py

Opções:
  python remover_fundo.py picanha.png ovo_branco.png   -> só essas imagens
  python remover_fundo.py --tolerancia 40               -> remove brancos mais "sujos" (padrão 28)
  python remover_fundo.py --largura 1400                -> reduz imagens maiores que isso (padrão 1600)
  python remover_fundo.py coracao_frango.png --furos    -> também remove vãos brancos fechados entre itens
                                                           (use só em imagens com pilhas/vãos; NÃO use em ovo branco)
  python remover_fundo.py --ia                          -> usa IA (rembg), melhor para ovos brancos
                                                           (antes: pip install "rembg[cpu]")

As imagens originais ficam guardadas em: backup_imagens_originais/
"""
import argparse, os, shutil, sys
import numpy as np
from PIL import Image, ImageFilter

PASTA = os.path.join("public", "assets", "carnes")
BACKUP = "backup_imagens_originais"


def ja_transparente(im):
    a = np.asarray(im.getchannel("A"))
    h, w = a.shape
    cantos = [a[0, 0], a[0, w - 1], a[h - 1, 0], a[h - 1, w - 1]]
    return all(c < 20 for c in cantos)


def _scipy():
    try:
        from scipy import ndimage
        return ndimage
    except ImportError:
        sys.exit("Falta instalar o scipy. Rode:  pip install pillow numpy scipy")


def componentes_do_fundo(mask_branco, raio=4):
    """Mantém só as áreas brancas ligadas à borda. O 'raio' corta ligações finas
    (assim o brilho branco de dentro de um ovo não é confundido com o fundo)."""
    nd = _scipy()
    nucleo = nd.binary_erosion(mask_branco, iterations=raio, border_value=1)
    rotulos, n = nd.label(nucleo)
    if n == 0:
        return np.zeros_like(mask_branco)
    borda = np.unique(np.concatenate([rotulos[0, :], rotulos[-1, :], rotulos[:, 0], rotulos[:, -1]]))
    borda = borda[borda != 0]
    miolo = np.isin(rotulos, borda)
    return nd.binary_dilation(miolo, iterations=raio + 1) & mask_branco


def vaos_fechados(mask_estrito, fundo, minimo):
    """Áreas brancas fechadas (ex.: espaço entre dois itens) com área grande."""
    nd = _scipy()
    resto = mask_estrito & ~fundo
    rotulos, n = nd.label(resto)
    if n == 0:
        return fundo
    tamanhos = np.bincount(rotulos.ravel())
    grandes = np.where(tamanhos >= minimo)[0]
    grandes = grandes[grandes != 0]
    return fundo | np.isin(rotulos, grandes)


def remover_branco(im, tol, furos=False):
    rgb = np.asarray(im.convert("RGB")).astype(np.int16)
    quase_branco = rgb.min(axis=2) >= (255 - tol)
    fundo = componentes_do_fundo(quase_branco)
    if furos:
        estrito = rgb.min(axis=2) >= 250
        fundo = vaos_fechados(estrito, fundo, int(0.002 * fundo.size))
    sujeito = (~fundo).astype(np.uint8) * 255
    m = Image.fromarray(sujeito, "L")
    m = m.filter(ImageFilter.MinFilter(3))          # tira o "halo" branco da borda
    m = m.filter(ImageFilter.GaussianBlur(1.0))     # borda suave
    out = im.convert("RGBA")
    out.putalpha(m)
    return out


def remover_com_ia(im):
    try:
        from rembg import remove
    except ImportError:
        sys.exit('Falta instalar o rembg. Rode:  pip install "rembg[cpu]"')
    return remove(im.convert("RGBA"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arquivos", nargs="*")
    ap.add_argument("--tolerancia", type=int, default=28)
    ap.add_argument("--largura", type=int, default=1600)
    ap.add_argument("--ia", action="store_true")
    ap.add_argument("--furos", action="store_true", help="remove vãos brancos fechados entre itens")
    ap.add_argument("--forcar", action="store_true", help="processa mesmo as que já têm fundo transparente")
    args = ap.parse_args()

    if not os.path.isdir(PASTA):
        sys.exit(f"Não achei a pasta {PASTA}. Rode o script na pasta principal do projeto.")

    nomes = args.arquivos or sorted(f for f in os.listdir(PASTA) if f.lower().endswith(".png"))
    os.makedirs(BACKUP, exist_ok=True)

    gi = ".gitignore"
    if os.path.exists(gi):
        txt = open(gi, encoding="utf-8").read()
        if BACKUP not in txt:
            with open(gi, "a", encoding="utf-8") as f:
                f.write(("\n" if not txt.endswith("\n") else "") + BACKUP + "/\n")

    feitas = puladas = 0
    for nome in nomes:
        caminho = os.path.join(PASTA, nome)
        if not os.path.exists(caminho):
            print("NÃO ENCONTRADA:", nome); continue
        im = Image.open(caminho).convert("RGBA")
        if ja_transparente(im) and not args.forcar:
            print("já transparente:", nome); puladas += 1; continue
        destino = os.path.join(BACKUP, nome)
        if not os.path.exists(destino):
            shutil.copy2(caminho, destino)
        res = remover_com_ia(im) if args.ia else remover_branco(im, args.tolerancia, args.furos)
        bb = res.getchannel("A").point(lambda v: 255 if v > 10 else 0).getbbox()
        if bb:                                   # recorta o excesso transparente
            res = res.crop(bb)
        if res.width > args.largura:
            h = round(res.height * args.largura / res.width)
            res = res.resize((args.largura, h), Image.LANCZOS)
        res.save(caminho, optimize=True)
        print("ok:", nome, f"({os.path.getsize(caminho)//1024} KB)")
        feitas += 1

    print(f"\nPronto: {feitas} imagens ajustadas, {puladas} já estavam transparentes.")
    print(f"Os originais ficaram em {BACKUP}/")

if __name__ == "__main__":
    main()
