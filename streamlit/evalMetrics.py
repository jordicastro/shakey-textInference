import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt

# Data Results Graphs
# 1. N-gram load times from training on 10 to 20 plays
# 2. N-gram cluster graph: precision, recall, f1, accuracy
# 3. trained plays vs tested plays vs total plays (ratio / percentage)
# 4. percentage of category of each play: trained vs tested
# 5. ATTACH:
#     - paper
#     - github link
#     - powerpoint (maybe in github or separate .pptx file)
this_dir = os.path.dirname(__file__)
favicon = os.path.join(this_dir, "assets", "favicon.ico")
logo = os.path.join(this_dir, "assets", "logo.png")
logo_sm = os.path.join(this_dir, "assets", "logo_sm.png")
logo_md = os.path.join(this_dir, "assets", "logo_md.png")
logo_lg = os.path.join(this_dir, "assets", "logo_lg.png")

st.set_page_config(
    page_title="Shakey - Evaluation Metrics",
    page_icon=favicon,
    # layout="wide",
)

@st.dialog(title="Evaluation Metrics", width="large")
def modal():
    st.markdown(
        """
        ### Design
        **100** quotes from **10** unseen plays were used to test the models.
        For each quote, the model was asked to predict the next word
        > returning a list of the top $k$ most likely words
        """
        """
        ### Logic
        ```python
        if target in guess_words:
            TP += 1 # correct guess
        else:
            FN += 1 # incorrect guess

        for guess in guess_words:
            if guess != target:
                FP += 1 # false positives
        ```
        ### Algorithms
        """
    )
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.latex(r'''
            \text{Precision} = \frac{TP}{TP + FP}
            ''')
    with col2:
        st.latex(r'''
            \text{Recall} = \frac{TP}{TP + FN}
            ''')
    with col3:
        st.latex(r'''
            \text{F1} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
            ''')

def ngrams_segmented_control():
    ngrams = {
            2: "bigram",
            3: "3-gram",
            4: "4-gram",
            5: "5-gram",
            6: "6-gram",
            7: "7-gram",
        }
    
    st.session_state.ngrams = st.segmented_control(
            "ngrams",
            options=ngrams.keys(),
            format_func=lambda x: ngrams[x],
            default=4,
            selection_mode="single",
            label_visibility="hidden",
        )


# sidebar
def sidebar():
    with st.sidebar:
        st.logo(logo_lg, size="large", icon_image=logo, link=None)

        "# Text Inference Settings ⛭"
        st.divider()

        "## N-Grams"

        ngrams_segmented_control()

        "## Prediction Words"

        st.session_state.num_prediction_words = st.slider(
            "num_prediction_words",
            1,
            100,
            50,
            label_visibility="hidden",
        )
        st.divider()
        st.page_link("home.py", label="Home", icon="🏠")


sidebar()


"# Data Results / Evaluation Metrics"
st.divider()

# 1. N-gram load times from training on 10 to 20 plays
"### N-gram Load Times from Training on 10 to 20 Plays"
data_load_times = pd.DataFrame(
    data={
        "bigram": [0.03, 0.03, 0.03, 0.03, 0.04, 0.04, 0.05, 0.05, 0.05, 0.05, 0.05],
        "3-gram": [0.70, 0.73, 0.80, 0.85, 0.88, 0.97, 1.04, 1.10, 1.12, 1.25, 1.31],
        "4-gram": [1.37, 1.51, 1.66, 1.74, 1.99, 2.17, 2.23, 2.37, 2.53, 2.70, 3.49],
        "5-gram": [1.81, 1.96, 2.11, 2.37, 2.71, 2.71, 2.90, 3.15, 3.24, 3.61, 4.42],
        "6-gram": [2.20, 2.26, 2.46, 2.88, 3.00, 3.16, 3.48, 3.89, 3.81, 4.15, 4.45],
        "7-gram": [2.44, 2.66, 2.79, 3.10, 3.50, 3.54, 3.86, 3.82, 3.91, 4.26, 4.56],
    },
    index=["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"],
)
st.line_chart(
    data_load_times,
    use_container_width=True,
    x_label="Plays",
    y_label="Load Time (s)",
)

