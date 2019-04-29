# coding: UTF-8
from flask import Flask, render_template, request
from rozbierz_potegowanie import rozb_pot

app = Flask(__name__)

#calculation and result generation
@app.route('/potegowanie', methods=['POST'])
def do_potegowanie():
    liczba = "'" + (request.form['liczba']) + "'"
    potega = request.form['potega']
    wynik = (rozb_pot(liczba, potega))

    if type(wynik) != str:
        mnozenie = wynik[0]
        dodawanie = wynik[1]

    return render_template('potegowanie.html',
                           ta_liczba=liczba,
                           ta_potega=potega,
                           ten_wynik=wynik,)
                           #to_mnozenie=mnozenie,
                           #to_dodawanie=dodawanie,)

#collecting data
@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Rozbierz potegowanie')
