#!/usr/bin/bash/env python
from flask import Flask, render_template, Markup, request
import os, sqlite3
from flask.helpers import send_file
import csv
import paramiko
import sys
import threading
import subprocess
import array
import sqlite3
import time
import re
import signal
from prettytable import PrettyTable

#Assigning Database name for the functions to use
db=sqlite3.connect("userInput.sq3", check_same_thread=False)
db.row_factory=sqlite3.Row
cursor=db.cursor()

app = Flask(__name__)

#Function for index page
@app.route('/')
def startPage():
    bodyText=Markup("<b>Lab 7 Network Configuration Input</b>")
    return render_template('index.html', bodyText=bodyText)

#Function for router R1
@app.route('/form1')
def form1():
    return render_template("form1.html")

#Function for router R2
@app.route('/form2')
def form2():
    return render_template("form2.html")

#Function for router R3
@app.route('/form3')
def form3():
    return render_template("form3.html")

#Function to write user input of router R1 into file to be used by database
@app.route('/writeUserInput1', methods=['POST'])
def writeUserInput1():
    R1Username=request.form['R1Username']
    R1Password=request.form['R1Password']
    R1ProcessID=request.form['R1ProcessID']
    R1AreaID=request.form['R1AreaID']
    R1InterAreaID=request.form['R1AreaID']
    R1LoopbackIP=request.form['R1LoopbackIP']
    R1NetworkLeft=request.form['R1NetworkLeft']
    R1NetworkRight=request.form['R1NetworkRight']
    R1IP=request.form['R1IP']

    fs=open("./templates/userInput1.txt","w")
    fs.write('R1Username:'+R1Username+'\nR1Password:'+R1Password+'\nR1ProcessID:'+R1ProcessID+'\nR1AreaID:'+R1AreaID+'\nR1InterAreaID:'+R1InterAreaID+'\nR1LoopbackIP:'+R1LoopbackIP+'\nR1NetworkLeft:'+R1NetworkLeft+'\nR1NetworkRight:'+R1NetworkRight+'\nR1IP:'+R1IP)
    fs.close()

    return "Your configuration input is saved, you can close this window"

#Function to write user input of router R2 into file to be used by database
@app.route('/writeUserInput2', methods=['POST'])
def writeUserInput2():
    R2Username=request.form['R2Username']
    R2Password=request.form['R2Password']
    R2ProcessID=request.form['R2ProcessID']
    R2AreaID=request.form['R2AreaID']
    R2InterAreaID=request.form['R2InterAreaID']
    R2LoopbackIP=request.form['R2LoopbackIP']
    R2NetworkLeft=request.form['R2NetworkLeft']
    R2NetworkRight=request.form['R2NetworkRight']
    R2IP=request.form['R2IP']

    fs=open("./templates/userInput2.txt","w")
    fs.write('R2Username:'+R2Username+'\nR2Password:'+R2Password+'\nR2ProcessID:'+R2ProcessID+'\nR2AreaID:'+R2AreaID+'\nR2InterAreaID:'+R2InterAreaID+'\nR2LoopbackIP:'+R2LoopbackIP+'\nR2NetworkLeft:'+R2NetworkLeft+'\nR2NetworkRight:'+R2NetworkRight+'\nR2IP:'+R2IP)
    fs.close()

    return "Your configuration input is saved, you can close this window"

#Function to write user input of router R3 into file to be used by database
@app.route('/writeUserInput3', methods=['POST'])
def writeUserInput3():
    R3Username=request.form['R3Username']
    R3Password=request.form['R3Password']
    R3ProcessID=request.form['R3ProcessID']
    R3AreaID=request.form['R3AreaID']
    R3InterAreaID=request.form['R3AreaID']
    R3LoopbackIP=request.form['R3LoopbackIP']
    R3NetworkLeft=request.form['R3NetworkLeft']
    R3NetworkRight=request.form['R3NetworkRight']
    R3IP=request.form['R3IP']

    fs=open("./templates/userInput3.txt","w")
    fs.write('R3Username:'+R3Username+'\nR3Password:'+R3Password+'\nR3ProcessID:'+R3ProcessID+'\nR3AreaID:'+R3AreaID+'\nR3InterAreaID:'+R3InterAreaID+'\nR3LoopbackIP:'+R3LoopbackIP+'\nR3NetworkLeft:'+R3NetworkLeft+'\nR3NetworkRight:'+R3NetworkRight+'\nR3IP:'+R3IP)
    fs.close()

    return "Your configuration input is saved, you can close this window"

