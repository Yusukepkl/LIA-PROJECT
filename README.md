# Lia

Assistente virtual com interface grafica em PySide6.

## Configuracao no PyCharm

1. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Defina as seguintes variaveis de ambiente com suas chaves de API:
   - `OPENAI_API_KEY`
   - `GOOGLE_API_KEY`
   - `GOOGLE_CX`
   - `LIA_DB` (opcional, caminho do banco SQLite)
3. Rode a aplicacao:
   ```bash
   python main.py
   ```

## Estrutura de Pastas
- `lia/interface` - Interface Qt/QML e renderizacao do modelo 3D.
- `lia/vision` - Captura de video e reconhecimento de gestos.
- `lia/knowledge` - Integracao com Google, OpenAI e Grook.
- `lia/database` - Persistencia via SQLAlchemy.

Para mais detalhes, consulte a documentacao de cada modulo.
