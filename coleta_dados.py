import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)
sp = spotipy.Spotify(auth_manager=auth_manager)

artistas = [
    "Projeto Sola",
    "Morada",
    "José Jr",
    "Oficina G3",
    "Rodolfo Abrantes",
    "Aline Barros",
    "Fernandinho",
    "Purples"
]

tracks_lista = []

for artista in artistas:
    print(f"Coletando dados de: {artista}")
    
    # Faz 3 buscas com offset pra pegar mais músicas
    for offset in [0, 10]:
        resultado = sp.search(q=f"artist:{artista}", type="track", limit=10, offset=offset, market="BR")
        items = resultado["tracks"]["items"]
        
        for track in items:
            track_artist = track["artists"][0]["name"]
            if track_artist.lower() != artista.lower():
                continue
            
            tracks_lista.append({
                "artista_buscado": artista,
                "artista_track": track_artist,
                "musica": track["name"],
                "album": track["album"]["name"],
                "data_lancamento": track["album"]["release_date"],
                "duracao_ms": track["duration_ms"],
                "popularidade_musica": track.get("popularity", 0),
                "explicit": track["explicit"]
            })

df = pd.DataFrame(tracks_lista)
df = df.drop_duplicates(subset=["musica", "artista_buscado"])
df["duracao_min"] = (df["duracao_ms"] / 60000).round(2)
df["data_lancamento"] = pd.to_datetime(df["data_lancamento"], errors="coerce")
df["ano_lancamento"] = df["data_lancamento"].dt.year
df["explicit"] = df["explicit"].map({True: "Sim", False: "Não"})

os.makedirs("data", exist_ok=True)
df.to_csv("data/gospel_analytics.csv", index=False, encoding="utf-8-sig")


print(f"\nColeta concluída! {len(df)} músicas salvas em data/tracks_limpo.csv")
print(df.groupby("artista_buscado").agg(total=("musica","count"), anos=("ano_lancamento","nunique")).sort_values("total", ascending=False))