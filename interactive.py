import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns
import streamlit as st

# Setze Seaborn-Thema für konsistente und ansprechende Plots
sns.set_theme(style="whitegrid")

def calculate_pearson(x, y):
    """Manuelle Pearson-Berechnung"""
    n = len(x)
    sum_xy = np.sum(x * y)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_y2 = np.sum(y**2)
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
    
    return numerator / denominator if denominator != 0 else 0

def generate_linear_data(r, sample_size):
    """
    Generiere lineare Daten mit einem bestimmten Pearson-Korrelationskoeffizienten r.
    """
    # Generiere unabhängige Standardnormalverteilte Daten für x und z
    x = np.random.normal(0, 1, sample_size)
    z = np.random.normal(0, 1, sample_size)
    
    # Erzeuge y mit gewünschtem Korrelationskoeffizienten r
    y = r * x + np.sqrt(1 - r**2) * z
    
    # Skaliere x auf den Bereich [0, 10]
    x = (x - np.min(x)) / (np.max(x) - np.min(x)) * 10
    
    # Skaliere y auf den Bereich [0, 10]
    y = (y - np.min(y)) / (np.max(y) - np.min(y)) * 10
    
    return x, y

def generate_nonlinear_data(noise, sample_size):
    """
    Generiere nichtlineare (quadratische) Daten.
    """
    x = np.linspace(0, 10, sample_size)
    y = 0.5*(x-5)**2 + np.random.normal(0, noise, sample_size)
    return x, y

def generate_random_data(noise, sample_size):
    """
    Generiere zufällige Daten ohne Zusammenhang.
    """
    x = np.random.normal(5, 2, sample_size)
    y = np.random.normal(5, 2, sample_size)
    return x, y

def plot_regression_line(x, y):
    """
    Berechnet und zeichnet die Regressionslinie basierend auf den Daten.
    """
    slope, intercept = np.polyfit(x, y, 1)
    plt.plot(x, slope * x + intercept, 'r--', lw=2, label='Regressionslinie')

def display_formula():
    """
    Zeigt die Formel für den Pearson-Korrelationskoeffizienten an.
    """
    st.markdown(r"""
    ## Pearson-Korrelationskoeffizient Formel

    Der Pearson-Korrelationskoeffizient $r$ misst die Stärke und Richtung der linearen Beziehung zwischen zwei Variablen $X$ und $Y$.

    Die Formel lautet:

    $$
    r = \frac{n \sum xy - (\sum x)(\sum y)}{\sqrt{(n \sum x^2 - (\sum x)^2)(n \sum y^2 - (\sum y)^2)}}
    $$

    **Interpretation von $r$:**

    - **$r = 1$:** Perfekte positive lineare Korrelation
    - **$r = -1$:** Perfekte negative lineare Korrelation
    - **$r = 0$:** Keine lineare Korrelation

    **Bestimmtheitsmaß ($r^2$):** Gibt an, wie viel Prozent der Varianz der einen Variable durch die andere Variable erklärt wird.

    **P-Wert:** Gibt an, ob die beobachtete Korrelation statistisch signifikant ist.
    """)

