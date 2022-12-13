from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <html>
    <body>
        <h1>Flask App</h1>
        <p> Welcome to my python app</p>
        <a href = '/hello'> Go to Hello page</a>
    </body>
    </html>
    """
    return html


@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search results for: {term}</h1> <p> Sorting by {sort}</p>" 

@app.route('/add-comment')
def add_comment_form():
    return """
    <h1>Add comment</h1>
    <form method="POST">
        <input type='text' placeholder='comment' name ='comment'/>
        <input type='text' placeholder='undername' name = 'username'/>
        <button>Submit</button>
    </form> 
    """

@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form["username"]
    return f"""
    <h1>Saved your comment</h1>
    <ul>
    <li>Username: {username}</li>
    <li>Comment: {comment}</li>
    </ul>
    """

@app.route('/r/<subreddit>')
def show_comments(subreddit):
    return f"<h1>Browsing the {subreddit} subreddit</h1>"

@app.route("/r/<subreddit>/comments/<post_id>")
def show_subreddit(subreddit, post_id):
    return f"<h1>Viewing comments for the post with id: {post_id} from the {subreddit} subreddit</h1>"


POSTS: {
    1: "I like chicken tenders",
    2: "I hate mayo",
    3: "Double rainbow"
}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, "Post not found")
    return f"<p>{post}</p>"


app.run(host='0.0.0.0', port=81)