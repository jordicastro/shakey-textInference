import streamlit as st
import os
import subprocess
# from fragments import sidebarFrag

# Page Config
favicon = os.path.join(os.getcwd(), "assets", "favicon.ico")
logo = os.path.join(os.getcwd(), "assets", "logo.png")
logo_redtint = os.path.join(os.getcwd(), "assets", "logo_redtint.png")
logo_red = os.path.join(os.getcwd(), "assets", "logo_red.png")
st.set_page_config(
    page_title="Shakey - Text Inference",
    page_icon=favicon,
    # layout="wide",
)

# state
if "ngrams" not in st.session_state:
    st.session_state.ngrams = 4
if "num_prediction_words" not in st.session_state:
    st.session_state.num_prediction_words = 50
if "context" not in st.session_state:
    st.session_state.context = ""

# sidebar
def sidebar():
    with st.sidebar:
        st.logo(logo_red, size="large", icon_image=logo, link=None)

        "# Text Inference Settings ⛭"
        st.divider()

        "## N-Grams"

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
        )

        "## Prediction Words"

        st.session_state.num_prediction_words = st.slider(
            "num_prediction_words",
            1,
            100,
            50
        )


sidebar()

# main
"# Shakespearean Text Inference"
f"gram type: `{st.session_state.ngrams}`"
f"num prediction words: `{st.session_state.num_prediction_words}`"

# tabs
bigram, _3gram, _4gram, _5gram, _6gram, _7gram = st.tabs(["Bigram", "3-gram", "4-gram", "5-gram", "6-gram", "7-gram"])
if st.session_state.ngrams == 2:
    with bigram:
        st.write("Bigram")
elif st.session_state.ngrams == 3:
    with _3gram:
        st.write("3-gram")
elif st.session_state.ngrams == 4:
    with _4gram:
        st.write("4-gram")
elif st.session_state.ngrams == 5:
    with _5gram:
        st.write("5-gram")
elif st.session_state.ngrams == 6:
    with _6gram:
        st.write("6-gram")
elif st.session_state.ngrams == 7:
    with _7gram:
        st.write("7-gram")


st.session_state.context = st.text_area(
    "context",
    height=300,
    on_change=None,
    args=None,
    placeholder="Enter text...",
    label_visibility="hidden",
)

left, middle, right = st.columns(3)


if middle.button("Generate", use_container_width=True):
    st.session_state.context = st.session_state.context.strip()
    if not st.session_state.context:
        st.warning("Please enter some text in the context box.")
    else:
        st.session_state.context = st.session_state.context
        st.session_state.ngrams = st.session_state.ngrams
        st.session_state.num_prediction_words = st.session_state.num_prediction_words

        # Display the context
        f'## Context: `{st.session_state.context}`'
        f'## N-Grams: `{st.session_state.ngrams}`'
        f'## Prediction Words: `{st.session_state.num_prediction_words}`'

        ### Run the model
        # path: ../add_new_corpus.sh
        # run the model
        command = [
            "bash",
            "../query.sh",
            str(st.session_state.ngrams),
            str(st.session_state.num_prediction_words),
            st.session_state.context
        ]
        try:
            # Run the shell command and capture the output
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            output = result.stdout.strip()  # Get the standard output
            st.markdown(f"### Generated Text:\n{output}")
        except subprocess.CalledProcessError as e:
            st.error(f"Error running the query script: {e.stderr}")


