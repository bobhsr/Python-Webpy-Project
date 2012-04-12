import web

urls = (
    '/', 'index',
    '/hello', 'hello'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        form = web.input(name='Nobody')
        greeting = 'Hello %s;' % form.name

        # return greeting
        return render.index(greeting = greeting)

class hello:
    def GET(self):
       return render.hello_form()
    
    def POST(self):
        form = web.input(name='nobody',greet='hello')
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)

if __name__ == '__main__':
    app.run()
