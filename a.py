from bottle import *
import os





# Dæmi 2:
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

@route('/')
def index():
    return """
    
      <h1>halló heimur!</h1>
      <a href='/11'>val a<a/>
      <a href='/4'>val b<a/>
      """

@route('/mynd')
def index():
    return "<img src='static/stafura1.png'>"


#      <link rel="stylesheet" type="text/css" href="static/style.css">
@route('/<nr>')
def sida(nr):
    if nr == '11':
        return """
          <h1>Þetta er sida 1 xd</h1>

                <a href='/11'>sida1</a>
                <a href='/22'>sida2</a>
                <a href='/33'>sida3</a>
        """
    if nr == '22':
        return """
          <h1>Þetta er sida 2 xd</h1>
          <h1>nr.2</h1>

                <a href='/11'>sida1</a>
                <a href='/22'>sida2</a>
                <a href='/33'>sida3</a>
        """
    if nr == '33':
        return """
          <h1>Þetta er sida 3 ripperino</h1>
          <a href='/11'>sida1</a>
          <a href='/22'>sida2</a>
          <a href='/33'>sida3</a>


        """
    if nr == '4':
        return """
        
        <h1>Veldu uppáhalds stafinn þinn.</h1>
        
        <a href='/5'><img src='static/stafura1.png'></a>
        <a href='/6'><img src='static/stafurb.png'></a>
        <a href='/7'><img src='static/stafurc.png'></a>


        """
    if nr == '5':
        return """
          <h1>Þú hefur valið stafinn A.</h1>
          <img src='static/stafura1.png'>


        """
    if nr == '6':
        return """
          <h1>Þú hefur valið stafinn B.</h1>
          <img src='static/stafurb.png'>


        """
    if nr == '7':
        return """
          <h1>Þú hefur valið stafinn C.</h1>
          <img src='static/stafurc.png'>


        """


#run(host='localhost', port=8080)
run(host='0.0.0.0',port=os.environ.get('PORT'))
