## API - projeto _Onde Salvei_?
Este projeto é uma API desenvolvida utilizando o Django Rest Framework para permitir o envio e processamento de objetos de cor, interagindo com uma Inteligência Artificial (IA) para prever as cores com base em valores RGB fornecidos. A API permite que o usuário envie categorias de cores e objetos de cor, e, após o processamento, retorna as cores previstas pela IA. A IA utilizada foi criada espeficiamente para este projeto.

### 📋 Estrutura do Projeto
- mayapp: Contém a aplicação principal do projeto, com o código da API, incluindo views, serializers, enums e URLs.
    - views.py: Define a lógica para processar os objetos de cor recebidos.
    - serializers.py: Serializa os objetos de cor para validar e formatar os dados de entrada.
    - enums.py: Contém o enum `Color`, que define as cores possíveis para a IA prever.
    - urls.py: Define as rotas da API.
- projeto_final_api: Contém a configuração principal do Django.
    - settings.py: Configurações do Django, incluindo URLs, middleware e configurações de segurança.
    - urls.py: Arquivo de configuração das rotas da aplicação.
- manage.py: Utilitário de linha de comando para executar tarefas administrativas do Django.

### ⚙️ Funcionalidades
- Recebe dados de cores e suas categorias via requisição `POST`.
- Processa esses dados através de um modelo de IA para prever a cor correspondente.
- Retorna os resultados com as cores previstas e informações sobre cada objeto de cor.

### 🚀 Como Executar
- Requisitos:
    - Python 3.8+
- Pacotes listados no arquivo requirements.txt. Para instalá-los, execute:
```bash
pip install -r requirements.txt
```
#### API
Para iniciar o servidor:
```bash
python manage.py runserver
```

### 🗂️ Exemplos de Dados
A API está configurada para aceitar requisições POST no endpoint /api/receive-colors/. A requisição deve enviar um JSON como o exemplo abaixo na seguinte estrutura:
- Entrada (request)
```json
{
  "categories": ["Branco", "Preto", "Azul"],
  "colors": [
    {
      "path": "/path/to/image1.jpg",
      "average_rgb": [255, 255, 255]
    },
    {
      "path": "/path/to/image2.jpg",
      "average_rgb": [0, 0, 0]
    }
  ]
}
```
- Saída (response)
```json
[
  {
    "path": "/path/to/image1.jpg",
    "average_rgb": [255, 255, 255],
    "predicted_color": "Branco"
  },
  {
    "path": "/path/to/image2.jpg",
    "average_rgb": [0, 0, 0],
    "predicted_color": "Preto"
  }
]
```

### 📝 Licença
Este projeto está sob a licença MIT. Sinta-se livre para utilizá-lo e modificá-lo conforme necessário.

### 🎓 Objetivo
Este código integra o ecossistema do produto _Onde Salvei?_, desenvolvido como parte do Projeto de Conclusão de Curso da graduação em Ciência da Computação._
