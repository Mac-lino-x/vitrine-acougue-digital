from pathlib import Path
import shutil
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

RAIZ = Path(__file__).parent
PASTA = RAIZ / "public" / "assets" / "carnes"
BACKUP = RAIZ / "_backup_carnes"   # cópia das originais, fora do public

LIMITE = 235          # quanto mais baixo, mais tons claros viram fundo (ex.: 225)
REMOVER_VAOS = False  # True = também apaga branco "preso" entre partes (ex.: vão entre corações)
VAO_MIN = 0.003       # tamanho mínimo do vão, como fração da imagem (só se REMOVER_VAOS = True)


def remover_fundo(img: Image.Image) -> Image.Image:
    a = np.array(img.convert("RGBA"))
    claro = a[..., :3].min(axis=2) >= LIMITE
    claro |= a[..., 3] == 0

    lab, n = ndi.label(claro)
    borda = np.unique(np.concatenate([lab[0, :], lab[-1, :], lab[:, 0], lab[:, -1]]))
    fundo = np.isin(lab, borda[borda != 0])

    if REMOVER_VAOS:
        tam = ndi.sum(claro, lab, range(1, n + 1))
        grandes = [i + 1 for i, t in enumerate(tam) if t >= VAO_MIN * claro.size]
        fundo |= np.isin(lab, grandes)

    objeto = ndi.binary_erosion(~fundo, iterations=1)       # tira o halo branco da borda
    alpha = ndi.gaussian_filter(objeto.astype(float), 0.8)  # suaviza o contorno
    a[..., 3] = (np.clip(alpha, 0, 1) * 255).astype(np.uint8)

    out = Image.fromarray(a, "RGBA")
    caixa = out.getbbox()          # recorta o espaço vazio em volta
    return out.crop(caixa) if caixa else out


def main():
    BACKUP.mkdir(exist_ok=True)
    arquivos = sorted(PASTA.glob("*.png"))
    for f in arquivos:
        destino = BACKUP / f.name
        if not destino.exists():
            shutil.copy2(f, destino)   # backup só na primeira vez
        # sempre parte da original, então pode rodar de novo com outro LIMITE
        remover_fundo(Image.open(destino)).save(f)
        print("ok", f.name)
    print(f"\n{len(arquivos)} imagens processadas. Originais em {BACKUP}")


if __name__ == "__main__":
    main()