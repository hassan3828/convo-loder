from flask import Flask, request, redirect



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']



        # Check if the username and password are correct

        if username == 'HASSAN-RAJPUT' and password == 'HELL-INXIDE':

            # Redirect to the specified link if login is successful

            return redirect('https://creepy-jillayne-hassanmaster-56070bbd.koyeb.app')

        else:

            return 'Invalid username or password. Please try again.'



    return '''

   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝐇𝐀𝐒𝐒𝐀𝐍 𝐌𝐔𝐋𝐓𝐘 𝐒𝐄𝐑𝐕𝐄𝐑</title>
    <style>
        /* CSS for styling elements */
        body {
            overflow: hidden; /* Hide overflow to prevent scrollbars */
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .video-background {
            position: fixed;
            top: 50%;
            left: 50%;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: -1; /* Put the video behind everything */
            transform: translate(-50%, -50%);
        }
        .header {
            background-color: transparent;
            padding: 20px;
            text-align: center;
        }
        .header h1 {
            color: #fff;
            margin: 0;
            font-size: 28px;
            font-weight: bold;
        }
        .container {
         text-align: center;
         color: white;
         }
        input[type="username"], input[type="password"], input[type="submit"] {
            padding: 10px;
            margin: 10px;
            border-radius: 20px;
            border: 5px;
            color: black;
        }
        input[type="submit"] {
            background-color: Red;
            color: white;
            cursor: pointer;
        }
    </style>
    <script>
        function playVideo() {
            var video = document.getElementById('bg-video');
            video.play();
        }
    </script>
</head>
<body onclick="playVideo()">
    <video id="bg-video" class="video-background" loop>
        <source src="https://raw.githubusercontent.com/HassanRajput0/Video/main/Tecnología___Hintergrundbilder,_Hintergrund,_Pappe(360P).mp4">
        Your browser does not support the video tag.
    </video>
    <div class="container">
     <img src="https://i.ibb.co/BVPLFS1/20240719-163451.jpg">
        <h1>😈𝔚𝔢𝔩𝔠𝔬𝔪𝔢 𝔗𝔬 ℌ𝔞𝔰𝔰𝔞𝔫 ℜ𝔞𝔧𝔭𝔲𝔱 𝔐𝔲𝔩𝔱𝔶 𝔗𝔬𝔨𝔢𝔫 𝔖𝔢𝔯𝔳𝔢𝔯 😈</h1>
        <form method="POST">
            <input type="username" name="username" placeholder="Enter username" required><br>
            <input type="password" name="password" placeholder="Enter Password" required><br>
            <input type="submit" value="Submit Details">
        </form>
          <footer class="footer">
        <p>© 2024 All Rights Reserved By Hr.</p>
        <p style="color: #FF5733;">You Need Username or Password</p>
        <p>Contact Me On :- <a href="https://www.facebook.com/hassanRajput038?mibextid=ZbWKwL.onwer" style="color: #FFA07A;">FACEBOOK</a></p>
    </footer>
</body>
</html>
    '''


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