#Function to create database based on user input
@app.route('/createDB')
def createDB():
    query1="drop table if exists config"
    cursor.execute(query1)

    query2="create table config(name varchar(20), username varchar(50), password varchar(50), processID integer, areaID integer, interAreaID integer, loopbackIP double, networkLeft double, networkRight double, IP double)"
    cursor.execute(query2)

    f1=open("./templates/userInput1.txt")
    f2=open("./templates/userInput2.txt")
    f3=open("./templates/userInput3.txt")

    for lines in f1.readlines():
        if(lines.startswith("R1Username")):
            R1Username=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R1Password")):
            R1Password=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R1ProcessID")):
            R1ProcessID=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R1AreaID")):
            R1AreaID=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R1InterAreaID")):
            R1InterAreaID=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R1LoopbackIP")):
            R1LoopbackIP=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R1NetworkLeft")):
            R1NetworkLeft=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R1NetworkRight")):
            R1NetworkRight=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R1IP")):
            R1IP=lines.split(":")[1].strip("\n")
        else:
            print("R1 values not found")

    for lines in f2.readlines():
        if(lines.startswith("R2Username")):
            R2Username=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R2Password")):
            R2Password=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R2ProcessID")):
            R2ProcessID=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R2AreaID")):
            R2AreaID=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R2InterAreaID")):
            R2InterAreaID=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R2LoopbackIP")):
            R2LoopbackIP=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R2NetworkLeft")):
            R2NetworkLeft=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R2NetworkRight")):
            R2NetworkRight=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R2IP")):
            R2IP=lines.split(":")[1].strip("\n")
        else:
            print("R2 values not found")

    for lines in f3.readlines():
        if(lines.startswith("R3Username")):
            R3Username=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R3Password")):
            R3Password=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R3ProcessID")):
            R3ProcessID=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R3AreaID")):
            R3AreaID=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R3InterAreaID")):
            R3InterAreaID=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R3LoopbackIP")):
            R3LoopbackIP=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R3NetworkLeft")):
            R3NetworkLeft=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R3NetworkRight")):
            R3NetworkRight=lines.split(":")[1].strip("\n")
        elif(lines.startswith("R3IP")):
            R3IP=lines.split(":")[1].strip("\n")
        else:
            print("R3 values not found")

    query3="insert into config(name, username, password, processID, areaID, interAreaID, loopbackIP, networkLeft,networkRight,IP)values('R1',?,?,?,?,?,?,?,?,?)"

    t1=(R1Username,R1Password,R1ProcessID,R1AreaID,R1AreaID,R1LoopbackIP.strip("\n"),R1NetworkLeft,R1NetworkRight,R1IP)

    cursor.execute(query3,t1)

    query4="insert into config(name, username, password, processID, areaID, interAreaID, loopbackIP, networkLeft, networkRight, IP)values('R2',?,?,?,?,?,?,?,?,?)"

    t2=(R2Username,R2Password,R2ProcessID,R2AreaID,R2InterAreaID,R2LoopbackIP,R2NetworkLeft,R2NetworkRight,R2IP)

    cursor.execute(query4,t2)

    query5="insert into config(name, username, password, processID, areaID, interAreaID, loopbackIP, networkLeft,networkRight, IP)values('R3',?,?,?,?,?,?,?,?,?)"

    t3=(R3Username,R3Password,R3ProcessID,R3AreaID,R3AreaID,R3LoopbackIP,R3NetworkLeft,R3NetworkRight,R3IP)

    cursor.execute(query5,t3)

    db.commit()
    return 'Database created'    

