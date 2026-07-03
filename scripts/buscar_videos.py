import yt_dlp
import json
from pathlib import Path

#Hastags que quero procurar
HASHTAGS = ['#copadomundo']

#quatidade de vídeos para procurar de cada hashtag
QUANTIDADE = 66

#caminho do arquivo videos.json
CAMINHO_JSON = Path(__file__).parent.parent / 'src' / 'data' / 'videos.json'

#Função principal do código
def buscar_videos():
    """
    Busca videos no Youtube com as hashtags especificas e salva em videos.json
    """
    print("Iniciando busca de vídeos...")

    # o if depois de declarar todos_os_videos serve para evitar ids duplicados a cada nova pesquisa do script.
    todos_os_videos =[]
    if videos_existentes:
        id_contador = max([item['id'] for item in videos_existentes]) + 1
    else:
        id_contador = 1

    #condição caso já exista videos no video.json para adicionar mais vídeos
    if CAMINHO_JSON.exists():
        with open(CAMINHO_JSON) as f:
            videos_existentes = json.load(f)
    else:
        videos_existentes = []

    ids_existentes = [item['videoId'] for item in videos_existentes]

    #Para cada hashtag que vc quer procurar
    for hashtag in HASHTAGS:
        print(f"\n Procurando vídeos com {hashtag}...")

        try: #config do yt-dlp
            ydl_opts = {
                'quiet':True,
                'no_warnings': True,
                'extract_flat': 'in_playlist',
                'playlistend': QUANTIDADE,
            }
            #procurar no YT
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                #buscar com hashtag
                search_query = f'ytsearch{QUANTIDADE}:{hashtag}'
                resultado = ydl.extract_info(search_query, download=False)

            #processa os resultados
            if resultado and 'entries' in resultado:
                for video in resultado['entries']:
                    if video and 'id' in video and 'title' in video and video['id'] not in ids_existentes:
                        video_info ={
                            'id': id_contador,
                            'titulo': video['title'],
                            'subtitulo': f"Encontrado em: {hashtag}",
                            'videoId': video['id']
                        }
                        todos_os_videos.append(video_info)
                        id_contador += 1
                        print(f" Correto{video['title']}")
        
        except Exception as e:
            print(f" Erro ao procurar {hashtag}: {e}")

    #Salvar em json
    if todos_os_videos:
        try: #criar a pasta se não exitir
            CAMINHO_JSON.parent.mkdir(parents=True, exist_ok=True)
            #Salvar em json / - para juntar videos novos com videos antigos, foi necessário incluir "voideos_existentes +" 
            with open(CAMINHO_JSON, 'w', encoding='utf-8') as f:
                json.dump(videos_existentes + todos_os_videos, f, ensure_ascii=False, indent=2)

            print(f"\n Sucesso! {len(todos_os_videos)} videos salvos em {CAMINHO_JSON}")

        except Exception as e:
            print(f" Erro ao salvar JSON: {e}")
        
        else:
            print(f"\n Nenhum vídeo foi encontrado.")

#Executar

if __name__ == '__main__':
    buscar_videos()
