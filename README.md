# Spotify Music Analytics — Gospel BR

Projeto de análise de dados desenvolvido com Python e Power BI para mapear o comportamento musical de artistas do segmento gospel brasileiro na plataforma Spotify.

## Contexto

O mercado de música gospel brasileiro movimenta bilhões de reais anualmente e possui uma base de consumidores extremamente fiel. Este projeto utiliza dados públicos da Spotify Web API para extrair métricas de artistas relevantes do segmento, com o objetivo de identificar padrões de produção musical, duração de faixas e volume de catálogo por artista.

## Objetivos

- Coletar dados de músicas e álbuns de 8 artistas do gospel brasileiro via API REST
- Realizar limpeza e tratamento dos dados com Python e Pandas
- Responder perguntas de negócio através de visualizações no Power BI

## Perguntas de Negócio

1. Qual artista possui maior volume de faixas catalogadas no Spotify?
2. Qual é a duração média das músicas por artista — e o que isso diz sobre o estilo de cada um?
3. Como a produção musical evoluiu ao longo dos anos por artista?
4. Quais álbuns concentram maior número de faixas?
5. Existe correlação entre duração das faixas e ano de lançamento?

## Stack Tecnológica

| Camada | Tecnologia |
|--------|------------|
| Coleta de dados | Python, Spotipy, Spotify Web API |
| Transformação | Python, Pandas |
| Visualização | Power BI |
| Versionamento | Git, GitHub |

## Arquitetura do Pipeline
## Como Reproduzir

**Pré-requisitos:** Python 3.8+, conta no Spotify Developer

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/spotify-music-analytics.git
cd spotify_music_analytics

# 2. Instale as dependências
pip install spotipy pandas python-dotenv

# 3. Configure as credenciais
# Crie um arquivo .env com:
# SPOTIFY_CLIENT_ID=seu_client_id
# SPOTIFY_CLIENT_SECRET=seu_client_secret

# 4. Execute o pipeline
python coleta_dados.py
python limpeza_dados.py
```

## Dataset

51 faixas coletadas de 8 artistas, com os seguintes atributos:

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| artista_buscado | string | Artista pesquisado |
| musica | string | Nome da faixa |
| album | string | Nome do álbum |
| data_lancamento | date | Data de lançamento |
| duracao_min | float | Duração em minutos |
| ano_lancamento | int | Ano extraído da data |
| explicit | string | Conteúdo explícito (Sim/Não) |

## Artistas Analisados

Projeto Sola · Morada · Fernandinho · Oficina G3 · Rodolfo Abrantes · Aline Barros · José Jr · Purples

## Próximos Passos

- Expandir o dataset com mais artistas do segmento
- Incluir dados de seguidores via autenticação OAuth2
- Automatizar a atualização do dataset com agendamento