st.divider()
# 2. n-gram cluster graph: precision, recall, f1, accuracy
k1, k3, k5 = st.tabs(["$\small{k=1}$", "$\small{k=3}$", "$\small{k=5}$"])

with k1:

    "### Precision, Recall, F1, Accuracy for $\small{k=1}$"


    data_eval_metrics_k1 = pd.DataFrame(
        data={
            "Precision": [0.0857, 0.1235, 0.0588],
            "Recall"   : [0.0900, 0.1000, 0.0200],
            "F1"       : [0.0878, 0.1105, 0.0299],
            "Accuracy" : [0.0459, 0.0585, 0.0152],
        },
        index=["Bigram", "3-gram", "4-gram"],
    )

    st.bar_chart(
        data_eval_metrics_k1,
        use_container_width=True,
        x_label="N-grams",
        y_label="Evaluation Metrics",
        stack=False,     
    )

with k3:
    "### Precision, Recall, F1, Accuracy for $\small{k=3}$"


    data_eval_metrics_k3 = pd.DataFrame(
        data={
            "Precision": [0.0559, 0.0845, 0.0571],
            "Recall"   : [0.1700, 0.1800, 0.0400],
            "F1"       : [0.0842, 0.1150, 0.0471],
            "Accuracy" : [0.0439, 0.0610, 0.0241],
        },
        index=["Bigram", "3-gram", "4-gram"],
    )

    st.bar_chart(
        data_eval_metrics_k3,
        use_container_width=True,
        x_label="N-grams",
        y_label="Evaluation Metrics",
        stack=False,
    )

with k5:
    "### Precision, Recall, F1, Accuracy for $\small{k=5}$"


    data_eval_metrics_k5 = pd.DataFrame(
        data={
            "Precision": [0.0463, 0.0710, 0.0667],
            "Recall"   : [0.2300, 0.2300, 0.0600],
            "F1"       : [0.0771, 0.1085, 0.0632],
            "Accuracy" : [0.0401, 0.0574, 0.0326],
        },
        index=["Bigram", "3-gram", "4-gram"],
    )

    st.bar_chart(
        data_eval_metrics_k5,
        use_container_width=True,
        x_label="N-grams",
        y_label="Evaluation Metrics",
        stack=False,
    )
# popover or modal to demonstrate algorithms and what k means

# QUESTIONS:
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("Evaluation Metrics Explained"):
        modal()

# for one of these, put them side by side using st.columns
# left: categories for trained
# right: categories for tested
# attach links using st.markdown or [st.link_button](https://docs.streamlit.io/develop/api-reference/widgets/st.link_button)

st.divider()

# 3. skip

# 4. percentage of category of each play: trained vs tested
labels = ['Tragedy', 'Comedy', 'History']
sizes = [0.45, 0.25, 0.30]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

"### Percentage of Category of Each Play: Trained vs Tested"
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.markdown(
        """
        ### Trained Plays
        """
    )
    st.pyplot(fig)

sizes = [0.40, 0.30, 0.30]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
with col2:
    st.markdown(
        """
        ### Tested Plays
        """
    )
    st.pyplot(fig)

sizes = [0.46, 0.27, 0.27]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
with col3:
    st.markdown(
        """
        ### Total Plays
        """
    )
    st.pyplot(fig)
st.divider()

"### Important Links"
st.link_button(
    label="GitHub",
    url="https://github.com/jordicastro/textInference",
    type="tertiary",
    icon="📦",
    disabled=False,
)
st.link_button(
    label="Figma",
    url="https://www.figma.com/design/2uO5IfvkznyVWSu2DmJmq6/shakey?node-id=0-1&t=4eN8dSqlIxEvMEBo-1",
    type="tertiary",
    icon="🎨",
    disabled=False,
)

with open("./assets/docs/Final_Text_Inference_Paper.pdf", "rb") as f:
    st.download_button(
        label="📄 Paper",
        data=f,
        file_name="Text_Inference_Paper_Castro.pdf",
        mime="application/pdf",
        type="tertiary",
    )

with open("./assets/docs/Final_Text_Inference_Presentation.pptx", "rb") as f:
    st.download_button(
        label="📊 Powerpoint",
        data=f,
        file_name="Text_Inference_Presentation_Castro.pptx",
        mime="application/pdf",
        type="tertiary",
    )