def update_plot(dataset_type, r, noise, sample_size, show_line):
    plt.figure(figsize=(10, 6))
    
    # Datensatz generieren und Titel festlegen
    if dataset_type == "Linear":
        x, y = generate_linear_data(r, sample_size)
        title = f"Lineare Beziehung (r={r})"
    elif dataset_type == "Nichtlinear (quadratisch)":
        x, y = generate_nonlinear_data(noise, sample_size)
        title = "Nichtlinearer Zusammenhang (quadratisch)"
    elif dataset_type == "Zufällig":
        x, y = generate_random_data(noise, sample_size)
        title = "Zufällige Verteilung"
    
    # Berechne Korrelation
    r_manual = calculate_pearson(x, y)
    r_scipy, p_value = pearsonr(x, y)
    r_squared = r_scipy**2
    
    # Plot
    if dataset_type == "Linear":
        color = 'teal'
    elif dataset_type == "Nichtlinear (quadratisch)":
        color = 'purple'
    else:  # Zufällig
        color = 'orange'
    
    plt.scatter(x, y, c=color, alpha=0.7, label='Datenpunkte')
    plt.title(f"{title}\nPearson r: {r_manual:.2f} (manuell) | {r_scipy:.2f} (scipy)")
    plt.xlabel("X")
    plt.ylabel("Y")
    
    # Achsenbegrenzungen anpassen
    if dataset_type == "Linear":
        plt.xlim(0, 10)
        plt.ylim(0, 10)
    elif dataset_type == "Nichtlinear (quadratisch)":
        plt.xlim(0, 10)
        plt.ylim(min(y) - noise, max(y) + noise)
    elif dataset_type == "Zufällig":
        plt.xlim(np.min(x) - noise, np.max(x) + noise)
        plt.ylim(np.min(y) - noise, np.max(y) + noise)
    
    # Regressionslinie hinzufügen, falls ausgewählt und sinnvoll
    if show_line and dataset_type == "Linear":
        plot_regression_line(x, y)
        plt.legend()
    
    st.pyplot(plt)
    plt.close()
    
    # Zusätzliche Statistiken anzeigen
    if dataset_type in ["Linear", "Nichtlinear (quadratisch)", "Zufällig"]:
        st.markdown(f"""
        **Pearson r:** {r_manual:.2f} (manuell) | {r_scipy:.2f} (scipy)

        **Bestimmtheitsmaß ($r^2$):** {r_squared:.2f}
        
        **P-Wert:** {p_value:.4f}
        """)
    
    # Erklärung basierend auf Datensatztyp
    if dataset_type == "Linear":
        st.markdown("""
        **Interpretation:**
        
        Ein Pearson-Korrelationskoeffizient von $r$ zeigt eine $r$-starke lineare Beziehung zwischen $X$ und $Y$.
        
        - **$r > 0$:** Positive Korrelation – wenn $X$ steigt, steigt $Y$.
        - **$r < 0$:** Negative Korrelation – wenn $X$ steigt, sinkt $Y$.
        - **$r = 0$:** Keine lineare Korrelation.
        """)
    elif dataset_type == "Nichtlinear (quadratisch)":
        st.markdown("""
        **Interpretation:**
        
        Der Pearson-Korrelationskoeffizient ist für nichtlineare Beziehungen wie eine quadratische Beziehung weniger aussagekräftig. Obwohl es eine starke Beziehung zwischen $X$ und $Y$ gibt, spiegelt $r$ nur die lineare Komponente dieser Beziehung wider.
        """)
    elif dataset_type == "Zufällig":
        st.markdown("""
        **Interpretation:**
        
        Ein Pearson-Korrelationskoeffizient nahe 0 zeigt keine lineare Korrelation zwischen $X$ und $Y$. Dies deutet darauf hin, dass die Datenpunkte zufällig verteilt sind und keine erkennbare Beziehung zwischen den Variablen besteht.
        """)

