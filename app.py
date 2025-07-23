from flask import Flask, render_template, request, jsonify
import pickle
import os

app = Flask(__name__, template_folder='templates_html')

# Load models and data
ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), 'templates')

with open(os.path.join(ARTIFACTS_DIR, 'book_names.pkl'), 'rb') as f:
    book_names = pickle.load(f)
with open(os.path.join(ARTIFACTS_DIR, 'book_pivot.pkl'), 'rb') as f:
    book_pivot = pickle.load(f)
with open(os.path.join(ARTIFACTS_DIR, 'final_rating.pkl'), 'rb') as f:
    final_rating = pickle.load(f)
with open(os.path.join(ARTIFACTS_DIR, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html', book_names=book_names)

@app.route('/recommend', methods=['POST'])
def recommend():
    book = request.form.get('book')
    if not book:
        return jsonify({'error': 'No book selected'}), 400
    try:
        # Find recommendations
        index = book_pivot.index.get_loc(book)
        distances, indices = model.kneighbors(book_pivot.iloc[index, :].values.reshape(1, -1), n_neighbors=6)
        recommended_books = []
        for i in indices.flatten()[1:]:
            rec_title = book_pivot.index[i]
            # Find image URL from final_rating DataFrame
            rec_row = final_rating[final_rating['title'] == rec_title].iloc[0] if not final_rating[final_rating['title'] == rec_title].empty else None
            image_url = rec_row['image_url'] if rec_row is not None and 'image_url' in rec_row else None
            recommended_books.append({'title': rec_title, 'image_url': image_url})
        return jsonify({'recommendations': recommended_books})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
