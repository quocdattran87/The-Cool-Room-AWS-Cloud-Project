from __future__ import print_function

endpoint = 'aa13ipuz8bmkd6g.crzhjgnecjeb.ap-southeast-2.rds.amazonaws.com'
username = 'Foffman'
password = 'Password123!'
database_name = 'ebdb'


import json
import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect(host=endpoint, user=username, password=password, dbname=database_name)

def lambda_handler(event, context):
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    
    # GET
    if event['rawPath'] == '/getRooms':
        query = event['queryStringParameters']['query']
        cursor.execute('SELECT base_room.id,base_room.name,base_room.description,base_room.updated,base_room.created,base_room.host_id,base_room.topic_id FROM base_room JOIN base_topic ON base_room.topic_id = base_topic.id JOIN base_user ON base_room.host_id = base_user.id WHERE lower(base_topic.name) LIKE \'%{}%\' OR lower(base_room.name) LIKE \'%{}%\' OR lower(base_room.description) LIKE \'%{}%\' OR lower(base_user.username) LIKE \'%{}%\''.format(query.lower(),query.lower(),query.lower(),query.lower()))
    elif event['rawPath'] == '/getTopics':
        query = event['queryStringParameters']['query']
        cursor.execute('SELECT * FROM base_topic WHERE lower(name) LIKE \'%{}%\''.format(query.lower()))
    elif event['rawPath'] == '/getUsers':
        cursor.execute('SELECT * FROM base_user')
    elif event['rawPath'] == '/getMessages':
        cursor.execute('SELECT * FROM base_message')
        
    # CREATE
    elif event['rawPath'] == '/createRoom':
        name = event['queryStringParameters']['name']
        description = event['queryStringParameters']['description']
        updated = event['queryStringParameters']['updated']
        created = event['queryStringParameters']['created']
        host_id = event['queryStringParameters']['host_id']
        topic_id = event['queryStringParameters']['topic_id']
        cursor.execute('INSERT INTO base_room (name, description, updated, created, host_id, topic_id) VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(name,description,updated,created,host_id,topic_id))
        connection.commit()
        return
        
    # DELETE
    elif event['rawPath'] == '/deleteRoom':
        query = event['queryStringParameters']['query']
        cursor.execute('DELETE FROM base_room_participants WHERE room_id = {}'.format(int(query)))
        cursor.execute('DELETE FROM base_room WHERE id = {}'.format(int(query)))
        connection.commit()
        return
    elif event['rawPath'] == '/deleteMessage':
        query = event['queryStringParameters']['query']
        cursor.execute('DELETE FROM base_message WHERE id = {}'.format(int(query)))
        connection.commit()
        return
    
    rows = cursor.fetchall()

    return {
        'statusCode': 200,
        'body': json.dumps(rows, indent=4, sort_keys=True, default=str)
    }