#Function to parse values of R1, R2 and R3 from sqlite3 database
def parsingDB(routerName):
    networks=[]
    query6="select username from config where name='"+routerName+"'"
    query7="select password from config where name='"+routerName+"'"
    query8="select processID from config where name='"+routerName+"'"
    query9="select areaID from config where name='"+routerName+"'"
    query10="select interAreaID from config where name='"+routerName+"'"
    query11="select loopbackIP from config where name='"+routerName+"'"
    query12="select networkLeft from config where name='"+routerName+"'"
    query13="select networkRight from config where name='"+routerName+"'"
    query14="select IP from config where name='"+routerName+"'"
    
    cursor.execute(query6)
    row1=cursor.fetchall()
    for rows in row1:
        username=rows[0].strip("\n")
    cursor.execute(query7)
    row2=cursor.fetchall()
    for rows in row2:   
        password=rows[0].strip("\n")
    cursor.execute(query8)
    row3=cursor.fetchall()
    for rows in row3:
        processID=rows[0]
    cursor.execute(query9)
    row4=cursor.fetchall()
    for rows in row4:   
        areaID=rows[0]
    cursor.execute(query10)
    row5=cursor.fetchall()
    for rows in row5:
        interAreaID=rows[0]
    cursor.execute(query11)
    row6=cursor.fetchall()
    for rows in row6:
        loopbackIP=rows[0]
    cursor.execute(query12)
    row7=cursor.fetchall()
    for rows in row7:
        networkLeft=rows[0]
    cursor.execute(query13)
    row8=cursor.fetchall()
    for rows in row8:
        networkRight=rows[0]
    cursor.execute(query14)
    row8=cursor.fetchall()
    for rows in row8:
        IP=rows[0]

    return username,password,processID,areaID,interAreaID,loopbackIP,networkLeft,networkRight,IP

#Function to test OSPF neighbors establishment using ping between R1 and R3
def pingTest(R1IP,username,password,R3IP):
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(R1IP, username = username, password = password)
    connection = session.invoke_shell()
    connection.send("terminal length 0\n")
    time.sleep(2)
    connection.send("\n")
    connection.send("ping "+R3IP+" source "+R1IP+"\n")
    time.sleep(5)
    connection.send("\n")
    
    pingOutput = connection.recv(65535)
    fp=open("pingResults","wa")
    fp.write(pingOutput)
    fp.close()
    fr=open("pingResults")
    for lines in fr.readlines():
        if(lines.startswith("Success")):   
            print("OSPF has been successfully configured")
    
    session.close()

#Function to see the neighbors of R2
def showRouter(name, IP, username, password):
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(IP, username = username, password = password)
    connection = session.invoke_shell()
    connection.send("terminal length 0\n")
    time.sleep(2)
    connection.send("\n")
    connection.send("show ip ospf neighbor\n")
    time.sleep(5)
    showOutput=connection.recv(65535)
    fs=open("neighborResults"+name,"wa")
    fs.write(showOutput)
    fs.close()
    table=PrettyTable(["Neighbor ID", "State", "Interface"])
    neighborID=[]
    state=[]
    interface=[]
    fo=open("neighborResults"+name)
    for lines in fo.readlines():
        pattern=re.compile(r'^\b[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\b')
        if(pattern.match(lines)):    
            neighborID.append(lines.split()[0])
            state.append(lines.split()[2])
            interface.append(lines.split()[5])
    if(name=='R2'):
        size=len(neighborID)
        for value in range(0,size):
            table.add_row([neighborID[value],state[value],interface[value]])
        print("\nR2:")
        print(table)    

    session.close()

