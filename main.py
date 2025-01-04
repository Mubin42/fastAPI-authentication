from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()


# Routes are called path in FastAPI
@app.get('/')   # this is path operation decorator
def index():    # this is path operation function
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
