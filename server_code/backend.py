import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
  conn = sqlite3.connect(data_files['prison_management.db'])
  cursor = conn.cursor()
  res = list(cursor.execute('SELECT Name, VID FROM Gefaengnis'))
  return res

@anvil.server.callable
def get_direktor(vid):
  conn = sqlite3.connect(data_files['prison_management.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f'SELECT Direktor, Anzahl_freie_Zellen FROM Verwaltung WHERE VID = {vid}'))
  print(vid, res)
  return res

@anvil.server.callable
def get_zelle(gid):
  conn = sqlite3.connect(data_files['prison_management.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f'SELECT Zellennummer FROM Zelle WHERE Name = {gid}'))
  print(gid, res)
  return res