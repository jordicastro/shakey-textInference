# Shakey - Text Inference

N-grams 2–7 trained on 20 Shakespeare plays.

## Streamlit web app
- View the website [here](https://shakey.streamlit.app/)

## Local setup

1. Clone the repository:
   ```bash
   git clone https://github.com/jordicastro/shakey-textInference.git
   ```
2. Navigate to the Streamlit directory:
   ```bash
   cd streamlit
   ```
3. Install the dependencies (in a virtual environment if Mac):
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

## Training Plays

| Play | Category |
| :--- | :------- |
| Romeo and Juliet | Tragedy |
| Hamlet | Tragedy |
| Macbeth | Tragedy |
| King Lear | Tragedy |
| Othello | Tragedy |
| The Life and Death of Julius Caesar | Tragedy |
| Twelfth Night | Comedy |
| A Midsummer Night’s Dream | Comedy |
| Much Ado About Nothing | Comedy |
| The Tempest | Comedy |
| As You Like It | Comedy |
| The Merchant of Venice | Comedy |
| The Winter’s Tale | Comedy |
| The Comedy of Errors | Comedy |
| The Taming of the Shrew | Comedy |
| King Henry IV Part I | History |
| King Henry IV Part II | History |
| The Life and Death of King John | History |
| Richard II | History |
| Henry V | History |

## Testing Plays

| Play | Category |
| :--- | :------- |
| Titus Andronicus | Tragedy |
| Timon of Athens | Tragedy |
| Coriolanus | Tragedy |
| Antony and Cleopatra | Tragedy |
| Two Gentlemen of Verona | Comedy |
| Troilus and Cressida | Comedy |
| Pericles, Prince of Tyre | Comedy |
| Richard III | History |
| Henry VIII | History |
| Henry VI, Part 3 | History |

## Repo Structure

```
shakey-textInference/
├── data/
│   ├── corpora/
│   ├── grams/
│   └── testing/
├── scripts/
│   └── query.sh
├── streamlit/
│   ├── main.py
│   ├── pages/
│   │   ├── home.py
│   │   └── evalMetrics.py
│   └── assets/
├── testing/
│   └── evalAllModelsMetrics.sh
```

## Data
- `/corpora` folder containing plays to train the models.
- `/grams` folder contains `.json` files with the N-gram models (trained on 20 plays).
- `/testing` folder contains `quotes.json`: the test quotes to evaluate the models.

## Scripts
- `add_new_corpus.sh`: script to add a new training corpus to each model.
- `test_successor_map.sh`: script to test the successor map of each model using quotes from `scripts/utils.py`.
- `query.sh`: script to query the models from Streamlit.

## Streamlit
- `main.py`: main file to run the Streamlit app (`streamlit run main.py`).

  **Pages**
  - `home.py`: home page with the large text area to query the models.
  - `evalMetrics.py`: page containing the evaluation metrics and important links.
- `/assets`: folder containing images and documents.

## Testing
- `evalAllModelsMetrics.sh`: script to evaluate all models using the test quotes in `testing/quotes.json`.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
