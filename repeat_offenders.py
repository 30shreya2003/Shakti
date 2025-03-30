from flask import Blueprint, jsonify, request
import sqlite3

repeat = Blueprint("repeat", __name__)

def get_db_connection():
    conn = sqlite3.connect("offenders.db")
    conn.row_factory = sqlite3.Row
    return conn

@repeat.route("/repeat_offenders", methods=["GET"])
def get_repeat_offenders():
    conn = get_db_connection()
    query = "SELECT Name, COUNT(*) as Cases FROM complaints GROUP BY Name HAVING COUNT(*) > 1"
    df = conn.execute(query).fetchall()
    conn.close()
    
    repeat_offenders = [{"Name": row["Name"], "Cases": row["Cases"]} for row in df]
    return jsonify(repeat_offenders)

@repeat.route("/crime_locations", methods=["GET"])
def get_crime_locations():
    conn = get_db_connection()
    query = "SELECT Location, Crime_Type, COUNT(*) as Cases FROM complaints GROUP BY Location, Crime_Type"
    df = conn.execute(query).fetchall()
    conn.close()
    
    crime_locations = [{"Location": row["Location"], "Crime_Type": row["Crime_Type"], "Cases": row["Cases"]} for row in df]
    return jsonify(crime_locations)


@repeat.route("/check_risk", methods=["POST"])
def check_risk():
    data = request.json
    offender = data.get("offender")
    location = data.get("location")

    conn = get_db_connection()
    query = "SELECT COUNT(*) as Cases FROM complaints WHERE Name = ? AND Location = ?"
    result = conn.execute(query, (offender, location)).fetchone()
    conn.close()

    return jsonify({"risk": "High Risk" if result["Cases"] > 1 else "Low Risk"})
