import logging
import os

from click.testing import CliRunner

from app import create_database

runner = CliRunner()




def test_create_database():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True

#Test for CSV File
import os

root = os.path.dirname(os.path.abspath(__file__))
csvdir = os.path.join(root, '../app/uploads/music.csv')

def test_request_songs(client):
    response = client.get("/songs")
    assert response.status_code == 200
    assert b"Browse: Songs" in response.data

def test_songs_upload(application):
    """Check to see if CSV file is uploaded and processed"""
    assert os.path.exists(csvdir) is True
    filepath = os.path.join(root, '../app/uploads/music.csv')
    assert os.path.exists(filepath) is True