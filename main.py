from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()


@app.get('/')
def index():
    return {
        'name': 'Kazi Ehsanul Mubin',
        'age': '27',
    }


@app.get('/about')
def about():
    return {
        'name': 'Kazi Ehsanul Mubin',
        'age': '27',
        'about': 'I am a software engineer'
    }
