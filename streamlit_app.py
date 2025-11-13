
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import numpy as np

# Configuração da página inicial do Streamlit
st.set_page_config(
    page_title="ODS 4: Educação de Qualidade Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 1. SIMULAÇÃO E CARREGAMENTO DE DADOS ---
# NOTA: Em um projeto real, esta seção carregaria um arquivo .csv ou .xlsx.
# Para este ambiente, vamos simular um DataFrame robusto com dados do ODS 4.

@st.cache_data
def load_data():
    """Cria um DataFrame simulado para o ODS 4 (Educação de Qualidade)."""
    
    countries = ['Brasil', 'Chile', 'México', 'Alemanha', 'Japão', 'Índia', 'África do Sul']
    years = range(2000, 2024)
    
    # Indicadores-chave para ODS 4
    indicators = {
        '% Conclusão Escolar (Ensino Médio)': {
            'min': 40, 'max': 99, 'progression_factor': {'Brasil': 1.8, 'Chile': 2.5, 'México': 1.5, 'Alemanha': 0.8, 'Japão': 0.5, 'Índia': 3.0, 'África do Sul': 2.0}
        },
        'Taxa de Alfabetização Adulta (%)': {
            'min': 75, 'max': 99, 'progression_factor': {'Brasil': 0.5, 'Chile': 0.3, 'México': 0.4, 'Alemanha': 0.1, 'Japão': 0.1, 'Índia': 1.5, 'África do Sul': 0.8}
        },
        'Gasto Público em Educação (% do PIB)': {
            'min': 3.0, 'max': 7.0, 'progression_factor': {'Brasil': 0.0, 'Chile': 0.2, 'México': -0.1, 'Alemanha': 0.1, 'Japão': 0.0, 'Índia': 0.3, 'África do Sul': 0.2}
        }
    }
    
    data = []
    
    # Geração dos dados simulados
    for country in countries:
        for year in years:
            for indicator_name, props in indicators.items():
                
                # Base de valor com ruído aleatório
                base_value = props['min'] + (props['max'] - props['min']) * ((year - 2000) / (len(years) - 1)) * 0.5
                
                # Aplica o fator de progressão específico do país
                progression = props['progression_factor'][country] * (year - 2000) * 0.1
                
                value = np.clip(base_value + progression + np.random.uniform(-3, 3), props['min'], props['max'])
                
                # Arredonda valores (percentuais para 1 casa decimal, gasto para 2)
                decimal_places = 1 if '%)' in indicator_name or '%' in indicator_name else 2
                value = round(value, decimal_places)
                
                data.append({
                    'País': country,
                    'Ano': year,
                    'Indicador': indicator_name,
                    'Valor': value
                })
                
    df = pd.DataFrame(data)
    
    return df

df = load_data()

# --- 2. TÍTULO E INTRODUÇÃO ---
st.title("🎯 Progresso dos Objetivos de Desenvolvimento Sustentável (ODS)")
st.subheader("ODS 4: Educação de Qualidade - Análise Interativa de Indicadores")

st.markdown("""
Esta aplicação demonstra o progresso simulado de países em indicadores-chave do ODS 4 (Educação de Qualidade) ao longo do tempo.
Utilize a barra lateral para filtrar os dados e explorar as tendências.
""")
# 

# --- 3. BARRA LATERAL (FILTROS) ---
st.sidebar.header("Filtros de Dados")

# Seleção de País
selected_countries = st.sidebar.multiselect(
    "Selecione os Países para Comparação",
    options=df['País'].unique(),
    default=['Brasil', 'Alemanha', 'Índia']
)

# Seleção de Indicador
indicator_options = df['Indicador'].unique().tolist()
selected_indicator = st.sidebar.selectbox(
    "Selecione o Indicador de ODS 4",
    options=indicator_options
)

# Filtro de Ano Mínimo
min_year_slider = st.sidebar.slider(
    "Ano Mínimo de Análise",
    min_value=int(df['Ano'].min()),
    max_value=int(df['Ano'].max()),
    value=int(df['Ano'].min())
)

# Aplicar todos os filtros
df_filtered = df[
    (df['País'].isin(selected_countries)) & 
    (df['Indicador'] == selected_indicator) & 
    (df['Ano'] >= min_year_slider)
]

# --- 4. VISUALIZAÇÃO DE DADOS INTERATIVA (PLOTLY) ---
st.header(f"📈 Tendência Histórica do Indicador: {selected_indicator}")

if df_filtered.empty:
    st.warning("Nenhum dado encontrado com os filtros selecionados. Por favor, ajuste os países ou o ano.")
else:
    # Gerar gráfico de linha com Plotly Express
    fig = px.line(
        df_filtered,
        x='Ano',
        y='Valor',
        color='País',
        title=f'{selected_indicator} por País (Anos {min_year_slider} a {df_filtered["Ano"].max()})',
        labels={'Valor': selected_indicator, 'Ano': 'Ano'},
        markers=True,
        template="plotly_white"
    )
    
    fig.update_layout(
        xaxis_title="Ano",
        yaxis_title=selected_indicator,
        legend_title="País",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

# --- 5. ANÁLISE EXPLORATÓRIA DE DADOS (EDA) COM PANDAS ---
st.header("🔍 Análise Exploratória (Pandas)")

# Análise 1: Progresso nos Últimos Anos
st.subheader(f"Progresso de {selected_indicator} (Análise de 5 Anos)")

latest_year = df['Ano'].max()
five_years_ago = latest_year - 4 # Para uma análise de 5 anos

df_progress = df[
    (df['Indicador'] == selected_indicator) & 
    (df['País'].isin(selected_countries)) &
    (df['Ano'].isin([latest_year, five_years_ago]))
]

if not df_progress.empty:
    # Pivotar a tabela para calcular a diferença
    df_pivot = df_progress.pivot_table(
        index='País', 
        columns='Ano', 
        values='Valor'
    ).reset_index()

    # Cálculo do Progresso
    col_latest = latest_year
    col_past = five_years_ago
    
    if col_latest in df_pivot.columns and col_past in df_pivot.columns:
        df_pivot['Progresso (Absoluto)'] = df_pivot[col_latest] - df_pivot[col_past]
        df_pivot['Progresso (%)'] = (df_pivot[col_latest] / df_pivot[col_past] - 1) * 100
        
        # Formatação para exibição
        df_pivot = df_pivot.rename(columns={col_latest: f'Valor em {col_latest}', col_past: f'Valor em {col_past}'})
        df_display = df_pivot[['País', f'Valor em {col_latest}', f'Valor em {col_past}', 'Progresso (Absoluto)', 'Progresso (%)']]
        
        # Estilização: destaque para o maior progresso
        styled_df = df_display.style.format({
            f'Valor em {col_latest}': '{:.1f}',
            f'Valor em {col_past}': '{:.1f}',
            'Progresso (Absoluto)': '{:+.1f}',
            'Progresso (%)': '{:+.1f}%'
        }).background_gradient(subset=['Progresso (Absoluto)'], cmap='YlGn')
        
        st.markdown(f"**Variação Absoluta e Percentual (de {five_years_ago} a {latest_year})**")
        st.dataframe(styled_df, use_container_width=True)
    else:
        st.info(f"Dados incompletos para os anos {latest_year} e {five_years_ago} para o indicador selecionado.")

# Análise 2: Tabela de Dados Brutos
st.subheader("Tabela de Dados Brutos Filtrados")
st.dataframe(df_filtered.sort_values(by=['País', 'Ano']), use_container_width=True)

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido com Python, Pandas e Streamlit.")
