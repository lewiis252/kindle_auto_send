# kindle_auto_send
This script automatically sent files from files_to_sent folder to your kindle and move sended files to sended folder. Just change your mail, kindle's mail and password.
Remember, you must do something like Turn Allow less secure apps to ON in your email service (gmail in this example)

## Requirements
``` sh
pip install -r requirements.txt
```

## Usage of app

```sh
git clone https://github.com/lewiis252/kindle_auto_send.git
```

After setting your virtual enviroment you must provide your emails and password - create .env file in the same directory as kindle_auto_sent.py and fill it like this:

```sh
# login settings
sender_email = 'my_email.com'
receiver_email = 'my_device_mail@kindle.com'
password = 'passsword'
```

Then simply run that file. 

## New google security policy
Follow this guide to send via gmail. 
https://stackoverflow.com/questions/72478573/sending-and-email-using-python-problem-causes-by-last-google-policy-update-on