def main():
    st.set_page_config(page_title="Pearson-Korrelation Visualisierung", layout="wide")
    st.title("Interaktive Pearson-Korrelation Visualisierung")
    
    # Einführungstext
    st.markdown("""
    **Der Pearson-Korrelationskoeffizient** ist ein Maß für die Stärke und Richtung der linearen Beziehung zwischen zwei Variablen. 
    Diese Anwendung ermöglicht es dir, perfekte lineare Datensätze zu generieren und den Einfluss des Korrelationskoeffizienten auf die Daten zu untersuchen.
    """)

    # Sidebar für die Parameter
    st.sidebar.header("Parameter Einstellungen")
    
    # Auswahl des Datensatztyps
    dataset_type = st.sidebar.selectbox(
        "Datensatz Typ:",
        ["Linear", "Nichtlinear (quadratisch)", "Zufällig"]
    )
    
    # Parameter basierend auf dem ausgewählten Datensatztyp festlegen
    if dataset_type == "Linear":
        r = st.sidebar.slider(
            "Pearson r:",
            min_value=-1.0,
            max_value=1.0,
            value=0.0,
            step=0.05,
            help="Steuert die Stärke und Richtung der linearen Beziehung zwischen X und Y."
        )
        sample_size = st.sidebar.slider(
            "Datenpunkte:",
            min_value=10,
            max_value=200,
            value=50,
            step=10,
            help="Wähle die Anzahl der Datenpunkte, die generiert werden sollen."
        )
        show_line = st.sidebar.checkbox(
            "Regressionslinie zeigen",
            value=False,
            help="Zeigt die beste lineare Anpassungslinie für die Daten."
        )
        # Aktualisiere den Plot basierend auf den Parametern
        update_plot(dataset_type, r, None, sample_size, show_line)
    
    elif dataset_type == "Nichtlinear (quadratisch)":
        noise = st.sidebar.slider(
            "Rauschen:",
            min_value=0.1,
            max_value=5.0,
            value=2.0,
            step=0.1,
            help="Bestimmt die Menge an zufälligem Rauschen, das den Daten hinzugefügt wird."
        )
        sample_size = st.sidebar.slider(
            "Datenpunkte:",
            min_value=10,
            max_value=200,
            value=50,
            step=10,
            help="Wähle die Anzahl der Datenpunkte, die generiert werden sollen."
        )
        # Aktualisiere den Plot basierend auf den Parametern
        update_plot(dataset_type, None, noise, sample_size, False)
    
    elif dataset_type == "Zufällig":
        noise = st.sidebar.slider(
            "Rauschen:",
            min_value=0.1,
            max_value=5.0,
            value=2.0,
            step=0.1,
            help="Bestimmt die Menge an zufälligem Rauschen, das den Daten hinzugefügt wird."
        )
        sample_size = st.sidebar.slider(
            "Datenpunkte:",
            min_value=10,
            max_value=200,
            value=50,
            step=10,
            help="Wähle die Anzahl der Datenpunkte, die generiert werden sollen."
        )
        # Aktualisiere den Plot basierend auf den Parametern
        update_plot(dataset_type, None, noise, sample_size, False)
    
    # Anzeige der Pearson-Formel
    display_formula()
    
    # Erklärung zum Pearson-Korrelationskoeffizienten
    st.markdown(r"""
    ## Was ist der Pearson-Korrelationskoeffizient?

    Der **Pearson-Korrelationskoeffizient** ($r$) ist ein statistisches Maß, das die Stärke und Richtung einer linearen Beziehung zwischen zwei Variablen beschreibt.

    ### **Interpretation von $r$:**

    - **$r = 1$:** Perfekte positive lineare Korrelation. Wenn $X$ steigt, steigt auch $Y$ in perfekter Harmonie.
    - **$r = -1$:** Perfekte negative lineare Korrelation. Wenn $X$ steigt, sinkt $Y$ in perfekter Harmonie.
    - **$r = 0$:** Keine lineare Korrelation. Es besteht keine erkennbare lineare Beziehung zwischen $X$ und $Y$.
    - **Zwischen -1 und 1:** Je näher $r$ an 1 oder -1 liegt, desto stärker ist die lineare Korrelation.

    ### **Bestimmtheitsmaß ($r^2$):**

    Das Bestimmtheitsmaß gibt an, wie viel Prozent der Varianz einer Variable durch die andere Variable erklärt wird. Zum Beispiel bedeutet $r^2 = 0.81$, dass 81% der Varianz von $Y$ durch $X$ erklärt wird.

    ### **P-Wert:**

    Der **P-Wert** gibt an, ob die beobachtete Korrelation statistisch signifikant ist. Ein kleiner P-Wert (typischerweise < 0.05) deutet darauf hin, dass die beobachtete Korrelation nicht zufällig entstanden ist.

    ### **Wichtige Hinweise:**

    - Der Pearson-Korrelationskoeffizient misst nur **lineare** Beziehungen. Bei nichtlinearen Beziehungen kann er irreführend sein.
    - Korrelation impliziert **keine Kausalität**. Ein hoher $r$ bedeutet nicht, dass eine Variable die andere verursacht.
    """)

if __name__ == "__main__":
    main()
