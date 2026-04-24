import pandas as pd

# Carrega o CSV
df = pd.read_csv("data/tracks.csv", encoding="utf-8-sig")

print("=== DADOS BRUTOS ===")
print(f"Total de linhas: {len(df)}")
print(f"Colunas: {list(df.columns)}")
print(f"\nValores nulos:\n{df.isnull().sum()}")

# Remove duplicatas
df = df.drop_duplicates(subset=["musica", "artista_buscado"])
print(f"\nApós remover duplicatas: {len(df)} linhas")

# Corrige tipos
df["data_lancamento"] = pd.to_datetime(df["data_lancamento"], errors="coerce")
df["ano_lancamento"] = df["data_lancamento"].dt.year
df["explicit"] = df["explicit"].map({True: "Sim", False: "Não"})

# Remove tracks de artistas errados
# (quando a busca trouxe artistas com nome parecido)
df = df[df["artista_buscado"].str.lower() == df["artista_track"].str.lower()].copy()
print(f"Após filtrar artistas corretos: {len(df)} linhas")

# Salva CSV limpo
df.to_csv("data/tracks_limpo.csv", index=False, encoding="utf-8-sig")

print("\n=== RESUMO FINAL ===")
print(df.groupby("artista_buscado").agg(
    total_musicas=("musica", "count"),
    popularidade_media=("popularidade_musica", "mean"),
    duracao_media_min=("duracao_min", "mean")
).round(2))

print("\nDados limpos salvos em data/tracks_limpo.csv")