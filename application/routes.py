from flask import render_template, flash, redirect, url_for, request, jsonify
from application import app
from application import keys
from application import api_validator
from application import json_errors
from application.api_calls import sub_vendors
from application.api_calls import leads
from application.api_calls import verticals
from application.api_calls import fields
from application.api_calls import vehicles
from application.api_calls import electric_companies
from application import db
from application import api

#veni vidi vici
@app.route('/')
@app.route('/index')
@app.route('/getting_started')
def index():
    return render_template('index.html', title='Oasis Leads')


########################################################################
##########################      MAIN     ###############################
########################################################################


@app.route('/testarea', methods = ['GET'])
def test_area():
    d = db.database()
    slead = d.get_lead_info()
    return render_template('test_area.html', title='Lead List', sleads=slead)

@app.route('/background_process')
def background_process():
	try:
		lang = request.args.get('proglang', 0, type=str)
		if lang.lower() == 'python':
			return jsonify(result='You are wise')
		else:
			return jsonify(result='Try again.')
	except Exception as e:
		return str(e)

########################################################################
#########################      LEADS     ###############################
########################################################################

@app.route('/byvendor', methods = ['GET'])
def byvendor():
    return render_template('byvendor.html', title='Oasis Leads')

@app.route('/bysubvendor', methods = ['GET'])
def bysubvendor():
    return render_template('bysubvendor.html', title='Oasis Leads')

@app.route('/listvendorarea')
def vendor_list():
	d = db.database()
	thelist = request.args.get('vlist',0, type=str)
	vlead = d.get_lead_vendor(thelist)
	return jsonify(vlead)

@app.route('/listsubvendorarea')
def subvendor_list():
	d = db.database()
	thelist = request.args.get('svlist',0, type=str)
	svlead = d.get_lead_subvendor(thelist)
	return jsonify(svlead)

@app.route('/search', methods = ['GET'])
def searchpage():
	d = db.database()
	sources = d.get_source_list()
	return render_template('search.html', sources=sources)

@app.route('/fname')
def fname():
	d = db.database()
	fname = request.args.get('search',0, type=str)
	svlead = d.get_lead_fname(fname)
	return jsonify(svlead)

@app.route('/lname')
def lname():
	d = db.database()
	lname = request.args.get('search',0, type=str)
	svlead = d.get_lead_lname(lname)
	return jsonify(svlead)

@app.route('/phonenum')
def phone():
	d = db.database()
	phone = request.args.get('search',0, type=str)
	svlead = d.get_lead_phone(phone)
	return jsonify(svlead)

@app.route('/email')
def email():
	d = db.database()
	email = request.args.get('search',0, type=str)
	svlead = d.get_lead_email(email)
	return jsonify(svlead)

@app.route('/source')
def source():
	d = db.database()
	source = request.args.get('search',0, type=str)
	svlead = d.get_lead_source(source)
	return jsonify(svlead)

@app.route('/sourceselect')
def sourcelist():
	d = db.database()
	source = request.args.get('source',0, type=str)
	svlead = d.get_lead_source(source)
	return jsonify(svlead)

@app.route('/daterange')
def searchdate():
	d = db.database()
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	getRange = d.get_lead_date(fromDate,toDate)
	return jsonify(getRange)

@app.route('/datefname')
def datefname():
	d = db.database()
	fname = request.args.get('search',0, type=str)
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	svlead = d.get_lead_datefname(fname,fromDate,toDate)
	return jsonify(svlead)

@app.route('/datelname')
def datelname():
	d = db.database()
	lname = request.args.get('search',0, type=str)
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	svlead = d.get_lead_datelname(lname,fromDate,toDate)
	return jsonify(svlead)

@app.route('/datephonenum')
def datephone():
	d = db.database()
	phone = request.args.get('search',0, type=str)
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	svlead = d.get_lead_datephone(phone,fromDate,toDate)
	return jsonify(svlead)

@app.route('/dateemail')
def dateemail():
	d = db.database()
	email = request.args.get('search',0, type=str)
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	svlead = d.get_lead_dateemail(email,fromDate,toDate)
	return jsonify(svlead)

@app.route('/datesource')
def datesource():
	d = db.database()
	source = request.args.get('search',0, type=str)
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	svlead = d.get_lead_datesource(source,fromDate,toDate)
	return jsonify(svlead)

########################################################################
#########################      SALES     ###############################
########################################################################

@app.route('/sales', methods = ['GET'])
def salespage():
	return render_template('sales.html')

@app.route('/insertsale')
def insertsale():
	d = db.database()
	data = request.args.getlist('saleinfo[]')
	sale = d.insert_sale(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[10],data[7],data[8],data[9])
	return jsonify(sale)

@app.route('/salefname')
def salefname():
	d = db.database()
	fname = request.args.get('search',0, type=str)
	sale = d.get_sale_fname(fname)
	return jsonify(sale)

@app.route('/salelname')
def salelname():
	d = db.database()
	lname = request.args.get('search',0, type=str)
	sale = d.get_sale_lname(lname)
	return jsonify(sale)

@app.route('/salenotes')
def salenotes():
	d = db.database()
	notes = request.args.get('search',0, type=str)
	sale = d.get_sale_notes(notes)
	return jsonify(sale)

@app.route('/salepolicy')
def salepolicy():
	d = db.database()
	policy = request.args.get('search',0, type=str)
	sale = d.get_sale_policy(policy)
	return jsonify(sale)

@app.route('/salesource')
def salesource():
	d = db.database()
	source = request.args.get('search',0, type=str)
	sale = d.get_sale_source(source)
	return jsonify(sale)

@app.route('/saleagent')
def saleagent():
	d = db.database()
	agent = request.args.get('search',0, type=str)
	sale = d.get_sale_agent(agent)
	return jsonify(sale)

@app.route('/datesalefname')
def datesalefname():
	d = db.database()
	fname = request.args.get('search',0, type=str)
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	svlead = d.get_sale_datefname(fname,fromDate,toDate)
	return jsonify(svlead)

@app.route('/datesalelname')
def datesalelname():
	d = db.database()
	lname = request.args.get('search',0, type=str)
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	svlead = d.get_sale_datelname(lname,fromDate,toDate)
	return jsonify(svlead)

@app.route('/datesalepolicy')
def datesalepolicy():
	d = db.database()
	policy = request.args.get('search',0, type=str)
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	svlead = d.get_sale_datepolicy(policy,fromDate,toDate)
	return jsonify(svlead)

@app.route('/datesaleagent')
def datesaleagent():
	d = db.database()
	agent = request.args.get('search',0, type=str)
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	svlead = d.get_sale_dateagent(agent,fromDate,toDate)
	return jsonify(svlead)

@app.route('/datesalesource')
def datesalesource():
	d = db.database()
	source = request.args.get('search',0, type=str)
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	svlead = d.get_sale_datesource(source,fromDate,toDate)
	return jsonify(svlead)

@app.route('/datesalenotes')
def datesalenotes():
	d = db.database()
	notes = request.args.get('search',0, type=str)
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	svlead = d.get_sale_datenotes(notes,fromDate,toDate)
	return jsonify(svlead)

@app.route('/saledaterange')
def searchsaledate():
	d = db.database()
	fromDate = request.args.get('fromDate',0, type=str)
	toDate = request.args.get('toDate',0, type=str)
	getRange = d.get_sale_date(fromDate,toDate)
	return jsonify(getRange)

@app.route('/listsales', methods = ['GET'])
def getsales():
    d = db.database()
    sales = d.get_sales()
    return render_template('saleslist.html', title='Sales List', sales=sales)

