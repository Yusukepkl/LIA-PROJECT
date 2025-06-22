# Projeto Lia

Assistente virtual com interface em PySide6.

## Configuração do ambiente

1. Crie o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Defina as variáveis de ambiente com suas chaves:
   - `OPENAI_API_KEY`
   - `GOOGLE_API_KEY` e `GOOGLE_CSE_ID`
   - `GROOK_API_KEY`

## Execução

```bash
python main.py
```

Abra o projeto no PyCharm e aponte para o interprete do virtualenv criado.

## Estrutura

- `lia/interface` – interface Qt/QML e carregamento de modelo 3D
- `lia/vision` – captura de câmera e reconhecimento
- `lia/knowledge` – integração com APIs externas
- `lia/database` – armazenamento de histórico com SQLite

Consistências entre respostas são verificadas antes de exibir.
