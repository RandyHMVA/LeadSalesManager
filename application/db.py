import pymysql
import json
import datetime
from flask import Flask
from lxml import etree
import time
import urllib


class database:

    def __init__(self):

        try:
            self.connection = pymysql.connect(host="oasisleads.c3gabbhvzqio.us-east-2.rds.amazonaws.com",
                                              user="god_user", password="00dl3s0fN00dl3s", db="OasisLeads",
                                              cursorclass=pymysql.cursors.DictCursor)

            self.cursor = self.connection.cursor()
            self.error = ""
            self.is_connected = True
        except Exception as e:
            self.error = e
            self.is_connected = False

########################################################################
#########################      LEADS     ###############################
########################################################################

    def get_lead_info(self):
        try:
            sql_select = "SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.email NOT LIKE '%%@no.com' AND Address NOT LIKE '%26 main street toms river nj%' AND Address NOT LIKE '%26 Main Street Toms River NJ%' AND t1.first_name NOT LIKE 'test' AND t1.first_name NOT LIKE 'no' AND t2.source NOT LIKE '%test%' AND t1.is_live = 1 AND t3.vendor_name NOT LIKE 'Apex Employees' AND t3.vendor_name NOT LIKE 'test keys' ORDER BY t2.added_on desc LIMIT 100"
            self.cursor.execute(sql_select)
            return self.cursor.fetchall()
        except:
            return False

    def get_lead_vendor(self, vlist):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.email NOT LIKE '%%@no.com' AND t1.email NOT LIKE '%%@no.com%%' AND Address NOT LIKE '%%26 main street toms river nj%%' AND Address NOT LIKE '%%26 Main Street Toms River NJ%%' AND t1.first_name NOT LIKE '%%test%%' AND t1.first_name NOT LIKE '%%no%%' AND t2.source NOT LIKE '%%test%%' AND t1.is_live = 1 AND t3.vendor_name NOT LIKE '%%test keys%%' AND t3.vendor_name = %s ORDER BY t2.added_on desc LIMIT 100"""
            self.cursor.execute(sql_select, (vlist))
            return self.cursor.fetchall()

    def get_lead_subvendor(self, svlist):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.email NOT LIKE '%%@no.com' AND t1.email NOT LIKE '%%@no.com%%' AND Address NOT LIKE '%%26 main street toms river nj%%' AND Address NOT LIKE '%%26 Main Street Toms River NJ%%' AND t1.first_name NOT LIKE '%%test%%' AND t1.first_name NOT LIKE '%%no%%' AND t2.source NOT LIKE '%%test%%' AND t1.is_live = 1 AND t3.vendor_name NOT LIKE '%%test keys%%' AND t4.sub_vendor_name = %s ORDER BY t2.added_on desc LIMIT 100"""
            self.cursor.execute(sql_select, (svlist))
            return self.cursor.fetchall() 

    def get_lead_fname(self, fname):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.email NOT LIKE '%%@no.com' AND t1.first_name LIKE %s AND t1.is_live = 1 ORDER BY t2.added_on desc"""
            self.cursor.execute(sql_select, (fname))
            return self.cursor.fetchall()

    def get_lead_lname(self, lname):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.email NOT LIKE '%%@no.com' AND t1.last_name LIKE %s AND t1.is_live = 1 ORDER BY t2.added_on desc"""
            self.cursor.execute(sql_select, (lname))
            return self.cursor.fetchall() 

    def get_lead_email(self, email):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.email NOT LIKE '%%@no.com' AND t1.email LIKE CONCAT('%%',%s,'%%') AND t1.is_live = 1 ORDER BY t2.added_on desc"""
            self.cursor.execute(sql_select, (email))
            return self.cursor.fetchall() 

    def get_lead_phone(self, phone):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.email NOT LIKE '%%@no.com' AND t1.phone LIKE %s AND t1.is_live = 1 ORDER BY t2.added_on desc"""
            self.cursor.execute(sql_select, (phone))
            return self.cursor.fetchall() 

    def get_lead_source(self, source):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.email NOT LIKE '%%@no.com' AND t2.source LIKE CONCAT('%%',%s,'%%') AND t1.is_live = 1 ORDER BY t2.added_on desc"""
            self.cursor.execute(sql_select, (source))
            return self.cursor.fetchall() 

    def get_lead_date(self, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE (t2.added_on BETWEEN %s AND %s) AND t1.email NOT LIKE '%%@no.com' AND t1.is_live = 1 ORDER BY t2.added_on desc"""
            self.cursor.execute(sql_select, (fromDate,toDate))
            return self.cursor.fetchall() 

    def get_lead_datefname(self, fname, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.first_name LIKE %s AND (t2.added_on BETWEEN %s AND %s) AND t1.email NOT LIKE '%%@no.com' AND t1.is_live = 1 ORDER BY t2.added_on desc"""
            self.cursor.execute(sql_select, (fname,fromDate,toDate))
            return self.cursor.fetchall()

    def get_lead_datelname(self, lname, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.last_name LIKE %s AND (t2.added_on BETWEEN %s AND %s) AND t1.email NOT LIKE '%%@no.com' AND t1.is_live = 1 ORDER BY t2.added_on desc"""
            self.cursor.execute(sql_select, (lname,fromDate,toDate))
            return self.cursor.fetchall() 

    def get_lead_dateemail(self, email, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.email LIKE CONCAT('%%',%s,'%%') AND (t2.added_on BETWEEN %s AND %s) AND t1.email NOT LIKE '%%@no.com' AND t1.is_live = 1 ORDER BY t2.added_on desc"""
            self.cursor.execute(sql_select, (email,fromDate,toDate))
            return self.cursor.fetchall() 

    def get_lead_datephone(self, phone, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t1.phone LIKE %s AND (t2.added_on BETWEEN %s AND %s) AND t1.email NOT LIKE '%%@no.com' AND t1.is_live = 1 ORDER BY t2.added_on desc"""
            self.cursor.execute(sql_select, (phone,fromDate,toDate))
            return self.cursor.fetchall() 

    def get_lead_datesource(self, source, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, CONCAT(t1.address,' ',t1.city,' ',t1.state,' ') AS Address, t1.lead_id, CONCAT(t1.phone,' ',t1.email) AS Contact, IFNULL(t1.teledrips_id, ' ') AS TeledripsID, IFNULL( t1.rep_id, ' ') AS RepID, t2.source, t2.added_on, IFNULL(t1.mailchimp_id, ' ') AS MailChimpID, t3.vendor_name as Vendors, t4.sub_vendor_name as SubVendors, t5.vertical AS Vertical FROM OasisLeads.leads as t1 INNER JOIN OasisLeads.lead_verticals AS t2 ON t1.lead_id = t2.lead_id INNER JOIN OasisLeads.vendors AS t3 ON t3.vendor_id = t2.vendor_id INNER JOIN OasisLeads.sub_vendors AS t4 ON t4.sub_vendor_id = t2.sub_vendor_id INNER JOIN OasisLeads.verticals AS t5 ON t2.vertical_id = t5.vertical_id WHERE t2.source LIKE CONCAT('%%',%s,'%%') AND (t2.added_on BETWEEN %s AND %s) AND t1.email NOT LIKE '%%@no.com' AND t1.is_live = 1 ORDER BY t2.added_on desc"""
            self.cursor.execute(sql_select, (source,fromDate,toDate))
            return self.cursor.fetchall() 

    def get_sub_vendors(self, vendor_id):
        sql_select = "SELECT sub_vendors.sub_vendor_id, sub_vendors.sub_vendor_name, sub_api_keys.sub_api_key, sub_vendors.creation_date FROM sub_vendors LEFT JOIN sub_api_keys ON sub_vendors.sub_vendor_id = sub_api_keys.sub_vendor_id WHERE vendor_id = %s"
        self.cursor.execute(sql_select, (vendor_id))

        return self.cursor.fetchall()

    def get_source_list(self):
        sql_select = "SELECT DISTINCT SC.source FROM source_codes AS SC"
        self.cursor.execute(sql_select)
        return self.cursor.fetchall()


    def delete_sub_vendor(self, vendor_id, sub_vendor_id):
        try:
            if self.valid_sub_vendors_parent(vendor_id, sub_vendor_id):
                sql_delete = "DELETE FROM sub_api_keys WHERE sub_vendor_id = %s "
                self.cursor.execute(sql_delete, (sub_vendor_id) )
                deleted_sub_api_key = self.cursor.rowcount
                self.connection.commit()

                sql_delete = "DELETE FROM sub_vendors WHERE sub_vendor_id = %s"
                self.cursor.execute(sql_delete, (sub_vendor_id) )
                deleted_sub_vendor = self.cursor.rowcount
                self.connection.commit()

                if deleted_sub_vendor and deleted_sub_api_key:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False

    def valid_sub_vendors_parent(self,vendor_id, sub_vendor_id):
        try:
            sql_select = "SELECT * FROM sub_vendors WHERE vendor_id = %s AND sub_vendor_id = %s"
            self.cursor.execute(sql_select, (vendor_id, sub_vendor_id) )
            data = self.cursor.fetchall()
            if len(data) == 1:
                return True
            else:
                return False
        except:
            return False

    def check_if_existing_vendor_id(self,vendor_id):
        try:
            sql_select = "SELECT api_key FROM api_keys WHERE vendor_id = %s"
            self.cursor.execute(sql_select, (vendor_id))
            fetched = self.cursor.fetchone()
        except:
            return False

        if fetched is not None:
            return True
        else:
            return False

########################################################################
#########################      SALES     ###############################
########################################################################

    def get_sale_fname(self, fname):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND t1.first_name LIKE %s"""
            self.cursor.execute(sql_select, (fname))
            return self.cursor.fetchall()

    def get_sale_lname(self, lname):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND t1.last_name LIKE %s """
            self.cursor.execute(sql_select, (lname))
            return self.cursor.fetchall() 

    def get_sale_source(self, source):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_idAND t2.source LIKE CONCAT('%%',%s,'%%') """
            self.cursor.execute(sql_select, (source))
            return self.cursor.fetchall() 

    def get_sale_policy(self, policy):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source,  IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND t2.policy_name LIKE CONCAT('%%',%s,'%%') """
            self.cursor.execute(sql_select, (policy))
            return self.cursor.fetchall() 

    def get_sale_notes(self, notes):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND t2.notes LIKE CONCAT('%%',%s,'%%') """
            self.cursor.execute(sql_select, (notes))
            return self.cursor.fetchall()

    def get_sale_agent(self, agent):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND t2.agent LIKE CONCAT('%%',%s,'%%') """
            self.cursor.execute(sql_select, (agent))
            return self.cursor.fetchall()

    def get_sale_date(self, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND (t2.Date BETWEEN %s AND %s) """
            self.cursor.execute(sql_select, (fromDate,toDate))
            return self.cursor.fetchall() 

    def get_sale_datefname(self, fname, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND t1.first_name LIKE %s AND (t2.Date BETWEEN %s AND %s) """
            self.cursor.execute(sql_select, (fname,fromDate,toDate))
            return self.cursor.fetchall()

    def get_sale_datelname(self, lname, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND t1.last_name LIKE %s AND (t2.Date BETWEEN %s AND %s) """
            self.cursor.execute(sql_select, (lname,fromDate,toDate))
            return self.cursor.fetchall() 

    def get_sale_datepolicy(self, policy, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND t2.policy_name LIKE CONCAT('%%',%s,'%%') AND (t2.Date BETWEEN %s AND %s) """
            self.cursor.execute(sql_select, (policy,fromDate,toDate))
            return self.cursor.fetchall() 

    def get_sale_datenotes(self, notes, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND t2.notes LIKE CONCAT('%%',%s,'%%') AND (t2.Date BETWEEN %s AND %s) """
            self.cursor.execute(sql_select, (notes,fromDate,toDate))
            return self.cursor.fetchall() 

    def get_sale_datesource(self, source, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND t2.source LIKE CONCAT('%%',%s,'%%') AND (t2.Date BETWEEN %s AND %s) """
            self.cursor.execute(sql_select, (source,fromDate,toDate))
            return self.cursor.fetchall()

    def get_sale_dateagent(self, agent, fromDate, toDate):
            sql_select = """SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, DATE_FORMAT (t2.Date,'%%Y-%%m-%%d') AS Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id AND t2.agent LIKE CONCAT('%%',%s,'%%') AND (t2.Date BETWEEN %s AND %s) """
            self.cursor.execute(sql_select, (agent,fromDate,toDate))
            return self.cursor.fetchall() 


    def get_sales(self):
            sql_select = "SELECT CONCAT(t1.first_name,' ',t1.last_name) AS Name, t2.policy_name, t2.agent, IFNULL(t2.customer_price, '') AS CustomerPrice, t2.down_deposit,t2.term, t2.source, IFNULL(t2.is_tele_dripped, ' ') AS IsTeleDripped, t2.notes, t2.Date, t2.notes_secondary FROM sales AS t2,leads AS t1 WHERE t1.lead_id = t2.lead_id  ORDER BY t2.Date desc"
            self.cursor.execute(sql_select)
            return self.cursor.fetchall()

    def insert_sale(self,lead_id,policy_name,agent,customer_price,down_deposit,term,source,is_tele_dripped,notes,notes_secondary,date):
        try:
            sql_insert = "INSERT INTO sales (lead_id, policy_name,agent,customer_price,down_deposit,term,source,is_tele_dripped,notes,Date,notes_secondary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(sql_insert, (lead_id,policy_name,agent,customer_price,down_deposit,term,source,is_tele_dripped,notes,date,notes_secondary))
            self.connection.commit()
            return True
        except:
            return False

    def data_listified(self,data):
        data_list = []
        for element in data:
            data_list.append(element)
        return data_list



