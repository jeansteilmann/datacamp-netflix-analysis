import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(filepath):
    """Carrega o dataset da Netflix a partir de um arquivo CSV."""
    df = pd.read_csv(filepath)
    if 'description' in df.columns:
        df = df.drop('description', axis=1)
    return df

def preprocess_movies(df):
    """Filtra o DataFrame para incluir apenas filmes e trata a coluna 'duration'."""
    movies_df = df[df['type'] == 'Movie'].copy()

    movies_df.dropna(subset=['duration'], inplace=True)

    movies_df['duration'] = movies_df['duration'].astype(str).str.replace(' min', '', regex=False).astype(int)
    return movies_df

def analyze_90s_movies(movies_df):
    """
    Realiza a análise focada em filmes da década de 1990,
    encontrando a duração mais frequente e contando filmes de ação curtos.
    """

    movies_90s_df = movies_df[(movies_df['release_year'] >= 1990) & (movies_df['release_year'] <= 1999)].copy()

    most_frequent_duration_90s = int(movies_90s_df['duration'].mode()[0])
    print(f"Duração mais comum para filmes dos anos 90: {most_frequent_duration_90s} minutos.")

    is_action = movies_90s_df['genre'].str.contains('Action', case=False, na=False)
    is_short = movies_90s_df['duration'] < 90
    action_movies_90s_short_df = movies_90s_df[is_action & is_short].copy()

    short_movie_count = int(action_movies_90s_short_df.shape[0])
    print(f"Total de filmes de Ação dos anos 90 com menos de 90 minutos: {short_movie_count}.")

    return short_movie_count, most_frequent_duration_90s, movies_90s_df

def plot_duration_distribution(df, filename="distribuicao_duracao_90s.png"):
    """
    Plota a distribuição da duração dos filmes da década de 1990.
    Salva o gráfico em um arquivo PNG na pasta 'images'.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(df['duration'], bins=20, kde=True, color='skyblue', edgecolor='black')
    plt.title('Distribuição da Duração dos Filmes da Década de 1990')
    plt.xlabel('Duração (minutos)')
    plt.ylabel('Número de Filmes')
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.savefig(os.path.join('images', filename))
    plt.close()
    print(f"Gráfico salvo como: images/{filename}")


def plot_top_genres(df, top_n=10, filename="top_generos_90s.png"):
    """
    Plota os N gêneros mais frequentes entre os filmes da década de 1990.
    Salva o gráfico em um arquivo PNG na pasta 'images'.
    """
    all_genres = df['genre'].fillna('').str.split(', ').explode()
    genre_counts = all_genres.value_counts().head(top_n)

    plt.figure(figsize=(12, 7))
    sns.barplot(x=genre_counts.values, y=genre_counts.index, hue=genre_counts.index, palette='viridis')
    plt.title(f'Top {top_n} Gêneros de Filmes na Década de 1990')
    plt.xlabel('Número de Filmes')
    plt.ylabel('Gênero')
    plt.tight_layout()
    plt.savefig(os.path.join('images', filename))
    plt.close()
    print(f"Gráfico salvo como: images/{filename}")


if __name__ == "__main__":
    file_path = "netflix_data.csv"
    images_dir = 'images'

    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # Carrega e pré-processa os dados
    df_raw = load_data(file_path)
    movies_data = preprocess_movies(df_raw)

    short_action_movies_count, popular_duration, movies_90s_df = analyze_90s_movies(movies_data)

    # Gera e salva os gráficos
    plot_duration_distribution(movies_90s_df)
    plot_top_genres(movies_90s_df, top_n=10)
