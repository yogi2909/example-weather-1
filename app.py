# https://www.metricfire.com/blog/develop-and-deploy-a-python-api-with-kubernetes-and-docker-part-ii/
# https://medium.com/@javatechie/kubernetes-tutorial-install-run-minikube-in-mac-os-k8s-cluster-369b25b0c3f0
# https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/#install-kubectl-binary-with-curl-on-macos
# https://github.com/sagunsh/weather-app
# https://console.cloud.google.com/apis/dashboard?project=plenary-glass-376602
# https://codelabs.developers.google.com/codelabs/cloud-deploy-website-on-gke#0

# 1. install python3
# 2. install pip3 (python package manager installer)
# 3. install vm
# 4. install docker
# 5. install gcp cli 
# 6. install brew ( mac package installer manager for kubernetes)
# 6. install kubernetes
# 7. install minicube1
# 8. Enable API service : gcloud services enable container.googleapis.com
# 8. create git account on github and install git cli

from flask import Flask
import requests
import os
app = Flask(__name__)
# API_KEY = os.environ['API_KEY']
#APP_KEY="89347981879807c589923f541135dd8c"
# APP_KEY="7fe977285a267e0a10dfe72a905882de"

@app.route('/')
def index():
    return 'App Works!'

@app.route('/<string:city>/<string:country>/')
def weather_by_city(country, city):
    url = 'https://samples.openweathermap.org/data/2.5/weather'
    params = dict(
        q=city + "," + country,
        appid= API_KEY,
    )
    response = requests.get(url=url, params=params)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