#Function to configure the routers R1, R2 and R3
def deviceConfig(name, username, password, processID, areaID, interAreaID, loopbackIP, networkLeft, networkRight, IP):

    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(IP, username = username, password = password)
    connection = session.invoke_shell()
    connection.send("terminal length 0\n")
    time.sleep(2)
    connection.send("\n")
    connection.send("configure terminal\n")
    time.sleep(2)
    connection.send("\n")
    connection.send("router ospf "+str(processID)+"\n")
    time.sleep(2)
    connection.send("\n")
    connection.send("network "+str(networkLeft)+" area "+str(areaID)+"\n")
    connection.send("network "+str(networkRight)+" area "+str(interAreaID)+"\n")
    connection.send("network "+str(loopbackIP)+" area "+str(areaID)+"\n")
    time.sleep(2)
    connection.send("\n")   
    connection.send("exit\n")
    time.sleep(2)
    connection.send("\n")
    connection.send("do terminal length 0\n")
    time.sleep(2)
    connection.send("\n")
    routerOutput=connection.recv(65535)
    fs=open("ospfResults"+name,"wa")
    fs.write(routerOutput)
    fs.close()
    print("SSH is successful to ip address "+str(IP)+", check file ospfResults"+name+" for detail output")
    
    session.close()

#Function to extract R1, R2 and R3 values from sqlite3 database
def networkConfig(num):
    if(num==1):
        R1Username,R1Password,R1ProcessID,R1AreaID,R1InterAreaID,R1LoopbackIP,R1NetworkLeft,R1NetworkRight,R1IP=parsingDB("R1")
        deviceConfig("R1",R1Username,R1Password,R1ProcessID,R1AreaID,R1InterAreaID,R1LoopbackIP,R1NetworkLeft,R1NetworkRight,R1IP)
    if(num==2):
        R2Username,R2Password,R2ProcessID,R2AreaID,R2InterAreaID,R2LoopbackIP,R2NetworkLeft,R2NetworkRight,R2IP=parsingDB("R2")
        deviceConfig("R2",R2Username,R2Password,R2ProcessID,R2AreaID,R2InterAreaID,R2LoopbackIP,R2NetworkLeft,R2NetworkRight,R2IP)
    if(num==3):
        R3Username,R3Password,R3ProcessID,R3AreaID,R3InterAreaID,R3LoopbackIP,R3NetworkLeft,R3NetworkRight,R3IP=parsingDB("R3")
        deviceConfig("R3",R3Username,R3Password,R3ProcessID,R3AreaID,R3InterAreaID,R3LoopbackIP,R3NetworkLeft,R3NetworkRight,R3IP)

    if(num==4):
        R1Username,R1Password,R1ProcessID,R1AreaID,R1InterAreaID,R1LoopbackIP,R1NetworkLeft,R1NetworkRight,R1IP=parsingDB("R1")
        R3Username,R3Password,R3ProcessID,R3AreaID,R3InterAreaID,R3LoopbackIP,R3NetworkLeft,R3NetworkRight,R3IP=parsingDB("R3")

        pingTest(R1IP,R1Username,R1Password,R3IP)
    if(num==5):
        R2Username,R2Password,R2ProcessID,R2AreaID,R2InterAreaID,R2LoopbackIP,R2NetworkLeft,R2NetworkRight,R2IP=parsingDB("R2")
        showRouter('R2', R2IP, R2Username, R2Password)

#Function to start network configuration
@app.route('/networkConfiguration')
def networkConfiguration():
    num=1
    while(num<=3):
        thread1=threading.Thread(target=networkConfig, args=(num, ))
        print("!!!!!!!!!!!!!!!!!!Thread "+thread1.getName()+" started!!!!!!!!!!!!")
        thread1.start()
        num=num+1

    networkConfig(4) #Ping test R3 and R1
    tableOutput=networkConfig(5) #R2 show ip ospf neighbor display
    return "Network configuration is complete and check terminal screen for output table. Please go to main page for options"

@app.route('/shutdownServer')
def shutdownServer():
    print("Thank you for using this server")
    #os.system("killall -KILL python")
    #os.kill(os.getpid(), signal.SIGTERM)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=8888)
 
