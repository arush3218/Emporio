from flask import Flask, jsonify, send_file
import firebase_admin
from firebase_admin import credentials, db
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

# Initialize Firebase Admin SDK with service account credentials
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "emporio-39652",
    "private_key_id": "77f45e2dee8a0a16c4d20aa3c43f03d8f4ea62ff",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCgSaAA07ucxblu\nr1px264sD0EJvo5fhM5rszZM/31KUlcSana7mRWLbz9l9GNVeyk3ZnrrFeQaNr9E\n9sKszBaXaigBBfdxqKRZsr8EgdEbhkS+KJvGu3Z8A3O+NzoyHS7Dyx78BP/TyuP9\nP83eEzwDLLXG82gw7zSl4Bsb/zmNHbx8Ite0Yggc6S+dcvyuuelxw1ArcyCMJiio\nKN/T1yEOIp3fRTZ4tai0Aezc6ilUaw7PZUou6qbLuXplK+yu1FXNXhKhma8N2qlo\n9nZawS8xFi8ij21AYuSrYOOWRv5zf3NBvr++iVsn63FFol/q1pcZQDEu6V5NmC6n\nZ4na+MKfAgMBAAECggEAJUHn3Llany7Akw9UfSm8mwYyrnKqQl6q4pLmGNC8TUXF\ncoTns2R6gw4pVOgRHOIDaxq5kKJmgodeP0gCaUsJJ0noIZDC+xrhlO39A62vLvAv\nU2o6B2A0ws/EnB7XOqXY5G729UquMoszIn8tuaSL6wr999BFVDaN7M6iTogtVvUH\nvwImYviLO4aBuxZajs33O6rm1Si72Kq2VD5+ONfWlcxXJPgeRgPBg+GQHfy2Ol7H\nBPzAUierfxHazqxiDDpQ4Ewsuvoqf89Zxoo2SekCNQ/KRxJ9pcfgN83/oO60DcZ0\nk2IQq1MXK/Tnydy+/CoasIdwZdt26ylUT/L+UxIU5QKBgQDUeigiR2FkQlLhdXdl\npF3qoGZ4tm+hly2jvgtr7GbhXGBgKPIam/r66poDx/0bHQrG5io4tMO/qcmKY8ut\n6zB2xdSxcrfPqKFcA7dZjfEnnK1a/680z8t3deUX2TZoNDg248Zqel+BH6nOnovX\n8i1//zGds1+QOgGQsIrgeXdjawKBgQDBHsJ/XKKyQS+7M+NDIU5oaQSKFeVW0da7\nkLk2CfjMsetuZlHYKSh9tqq8YSGm2vks3gRnlFnpf4CBU6RYD/iVdHdbEEPloWfC\nLP3lGPwoYc0S1pfYgw0uAqt5E1hHDbydAeA71WnppLOtyBNmSX3LYDuU0Ee5Cvi5\nuLp+Ch7enQKBgGSzEFpOoiW2GTmpRlDxuWD9bBNBw14+G+9Cnn8jpw6fjT2Fqlha\nHHTWwu+P1LEI7paddt0xLqSjf1ULPvjKQknIMKl4yQytyuulBzx2PRic9Lvv+cV5\nxeB0C4Nl+pcgSJQbF2pXXPQBYaT/Fx/dMxs6gvVOkbf1BdDhGrCQYLjJAoGBAInQ\n2rorMIwHCvoMWGWCskK+lxe38ndXvmcSK6pNyXjCi6G4cTXSgWvdXNCcfHhnkiSb\nuAb3Doccj2c7em/BzgNSHw8kd1+7JKGkm/fPMbvbt453B9viAhjQnPAFhx0Fx5FA\nUnZAoZm0COm+e2Gmlpf5b+uOC3EZTFC1bJkfvdHdAoGAIiHaIXL7NmEvVbWjf7LH\nXNlAn/UUfMv7Wxraf2qWqa1awfNitL+wohF0ecGBraFW5vswK9oPajs+kZRh4pbL\nBexGQnw/gso9KcYIqe6hl45CKO3LPOaNP525vkts/cF4vWOcNFgAAgNT75CwoNK4\nR8laA4XZfMI9OmNc3Q32lj4=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-urtfc@emporio-39652.iam.gserviceaccount.com",
    "client_id": "110013641371374482837",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-urtfc%40emporio-39652.iam.gserviceaccount.com"
})

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://emporio-39652.firebaseio.com/'
})

@app.route('/api/data')
def get_data():
    # Fetch data from Firebase (replace this with your actual data fetching code)
    ref = db.reference('/path/to/data')  # Adjust the path to your data
    data = ref.get()

    # Return the fetched data as JSON
    return jsonify(data)

@app.route('/api/plot')
def generate_plot():
    # Generate a sample Seaborn plot (replace this with your actual plot generation code)
    sns.set(style="whitegrid")
    data = sns.load_dataset("iris")
    plot = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=data)
    
    # Save the plot to a BytesIO buffer
    buffer = BytesIO()
    plot.figure.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Return the plot as an image file
    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)