from website import create_app

app = create_app()

if __name__ == '__main__' : #mean only when we run the file, we are going to validate the line below.
    app.run(debug=True) #this helps auto running the web server for us when changes are made.
    
