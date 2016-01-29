# weather.py

[OpenNMS](http://opennms.org) is the world’s first enterprise grade network management application platform developed under the open source model. This python script will display weather data and a radar map on the OpenNMS home page.

## Install
1. Setup a developer api key on wunderground http://www.wunderground.com/weather/api
2. Edit `weather.py` add your API_KEY and change your location
3. Copy weather.py to `/opt/opennms/bin`
4. Create a cronjob that will run the weather.py script periodically `*/10 * * * * /bin/python /opt/opennms/bin/weather.py > /dev/null 2>&1`
5. Edit `/opt/opennms/jetty-webapps/opennms/index.jsp` and add the below block of code.
```
<!-- weather box -->
<jsp:include page="/includes/weather.jsp" flush="false" />
```
To add the weather panel to the top of the right column the code would look like
```
<!-- Right Column -->
        <div class="col-md-3" id="index-contentright">
                <!-- weather box -->
                <jsp:include page="/includes/weather.jsp" flush="false" />
```
## Screenshot
![weather.py screenshot](https://raw.githubusercontent.com/jeremyfo/opennms-weather/master/SCREENSHOT.PNG)

## Issues
This script has been tested against OpenNMS Horizon 16 and Horizon 17. After each OpenNMS upgrade you will need to add the code block back to `index.jsp`

Please report issues on the issue tracker or contact jeremyfo@gmail.com
