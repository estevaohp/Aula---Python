try:
    import requests
    print(f"O pacote 'requests' está instalado. Versão: {requests.__version__}")
except ImportError:
    print("O pacote 'requests' NÃO está instalado.")
