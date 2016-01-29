#!/usr/bin/python
#
# This script gathers weather data from wunderground api so it can be displayed in
# OpenNMS.
#
# Copyright 2016 Jeremy Ford - jeremyfo@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import requests
import urllib

# Add your API key below
API_KEY = "api_key"

# Change your location in the below URLS.
conditions_req_url = "http://api.wunderground.com/api/" + API_KEY + "/conditions/q/CA/San_Francisco.json"
alerts_req_url = "http://api.wunderground.com/api/" + API_KEY + "/alerts/q/CA/San_Francisco.json"
radar_req_url = "http://api.wunderground.com/api/" + API_KEY + "/animatedradar/q/CA/San_Francisco.gif?newmaps=1&timelabel=1&timelabel.y=10&num=5&delay=50&width=450&height=450&radius=100"
###

# Get Current Conditions
conditions_req = requests.get(conditions_req_url)
myData = conditions_req.json()

# Get Current Alerts
alerts_req = requests.get(alerts_req_url)
myAlerts = alerts_req.json()

# We need to save the radar.gif locally so everytime we reload OpenNMS it doesnt
# count against our api quota
radar = urllib.urlretrieve(radar_req_url,'/opt/opennms/jetty-webapps/opennms/includes/radar.gif')

conditions = ("<b>Current Weather Conditions: " + str(myData['current_observation']['weather']) + "</b>")
temp = ("<b>Temperature: " + str(myData['current_observation']['temp_f']) + "</b>")
humidty = ("<b>Humidity: " + str(myData['current_observation']['relative_humidity']) + "</b>")
wind = ("<b>Wind: " + str(myData['current_observation']['wind_string']) + "</b>")
pressure = ("<b>Pressure: " + str(myData['current_observation']['pressure_mb']) + "</b>")
dew = ("<b>DewPoint: " + str(myData['current_observation']['dewpoint_f']) + "</b>")
feels = ("<b>Feels Like: " + str(myData['current_observation']['feelslike_f']) + "</b>")
precip = ("<b>Precipitation: " + str(myData['current_observation']['precip_today_in']) + "</b>")
obsv = ("<i>Observation Time: " + str(myData['current_observation']['observation_time'] + "</i>"))
icon = (str(myData['current_observation']['icon_url']))

html_top = """
<%@page language="java"
        contentType="text/html"
        session="true"
%>

<div class="panel panel-default">
        <div class="panel-heading">
                <h3 class="panel-title">Current Weather</a></h3>
        </div>
"""

html_bot = """
</div>
"""

myFile = open('/opt/opennms/jetty-webapps/opennms/includes/weather.jsp', 'w+')
myFile.write(html_top + '\n')
myFile.write('<ul style="list-style-type:none">' + '\n')
myFile.write('<li>' + '<img src="' + icon +'" alt="Current Conditions">' + '</li>' + '\n')
myFile.write('<li>' + temp + '</li>' + '\n')
myFile.write('<li>' + humidty + '</li>' + '\n')
myFile.write('<li>' + wind + '</li>' + '\n')
myFile.write('<li>' + pressure + '</li>' + '\n')
myFile.write('<li>' + dew + '</li>' + '\n')
myFile.write('<li>' + feels + '</li' + '\n')
myFile.write('<li>' + precip + '</li>' + '\n')
if not len(myAlerts['alerts']):
    noAlert = ("<b>There are currently no alerts for {0}".format(myData['current_observation']['display_location']['full']) + '</b>')
    myFile.write('<li>' + noAlert + '</li>' + '\n')
for alert in myAlerts['alerts']:
    Alert = ('<b>' + str(alert['description']) + "\nExpires: " + str(alert['expires']) + '</b>')
    myFile.write('<li><font color=red>' + Alert + '</font></li>' + '\n')
myFile.write('<li>' + obsv + '</li></ul>' + '\n')
myFile.write('<hr>' + '\n')
myFile.write('<img src="/opennms/includes/radar.gif">' + '\n')
myFile.write(html_bot + '\n')
myFile.close()
