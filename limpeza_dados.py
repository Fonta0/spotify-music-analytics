import pandas as pd


df = pd.read_csv("data/tracks.csv", encoding="utf-8-sig")

print("=== DADOS BRUTOS ===")
print(f"Total de linhas: {len(df)}")
print(f"Colunas: {list(df.columns)}")
print(f"\nValores nulos:\n{df.isnull().sum()}")

# Remove duplicatas
df = df.drop_duplicates(subset=["musica", "artista_buscado"])
print(f"\nApós remover duplicatas: {len(df)} linhas")

# Converte duração pra minutos
df["duracao_min"] = (df["duracao_ms"] / 60000).round(2)

# Corrige tipos
df["data_lancamento"] = pd.to_datetime(df["data_lancamento"], errors="coerce")
df["ano_lancamento"] = df["data_lancamento"].dt.year
df["explicit"] = df["explicit"].map({True: "Sim", False: "Não"})

# Remove tracks de artistas errados
df = df[df["artista_buscado"].str.lower() == df["artista_track"].str.lower()].copy()
print(f"Após filtrar artistas corretos: {len(df)} linhas")


df.to_csv("data/tracks_limpo.csv", index=False, encoding="utf-8-sig")

print("\nRESUMO")
print(df.groupby("artista_buscado").agg(
    total_musicas=("musica", "count"),
    popularidade_media=("popularidade_musica", "mean"),
    duracao_media_min=("duracao_min", "mean")
).round(2))

print("\nDados limpos salvos em data/tracks_limpo.csv")