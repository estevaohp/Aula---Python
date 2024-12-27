#type: ignore
from pathlib import Path

from PyPDF2 import PdfReader 

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ /  'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)


for page in reader.pages:
    print(page)
    print()