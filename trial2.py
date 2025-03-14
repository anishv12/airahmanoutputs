import pandas as pd
import plotly.express as px
import gradio as gr

# Function to load and plot 3D graph
def load_and_plot(tsv_points, tsv_labels):
    df_points = pd.read_csv(tsv_points, sep='\t')  # Load points TSV file
    df_labels = pd.read_csv(tsv_labels, sep='\t')  # Load labels TSV file
    
    if len(df_points.columns) < 3 or len(df_labels.columns) < 1:
        return "Error: Points file must have at least three columns, and labels file must have at least one column."
    
    df_points['label'] = df_labels.iloc[:, 0]  # Assign labels from the labels file
    
    fig = px.scatter_3d(df_points, x=df_points.columns[0], y=df_points.columns[1], z=df_points.columns[2], 
                         color='label', title="Interactive 3D Graph with Labels")  # Create 3D plot with color-coded labels
    fig.update_layout(scene=dict(aspectmode="cube"))  # Enable full 3D rotation
    return fig

# Specify local file paths for TSVs
points_file = "residual_conditional_25.tsv"
labels_file = "residual_conditional_instruments_22.tsv"

audio_files = {
    "Sample 1": "mg1.wav",
    "Sample 2": "mg2.wav",
    "Sample 3": "mg3.wav",
    "Original" : "og_audio.wav",
    "Flute" : "to_flute.wav",
    "Violin" : "to_violin.wav",
    "Xylophone" : "to_xylophone.wav",
    "Electronic to Rock" : "elec_Rock.wav",
    "Classical to Electronic" : "classical_elec.wav"
}

image_files = {
    "Visualization 1": "cluster.jpg",

}

with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as demo:
    gr.Markdown("""
    # 🎵 **Audio Samples** 🎶
    """)

    gr.Markdown("""## Model 1 : Musicgen""")
    gr.Markdown("""### Genre Steering : (Claasical to Rock)""")
    with gr.Row():
        gr.Audio(audio_files["Sample 1"], label="Sample 1")
        gr.Audio(audio_files["Sample 2"], label="Sample 2")
        gr.Audio(audio_files["Sample 3"], label="Sample 3")

    gr.Markdown("""### Instrument Steering""")
    with gr.Row():
        gr.Audio(audio_files["Original"], label="Original")
        gr.Audio(audio_files["Flute"], label="To Flute")
        gr.Audio(audio_files["Violin"], label="To Violin")
        gr.Audio(audio_files["Xylophone"], label="To Xylophone")
    gr.Markdown("""### Other Genre Steering Outputs""")
    with gr.Row():
        gr.Audio(audio_files["Electronic to Rock"], label="Electronic to Rock")
        gr.Audio(audio_files["Classical to Electronic"], label="Classical to Electronic")
    gr.Markdown("""## Clustering""")
    with gr.Row():
        gr.Image(image_files["Visualization 1"], label="Visualization 1")
        

    gr.Markdown("""## Interactive Graphs""")
    gr.Markdown("""3D visualization of preloaded data.""")
    plot_output = gr.Plot(value=load_and_plot(points_file, labels_file))

demo.launch()
