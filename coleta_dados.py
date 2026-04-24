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

    # Busca tracks do artista
    resultado = sp.search(q=f"artist:{artista}", type="track", limit=10, market="BR")
    items = resultado["tracks"]["items"]

    if not items:
        print(f"Nenhuma track encontrada para: {artista}")
        continue

    for track in items:
        # Pega info do artista principal da track
        artist_info = track["artists"][0]

        tracks_lista.append({
            "artista_buscado": artista,
            "artista_track": artist_info["name"],
            "musica": track["name"],
            "album": track["album"]["name"],
            "data_lancamento": track["album"]["release_date"],
            "duracao_ms": track["duration_ms"],
            "popularidade_musica": track.get("popularity", 0),
            "explicit": track["explicit"]
        })

df = pd.DataFrame(tracks_lista)
df["duracao_min"] = (df["duracao_ms"] / 60000).round(2)

os.makedirs("data", exist_ok=True)
df.to_csv("data/tracks.csv", index=False, encoding="utf-8-sig")

print(f"\nColeta concluída! {len(df)} músicas salvas em data/tracks.csv")
print(df.head())